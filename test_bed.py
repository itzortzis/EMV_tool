import utils.sample_data_utils as sdu
import utils.utils as utils


# Simulation configuration
gen_args = {
  "num_of_timepoints": 100, # The number of experiment x-axis points
  "num_of_iterations": 20,  # The number of experiment repetitions
  "num_of_metrics": 3,      # The number of experiment metrics
  "metric_id": 1,           # Metric id for the sample metrics
  "window": 0.8             # Variation number
}

# Figure configuration
fig_args = {
  "med_color": '#fb8500',
  "var_color": '#fb8500',
  "xlabel": 'Time Points',
  "ylabel": 'Metric Name',
  "font_size": 14
}

metrics = sdu.generate_sample_metrics(gen_args)
ci_elems = utils.compute_ci(metrics, gen_args)
utils.plot_metrics_ci(ci_elems, gen_args["num_of_timepoints"], fig_args)
