import wave
import numpy as np
import matplotlib.pyplot as plt
  
f = wave.open(r"EC516_voice.wav","rb")
params = f.getparams()
[nchannels, sampwidth, framerate, nframes] = params[:4]
str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data,dtype = np.short)
wave_data.shape = -1,2
wave_data = wave_data.T
time=np.arange(0,nframes/2)/framerate
# print(params)
plt.figure(1)
plt.subplot(211)
plt.plot(time,wave_data[0])
plt.xlabel("time/s")
plt.title('Wave')
  
  
N=40000
start=0

df = framerate/(N-1)

freq = [df*n for n in range(0,N)]

wave_data2=wave_data[0][start:start+N]
c=np.fft.fft(wave_data2)*2/N

plt.subplot(212)
plt.plot(freq[:round(len(freq)/2)],abs(c[:round(len(c)/2)]),'r')
plt.title('Freq')
plt.xlabel("Freq/Hz")
plt.show()
