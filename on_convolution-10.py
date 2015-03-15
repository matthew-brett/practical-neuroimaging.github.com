default_convolved = np.convolve(neural_signal_3, hrf_signal)
assert len(default_convolved) == n_time_points_3 + n_hrf_points - 1
assert len(default_convolved) == len(neural_signal_3) + len(hrf_signal) - 1