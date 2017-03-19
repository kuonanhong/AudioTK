#!/usr/bin/env python

from ATK.Core import DoubleInPointerFilter, DoubleOutPointerFilter
from ATK.Tools import DoubleOversampling6points5order_32Filter, DoubleOversampling6points5order_16Filter, DoubleOversampling6points5order_8Filter, DoubleOversampling6points5order_4Filter, DoubleDecimationFilter
from ATK.EQ import DoubleButterworthLowPassFilter, DoubleSD1ToneFilter, DoubleChamberlinFilter
from ATK.Distortion import DoubleSD1OverdriveFilter

sample_rate = 48000

def filter_32(input):
  import numpy as np
  output = np.zeros(input.shape, dtype=np.float64)

  inputfilter = DoubleInPointerFilter(input, False)
  inputfilter.set_input_sampling_rate(sample_rate)
  infilter = DoubleChamberlinFilter()
  infilter.set_input_sampling_rate(sample_rate)
  infilter.set_input_port(0, inputfilter, 0)
  infilter.select(0)
  infilter.set_attenuation(1)
  infilter.set_cut_frequency(1000)
  overfilter = DoubleOversampling6points5order_32Filter()
  overfilter.set_input_sampling_rate(sample_rate)
  overfilter.set_output_sampling_rate(sample_rate * 32)
  overfilter.set_input_port(0, infilter, 0)
  overdrivefilter = DoubleSD1OverdriveFilter()
  overdrivefilter.set_input_sampling_rate(sample_rate * 32)
  overdrivefilter.set_input_port(0, overfilter, 0)
  overdrivefilter.set_drive(0.9)
  lowpassfilter = DoubleButterworthLowPassFilter()
  lowpassfilter.set_input_sampling_rate(sample_rate * 32)
  lowpassfilter.set_cut_frequency(20000)
  lowpassfilter.set_order(5)
  lowpassfilter.set_input_port(0, overdrivefilter, 0)
#  lowpassfilter2 = DoubleButterworthLowPassFilter()
#  lowpassfilter2.set_input_sampling_rate(sample_rate * 32)
#  lowpassfilter2.set_cut_frequency(20000)
#  lowpassfilter2.set_order(5)
#  lowpassfilter2.set_input_port(0, lowpassfilter, 0)
#  lowpassfilter3 = DoubleButterworthLowPassFilter()
#  lowpassfilter3.set_input_sampling_rate(sample_rate * 32)
#  lowpassfilter3.set_cut_frequency(20000)
#  lowpassfilter3.set_order(5)
#  lowpassfilter3.set_input_port(0, lowpassfilter2, 0)
  decimationfilter = DoubleDecimationFilter(1)
  decimationfilter.set_input_sampling_rate(sample_rate * 32)
  decimationfilter.set_output_sampling_rate(sample_rate)
  decimationfilter.set_input_port(0, lowpassfilter, 0)
  #tonefilter = DoubleSD1ToneFilter()
  #tonefilter.set_input_sampling_rate(sample_rate)
  #tonefilter.set_input_port(0, decimationfilter, 0)
  #tonefilter.set_tone(1)
  #highpassfilter = DoubleChamberlinFilter()
  #highpassfilter.set_input_sampling_rate(sample_rate)
  #highpassfilter.set_input_port(0, tonefilter, 0)
  #highpassfilter.select(2)
  #highpassfilter.set_attenuation(1)
  #highpassfilter.set_cut_frequency(20)
  outfilter = DoubleOutPointerFilter(output, False)
  outfilter.set_input_sampling_rate(sample_rate)
  #outfilter.set_input_port(0, highpassfilter, 0)
  outfilter.set_input_port(0, decimationfilter, 0)
  outfilter.process(input.shape[1])
  return output

def filter_16(input):
  import numpy as np
  output = np.zeros(input.shape, dtype=np.float64)

  inputfilter = DoubleInPointerFilter(input, False)
  inputfilter.set_input_sampling_rate(sample_rate)
  infilter = DoubleChamberlinFilter()
  infilter.set_input_sampling_rate(sample_rate)
  infilter.set_input_port(0, inputfilter, 0)
  infilter.select(0)
  infilter.set_attenuation(1)
  infilter.set_cut_frequency(1000)
  overfilter = DoubleOversampling6points5order_16Filter()
  overfilter.set_input_sampling_rate(sample_rate)
  overfilter.set_output_sampling_rate(sample_rate * 16)
  overfilter.set_input_port(0, infilter, 0)
  overdrivefilter = DoubleSD1OverdriveFilter()
  overdrivefilter.set_input_sampling_rate(sample_rate * 16)
  overdrivefilter.set_input_port(0, overfilter, 0)
  overdrivefilter.set_drive(0.9)
  lowpassfilter = DoubleButterworthLowPassFilter()
  lowpassfilter.set_input_sampling_rate(sample_rate * 16)
  lowpassfilter.set_cut_frequency(sample_rate)
  lowpassfilter.set_order(5)
  lowpassfilter.set_input_port(0, overdrivefilter, 0)
  decimationfilter = DoubleDecimationFilter(1)
  decimationfilter.set_input_sampling_rate(sample_rate * 16)
  decimationfilter.set_output_sampling_rate(sample_rate)
  decimationfilter.set_input_port(0, lowpassfilter, 0)
  #tonefilter = DoubleSD1ToneFilter()
  #tonefilter.set_input_sampling_rate(sample_rate)
  #tonefilter.set_input_port(0, decimationfilter, 0)
  #tonefilter.set_tone(1)
  #highpassfilter = DoubleChamberlinFilter()
  #highpassfilter.set_input_sampling_rate(sample_rate)
  #highpassfilter.set_input_port(0, tonefilter, 0)
  #highpassfilter.select(2)
  #highpassfilter.set_attenuation(1)
  #highpassfilter.set_cut_frequency(20)
  outfilter = DoubleOutPointerFilter(output, False)
  outfilter.set_input_sampling_rate(sample_rate)
  #outfilter.set_input_port(0, highpassfilter, 0)
  outfilter.set_input_port(0, decimationfilter, 0)
  outfilter.process(input.shape[1])
  return output

def filter_8(input):
  import numpy as np
  output = np.zeros(input.shape, dtype=np.float64)

  inputfilter = DoubleInPointerFilter(input, False)
  inputfilter.set_input_sampling_rate(sample_rate)
  infilter = DoubleChamberlinFilter()
  infilter.set_input_sampling_rate(sample_rate)
  infilter.set_input_port(0, inputfilter, 0)
  infilter.select(0)
  infilter.set_attenuation(1)
  infilter.set_cut_frequency(1000)
  overfilter = DoubleOversampling6points5order_8Filter()
  overfilter.set_input_sampling_rate(sample_rate)
  overfilter.set_output_sampling_rate(sample_rate * 8)
  overfilter.set_input_port(0, infilter, 0)
  overdrivefilter = DoubleSD1OverdriveFilter()
  overdrivefilter.set_input_sampling_rate(sample_rate * 8)
  overdrivefilter.set_input_port(0, overfilter, 0)
  overdrivefilter.set_drive(0.9)
  lowpassfilter = DoubleButterworthLowPassFilter()
  lowpassfilter.set_input_sampling_rate(sample_rate * 8)
  lowpassfilter.set_cut_frequency(sample_rate)
  lowpassfilter.set_order(5)
  lowpassfilter.set_input_port(0, overdrivefilter, 0)
  decimationfilter = DoubleDecimationFilter(1)
  decimationfilter.set_input_sampling_rate(sample_rate * 8)
  decimationfilter.set_output_sampling_rate(sample_rate)
  decimationfilter.set_input_port(0, lowpassfilter, 0)
  #tonefilter = DoubleSD1ToneFilter()
  #tonefilter.set_input_sampling_rate(sample_rate)
  #tonefilter.set_input_port(0, decimationfilter, 0)
  #tonefilter.set_tone(1)
  #highpassfilter = DoubleChamberlinFilter()
  #highpassfilter.set_input_sampling_rate(sample_rate)
  #highpassfilter.set_input_port(0, tonefilter, 0)
  #highpassfilter.select(2)
  #highpassfilter.set_attenuation(1)
  #highpassfilter.set_cut_frequency(20)
  outfilter = DoubleOutPointerFilter(output, False)
  outfilter.set_input_sampling_rate(sample_rate)
  #outfilter.set_input_port(0, highpassfilter, 0)
  outfilter.set_input_port(0, decimationfilter, 0)
  outfilter.process(input.shape[1])
  return output

def filter_4(input):
  import numpy as np
  output = np.zeros(input.shape, dtype=np.float64)

  inputfilter = DoubleInPointerFilter(input, False)
  inputfilter.set_input_sampling_rate(sample_rate)
  overfilter = DoubleOversampling6points5order_4Filter()
  overfilter.set_input_sampling_rate(sample_rate)
  overfilter.set_output_sampling_rate(sample_rate * 4)
  overfilter.set_input_port(0, inputfilter, 0)
  overdrivefilter = DoubleSD1OverdriveFilter()
  overdrivefilter.set_input_sampling_rate(sample_rate * 4)
  overdrivefilter.set_input_port(0, overfilter, 0)
  overdrivefilter.set_drive(0.9)
  lowpassfilter = DoubleButterworthLowPassFilter()
  lowpassfilter.set_input_sampling_rate(sample_rate * 4)
  lowpassfilter.set_cut_frequency(sample_rate)
  lowpassfilter.set_order(5)
  lowpassfilter.set_input_port(0, overdrivefilter, 0)
  decimationfilter = DoubleDecimationFilter(1)
  decimationfilter.set_input_sampling_rate(sample_rate * 4)
  decimationfilter.set_output_sampling_rate(sample_rate)
  decimationfilter.set_input_port(0, lowpassfilter, 0)
  #tonefilter = DoubleSD1ToneFilter()
  #tonefilter.set_input_sampling_rate(sample_rate)
  #tonefilter.set_input_port(0, decimationfilter, 0)
  #tonefilter.set_tone(1)
  #highpassfilter = DoubleChamberlinFilter()
  #highpassfilter.set_input_sampling_rate(sample_rate)
  #highpassfilter.set_input_port(0, tonefilter, 0)
  #highpassfilter.select(2)
  #highpassfilter.set_attenuation(1)
  #highpassfilter.set_cut_frequency(20)
  outfilter = DoubleOutPointerFilter(output, False)
  outfilter.set_input_sampling_rate(sample_rate)
  #outfilter.set_input_port(0, highpassfilter, 0)
  outfilter.set_input_port(0, decimationfilter, 0)
  outfilter.process(input.shape[1])
  return output

if __name__ == "__main__":
  import numpy as np
  size = 1200
  
  x = np.arange(size).reshape(1, -1) / 48000.
  d = np.sin(x * 2 * np.pi * 100)
  d.tofile("input.dat")
  out = filter_32(d)
  out.tofile("output32_sd1.dat")
  out = filter_16(d)
  out.tofile("output16_sd1.dat")
  out = filter_8(d)
  out.tofile("output8_sd1.dat")
  out = filter_4(d)
  out.tofile("output4_sd1.dat")

  import matplotlib.pyplot as plt
  plt.plot(x[0], d[0], label="input")
  plt.plot(x[0], out[0], label="output")
  plt.legend()
  plt.show()
