#!/usr/bin/env python

from ATK.Core import DoubleInPointerFilter, DoubleOutPointerFilter
from ATK.Dynamic import DoubleGainCompressorFilter
from ATK.Tools import DoubleApplyGainFilter

import matplotlib.pyplot as plt

sample_rate = 96000

def filter(input, slope=4, threshold=1, softness=1):
  import numpy as np
  output = np.zeros(input.shape, dtype=np.float64)

  infilter = DoubleInPointerFilter(input, False)
  infilter.set_input_sampling_rate(sample_rate)

  gainfilter = DoubleGainCompressorFilter(1)
  gainfilter.set_input_sampling_rate(sample_rate)
  gainfilter.set_input_port(0, infilter, 0)
  gainfilter.set_threshold(threshold)
  gainfilter.set_slope(slope)
  gainfilter.set_softness(softness)

  applygainfilter = DoubleApplyGainFilter(1)
  applygainfilter.set_input_sampling_rate(sample_rate)
  applygainfilter.set_input_port(0, gainfilter, 0)
  applygainfilter.set_input_port(1, infilter, 0)

  outfilter = DoubleOutPointerFilter(output, False)
  outfilter.set_input_sampling_rate(sample_rate)
  outfilter.set_input_port(0, applygainfilter, 0)
  outfilter.process(input.shape[1])

  return output

if __name__ == "__main__":
  import numpy as np
  size = 1000

  x = np.arange(size, dtype=np.float64).reshape(1, -1) / 100

  np.savetxt("input.txt", x)
  out_2_1_1 = filter(x, 2, 1, 1)
  out_4_1_1 = filter(x, 4, 1, 1)
  out_8_1_1 = filter(x, 8, 1, 1)
  out_10_01_001 = filter(x, 10, .1, 0.01)
  out_10_01_1 = filter(x, 10, .1, 1)
  out_10_01_10 = filter(x, 10, .1, 10)
  plt.figure()
  plt.loglog(x[0], out_2_1_1[0], label="slope(2), threshold(1), softness(1)")
  plt.loglog(x[0], out_4_1_1[0], label="slope(4), threshold(1), softness(1)")
  plt.loglog(x[0], out_8_1_1[0], label="slope(8), threshold(1), softness(1)")
  plt.loglog(x[0], out_10_01_001[0], label="slope(10), threshold(0.1), softness(1e-2)")
  plt.loglog(x[0], out_10_01_1[0], label="slope(10), threshold(0.1), softness(1)")
  plt.loglog(x[0], out_10_01_10[0], label="slope(10), threshold(0.1), softness(10)")
  plt.title("Compressor gain")
  plt.legend(loc=4)
  plt.grid()
  plt.show()
