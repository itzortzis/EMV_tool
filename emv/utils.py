import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt


# Compute_ci:
# -----------
# Computes the 95% confidence interval for the given
# numpy array containing the experimental data
#
# -> mtrcs: The numpy array with the experimental data
# -> args: dictionary with the tweaking parameters
# <- low: vector containing the lowest values
# <- med: vector containing the median values
# <- high: vector containing the highest values

def compute_ci(metrics, args):
  TPS  = args["num_of_timepoints"]
  low  = np.zeros((TPS))
  high = np.zeros((TPS))
  med  = np.zeros((TPS))

  for indx in range(TPS):
    m  = metrics[indx, :, args["metric_id"]]

    data = m
    temp = st.t.interval(confidence=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data))
    low[indx]  = temp[0]
    high[indx] = temp[1]
    med[indx]  = (temp[0] + temp[1])/2

  return low, med, high


# Plot_metrics_ci:
# ----------------
# Plots the 95% confidence interval of the experimental data
#
# -> ci_elems: vectors of the lowest, median and highest values
# <- args: configuration parameters for the figure

def plot_metrics_ci(ci_elems, TPS, args):
  low  = ci_elems[0]
  med  = ci_elems[1]
  high = ci_elems[2]
  x = np.arange(TPS)+1

  fig, ax = plt.subplots()
  fig.set_size_inches(7, 5)
  line, = ax.plot(x, med, color = args["med_color"])
  ax.fill_between(x, low, high, color = args["var_color"], alpha=.1)
  ax.set_ylim([args["y_min"], args["ymax"]])
  plt.xlabel(args["xlabel"], fontsize = args["font_size"])
  plt.ylabel(args["ylabel"], fontsize = args["font_size"])
  plt.grid()
  plt.show()


# Bar_metrics_ci:
# ----------------
# Presents the 95% confidence interval of the experimental data
# using bar plots.
#
# -> ci_elems: vectors of the lowest, median and highest values
# <- args: configuration parameters for the figure

def bar_metrics_ci(ci_elems, TPS, args):
  low  = ci_elems[0]
  med  = ci_elems[1]
  high = ci_elems[2]
  x = np.arange(TPS)+1
  width = 0.35
  fig, ax = plt.subplots()
  fig.set_size_inches(7, 5)
  line = ax.bar(x, med, width, yerr = high-med)
  #ax.fill_between(x, low, high, color = args["var_color"], alpha=.1)
  plt.xlabel(args["xlabel"], fontsize = args["font_size"])
  plt.ylabel(args["ylabel"], fontsize = args["font_size"])
  plt.grid()
  plt.show()
