import os
import random
import numpy as np
from matplotlib import pyplot as plt

# Base_function:
# --------------
# Selects among three mathematical functions
# and creates the corresponding numpy array
#
# -> timepoints: numpy array with the timepoints (x-axis)
# -> id: identifier of the preferred math function
# <- numpy array with the y values, output of the selected math function

def base_function(timepoints, id):
  if id < 0 or id > 2:
    print("Wrong math function id input...")

  if id == 0: return np.sqrt(timepoints)
  if id == 1: return np.cos(2*3.14*timepoints)
  if id == 2: return np.log2(timepoints)

  return np.sqrt(timepoints)


# Rand_variation:
# ---------------
# Applies a random variation to the given curve
#
# -> curve: numpy array with the y values of the curve
# -> window: float number that corresponds to the desired variation
# <- curve: numpy array with the v values of the new curve

def rand_variation(curve, window):
  for i in range(len(curve)):
    w = random.uniform(-window, window)
    curve[i] += w

  return curve


# Generate_sample_metrics:
# ------------------------
# Construct the final numpy array containing all the experiments data
# according to the given number of timepoints, iterations and metrics
#
# -> args: dictionary with the number of timepoints, iterations and metrics
# <- mtrcs: The final numpy array with the simulated data

def generate_sample_metrics(args):
  num_of_timepoints = args["num_of_timepoints"]
  num_of_iters      = args["num_of_iterations"]
  num_of_metrics    = args["num_of_metrics"]

  mtrcs = np.zeros((num_of_timepoints, num_of_iters, num_of_metrics))
  timepoints = np.arange(num_of_timepoints) + 1

  for m in range(num_of_metrics):
    for i in range(num_of_iters):
      curve = base_function(timepoints, m)
      curve = rand_variation(curve, args["window"])
      mtrcs[:, i, m] = curve

  return mtrcs
