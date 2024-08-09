import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 16  # Number of samples
time = np.arange(0, N)  # Time vector (0 to N-1)
time1 = np.arange(0, N, 0.05)  # Time vector (0 to N-1)

# Cosine waves
cos0 = np.cos(2 * np.pi * 1 * time1 / N)  # Cosine with frequency 1/N
cos1 = np.cos(2 * np.pi * 15 * time1 / 16)  # Cosine with frequency 15/N
cos2 = np.cos(2 * np.pi * 15 * time / 16)  # Cosine with frequency 15/N

# Plotting the cosine waves
plt.figure(figsize=(10, 6))
plt.plot(time1, cos0, label='cos(2π * 1 * t / N)', linestyle='-')
plt.plot(time1, cos1, label='cos(2π * 15 * t / N)', linestyle='-')
plt.plot(time, cos2,  'ro', label='cos(2π * 15 * t / 16)')

# Adding titles and labels
plt.title('Comparison of Two Cosine Waves')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
