bold_signal = np.convolve(neural_signal, hrf_signal)[:n_time_points]
plt.plot(times, bold_signal)
plt.xlabel('time (seconds)')
plt.ylabel('bold signal')
plt.title('Output BOLD signal predicted by convolution')