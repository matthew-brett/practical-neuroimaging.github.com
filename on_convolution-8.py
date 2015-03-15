neural_signal_3[i_time_10] = 2  # A bigger spike at time == 10
plt.plot(times_3, neural_signal_3)
plt.xlabel('time (seconds)')
plt.ylabel('neural signal')
plt.ylim(0, 2.2)
plt.title('Neural model for larger event at 10 seconds')