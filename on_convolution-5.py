n_hrf_points = len(hrf_signal)
bold_more_simple = np.zeros(n_time_points)
bold_more_simple[i_time_4:i_time_4 + n_hrf_points] = hrf_signal
assert np.all(bold_more_simple == bold_signal)