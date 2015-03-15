bold_signal_3 = np.convolve(neural_signal_3, hrf_signal)[:n_time_points_3]
plt.plot(times_3, bold_signal_3)
plt.xlabel('time (seconds)')
plt.ylabel('bold signal')
plt.title('Output BOLD signal for larger event at 10 seconds')