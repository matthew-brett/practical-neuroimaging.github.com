times_3 = np.arange(0, 50, 0.1)
n_time_points_3 = len(times_3)
neural_signal_3 = np.zeros(n_time_points_3)
i_time_4 = np.where(times_3 == 4)[0]  # index of value 4 in "times_3"
i_time_10 = np.where(times_3 == 10)[0]  # index of value 10 in "times_3"
i_time_30 = np.where(times_3 == 30)[0]  # index of value 30 in "times_3"
neural_signal_3[i_time_4] = 1  # A single spike at time == 4
neural_signal_3[i_time_10] = 1  # A single spike at time == 10
neural_signal_3[i_time_30] = 1  # A single spike at time == 30
plt.plot(times_3, neural_signal_3)
plt.xlabel('time (seconds)')
plt.ylabel('neural signal')
plt.ylim(0, 1.2)
plt.title('Neural model for very brief events at times 4, 10, 30')