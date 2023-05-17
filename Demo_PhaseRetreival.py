# Loads a wav file, extracts the envelope, and reconstructs the phase
# Audio from (https://www.videvo.net/royalty-free-music-track/the-flight-of-the-bumble-bee-60s/231158/)

# Baseband -> Baseband -> Phase recovery of BB signal

import scipy
import numpy as np
import matplotlib.pyplot as plt

import wave
filename = './Rimsky-Korsakov-The-Flight-of-the-Bumble-Bee-CLA014201.wav'
# Open the .wav file
with wave.open(filename, 'rb') as audio_file:
    # Get the audio file parameters
    sample_width = audio_file.getsampwidth()
    num_channels = audio_file.getnchannels()
    sample_rate = audio_file.getframerate()
    num_frames = audio_file.getnframes()

    # Read all frames from the audio file
    audio_data = audio_file.readframes(num_frames)

original_signal = np.frombuffer(audio_data, dtype=np.int16)    

# truncate beginning and end (silence/zeros = bad for log function) + reducing the data size
original_signal = original_signal[int(len(original_signal)/4):int(len(original_signal)*3/4)]

import copy
signal = copy.deepcopy(original_signal)
# Adding a bias to prevent zero crossings
dc_bias = 5
signal = 0.0001*signal + dc_bias

def envelopeDetector(signal, sos_LPF):
    signal_rect = [abs(k) for k in signal]
    envelope_estimate = scipy.signal.sosfilt(sos_LPF, signal_rect)
    return envelope_estimate

envelope_estimate = envelopeDetector(signal, sos_LPF=scipy.signal.cheby1(15,40,0.5,'lowpass',output='sos'))

# plt.plot(signal)
# plt.plot(envelope_estimate)
# plt.grid()
# plt.show()

def plotError(sig1,sig2):
    assert len(sig1)==len(sig2)
    error_sig = sig1-sig2
    plt.plot(abs(error_sig))

def dumpWav(signal):
    return None

log_envelope_estimate = np.log(envelope_estimate)
# Hilbert t/f and see if it's a faithful reproduction of the signal
phase_estimate = np.imag(scipy.signal.hilbert(log_envelope_estimate)) # scipy.signal.hilbert actually outputs the analytic complex signal, f_t + j*Hilbert{f_t}

# Reconstructed signal
signal_reconstructed = envelope_estimate*np.cos(phase_estimate)-dc_bias

# Some excursions at the beginning and end of the signal, so we'll clip those..
# m = np.median(signal_reconstructed)
# signal_clipped = np.clip(signal_reconstructed, -1000*m, 1000*m) # primarly targeting the spikes at the beginning and end of the signal
signal_final = np.clip(signal_reconstructed, -0.2, 0.2) # primarly targeting the spikes at the beginning and end of the signal
signal_final = signal_final/max(signal_final)
plt.plot(signal_final)
plt.grid()
plt.show()

scaled_data = np.int16(signal_final*32767)

# Create a new WAV file
with wave.open('output.wav', 'w') as wav_file:
    wav_file.setnchannels(num_channels)  # Mono audio
    wav_file.setsampwidth(sample_width)  # 16-bit audio
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(scaled_data.tobytes())

# ====================================================
# TODO: Baseband -> Upconversion -> Phase recovery of BB signal

# TODO: Demonstrate this for an image? 
# Aside: Can adding a bias be used for compressing an image by discarding the DCT phase?


