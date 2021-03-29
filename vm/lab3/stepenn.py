import matplotlib.pyplot as plt
import numpy as np
from parsers import *
from scipy.io.wavfile import write

data = pars()

ROW = 2


for i in range(1, len(data)-1):
    if not data[i][ROW] == 999.9:
        dat.append(data[i][ROW])
        xs.append(data[i][0])

signal = np.array(dat)
signal += 13
signal *= 2500

FD = 200

spectrum = np.fft.rfft(signal)

new_spec = [0 for _ in range(import matplotlib.pyplot as plt
import numpy as np
from parsers import *
from scipy.io.wavfile import write

data = pars()

ROW = 2


for i in range(1, len(data)-1):
    if not data[i][ROW] == 999.9:
        dat.append(data[i][ROW])
        xs.append(data[i][0])

signal = np.array(dat)
signal += 13
signal *= 2500

FD = 200

spectrum = np.fft.rfft(signal)

new_spec = [0 for _ in range(500)]
for i in np.abs(spectrum):
    new_spec.append(i)

signal = np.fft.irfft(new_spec)
signal *= 10

for i in range(len(signal)):
    if abs(signal[i]) > 20000:
        signal[i] *= 20000 /signal[i]
spectrum = np.fft.rfft(signal)


write("example.wav", FD, signal.astype(np.int16))

plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(np.fft.rfftfreq(len(signal), d=1./FD), np.abs(spectrum))
plt.show()