/**
 * \file WaveshapperFilter.h
 */

#ifndef ATK_DISTORTION_WAVESHAPER_H
#define ATK_DISTORTION_WAVESHAPER_H

#include <cassert>
#include <vector>

#include <ATK/Core/TypedBaseFilter.h>
#include "config.h"

namespace ATK
{
  /// Waveshapper generic filter. Based on a LUT table, compute the shape.
  template<class ParentFilter>
  class WaveshaperFilter final : public ParentFilter
  {
  public:
    typedef ParentFilter Parent;
    using typename Parent::DataType;
    using Parent::converted_inputs;
    using Parent::outputs;
    using Parent::threshold;
    using Parent::nb_input_ports;
    using Parent::nb_output_ports;
    using Parent::computeGain;
    using Parent::LUTsize;
    using Parent::LUTprecision;
    using Parent::gainLUT;

    WaveshaperFilter(std::size_t nb_channels = 1, size_t LUTsize = 128 * 1024, size_t LUTprecision = 1024)
    :Parent(nb_channels, nb_channels), LUTsize(LUTsize), LUTprecision(LUTprecision), positiveShaperLUT(LUTsize, 0), negativeShaperLUT(LUTsize, 0)
    {
    }

    ~WaveshaperFilter()
    {
    }

  protected:
    virtual void process_impl(std::size_t size) const override final
    {
      assert(nb_input_ports == nb_output_ports);

      for (unsigned int channel = 0; channel < nb_output_ports; ++channel)
      {
        const auto* ATK_RESTRICT input = converted_inputs[channel];
        auto* ATK_RESTRICT output = outputs[channel];
        for (std::size_t i = 0; i < size; ++i)
        {
          if(input[i] < 0)
          {
            size_t step = static_cast<size_t>(-input[i] * LUTprecision);
            if (step >= LUTsize)
            {
              step = static_cast<int>(LUTsize) - 1;
            }
            output[i] = negativeShaperLUT[step];
          }
          else
          {
            size_t step = static_cast<size_t>(input[i] * LUTprecision);
            if (step >= LUTsize)
            {
              step = static_cast<int>(LUTsize) - 1;
            }
            output[i] = positiveShaperLUT[step];
          }
        }
      }
    }

    size_t LUTsize;
    size_t LUTprecision;
    std::vector<DataType_> positiveShaperLUT;
    std::vector<DataType_> negativeShaperLUT;
  };
}

#endif
