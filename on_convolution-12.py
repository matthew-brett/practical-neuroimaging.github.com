neural_signal_5s = np.zeros(n_time_points)
neural_signal_5s[(times >= 4) & (times < 9)] = 1
bold_signal_5s = np.convolve(neural_signal_5s, hrf_signal)[:n_time_points]
neural_signal_impulse = np.zeros(n_time_points)
neural_signal_impulse[(times == 4)] = 1
bold_signal_impulse = np.convolve(neural_signal_impulse, hrf_signal)[:n_time_points]
plt.plot(times, bold_signal_5s, label='5 second event signal')
plt.plot(times, bold_signal_impulse, label='impulse event signal')
plt.xlabel('time (seconds)')
plt.ylabel('bold signal')
plt.title('Output BOLD signal for event 5 seconds long')
plt.legend()