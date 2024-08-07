import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pylab as pl
#from IPython import display
import time as ttime
import random
from mpl_toolkits.mplot3d import Axes3D
# with a signal

# Num of phase points
N=32
# simulation parameters
srate = 1000;
time  = np.arange(-1.,1.,1./srate)

def gen_signal(phase_point):    
    # phase of signal
    signal_freq = 5
    theta = 2*np.pi*phase_point/N;    
    # signal
    sinew  = np.sin(2*np.pi*signal_freq*time + theta)
    gauss  = np.exp( (-time**2) / .1);
    signal = np.multiply(sinew,gauss)
    return signal

# plot signal
fig, axs = plt.subplots(3,1)

dot_prod = np.zeros(N+1)
sine_freq = 5

# create complex sine wave
csw = np.exp( 1j*2*np.pi*sine_freq*time )
rsw = np.sin(    2*np.pi*sine_freq*time )

def animate(i):
    axs[0].cla()
    axs[1].cla()
    axs[2].cla()
    signal = gen_signal(i)
    axs[0].grid(True)
    axs[0].plot(time, signal)
    dot_prod[i] = np.abs(np.vdot( csw,signal ))
    # compute complex dot product
    cdp = np.sum( np.multiply(signal,csw) ) / len(time)
    rdp = sum( np.multiply(signal,rsw) ) / len(time)
    
    limit = 0.2
    axs[1].set_ylim(-limit, limit)
    axs[1].set_xlim(-limit, limit)
    axs[1].set_xlabel('Real')
    axs[1].set_ylabel('Img')
    axs[1].grid(True)
    axs[1].set_aspect('equal', adjustable='box')
    axs[1].plot(np.imag(cdp),np.real(cdp),'ro')
    
    axs[2].set_ylim(-limit, limit)
    axs[2].set_xlim(-limit, limit)
    axs[2].set_xlabel('Real')
    axs[2].set_ylabel('Img')
    axs[2].grid(True)
    axs[2].set_aspect('equal', adjustable='box')
    axs[2].plot(rdp,0,'ro')
    
ani = animation.FuncAnimation(fig, animate, frames=range(0,N+1,1), interval=100, repeat=False)
plt.show()
