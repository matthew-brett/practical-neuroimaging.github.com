# The output is N + M - 1 long
n_output = n_time_points_3 + n_hrf_points - 1
output = np.zeros(n_output)
for i in range(n_time_points_3):
    neural_value = neural_signal_3[i]
    scaled_irf = neural_value * hrf_signal
    output[i:i+n_hrf_points] = output[i:i+n_hrf_points] + scaled_irf
corresponding_times = np.arange(n_output) * 0.1
plt.plot(corresponding_times, output)