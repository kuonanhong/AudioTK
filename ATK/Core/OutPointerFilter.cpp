/**
 * \file OutPointerFilter.cpp
 */

#include <ATK/Core/OutPointerFilter.hxx>

#include <complex>

namespace ATK
{
  template class OutPointerFilter<std::int16_t>;
  template class OutPointerFilter<std::int32_t>;
  template class OutPointerFilter<std::int64_t>;
  template class OutPointerFilter<float>;
  template class OutPointerFilter<double>;
  template class OutPointerFilter<std::complex<float>>;
  template class OutPointerFilter<std::complex<double>>;
}
