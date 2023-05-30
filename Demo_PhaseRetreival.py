import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

SAMPLE_RATE=1#1e9 # 1 GHz sample rate for the overall simulation
FREQ_CARRIER = 0.25#250e6

assert SAMPLE_RATE > 2*FREQ_CARRIER

SPS = 8 # Note that this already fixes the symbol rate as sym_rate = sample_rate/sym_per_sample

num_symbols = 10

input_words = np.random.randint(0, 4, num_symbols) # An already-bitpacked source
# input_words = [1]

constellation_map = {
    0:1+1j,
    1:-1+1j,
    2:-1-1j,
    3:1-1j
}

complex_data = [constellation_map[w] for w in input_words]

# Now we prepare the input to the RRC filter: For every input sample pad SPS-1 zeros.
# Add suitable zero padding
x_I = np.zeros([SPS*num_symbols])
x_Q = np.zeros([SPS*num_symbols])
for k in range(len(complex_data)):
    x_I[k*SPS] = np.real(complex_data[k])
    x_Q[k*SPS] = np.imag(complex_data[k])

# RRC filter
num_taps = 101 # ie length of this FIR filter, should be ODD
beta = 0.35 # excess bandwidth relative to a brick wall function
Ts = SPS*(1/SAMPLE_RATE)
t = np.arange(num_taps) - (num_taps-1)//2 # interval from -num_taps to +num_taps
rrc_wave = 1/Ts*np.sinc(t/Ts) * np.cos(np.pi*beta*t/Ts) / (1 - (2*beta*t/Ts)**2)

# Pulse shaping
bb_tx_I = np.convolve(x_I, rrc_wave)
bb_tx_Q = np.convolve(x_Q, rrc_wave)

# Polar plot of the complex baseband

import animate
animate.animateXY(bb_tx_I,bb_tx_Q,interval = 10)

# # Upconversion
# carrier_freq = np.pi/4 #