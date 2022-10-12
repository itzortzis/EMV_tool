# EMV_tool

EMV stands for "Experimental Metrics Visualization".
EMV_tool is a simple tool for visualizing the metrics of a repetitive experiment.
It is a living repository and new commits will appear when new updates occur.

All the experimental iterations should be placed in a single numpy array with the following structure. The height of this array represents the several repetitions of the experiment; each row corresponds to a single repetition, the width represents the time points (x-axis) of the experiment, while the depth depicts the different metrics used for the evaluation of the experiment.

## Sample input numpy array:

Shape: (100, 10, 3) -> The experiment has 100 timepoints, it has been conducted 10 times and 3 metrics were used for the evaluation.


## Configuration parameters:

### General parameters:
- med_color: color of the line that corresponds to median value
- var_color: color of the deviation area around median
- xlabel: label for x-axis
- ylabel: label for y-axis
- font-size: font size for labels of the figure
```
fig_args = {
  "med_color": '#219ebc',
  "var_color": '#219ebc',
  "xlabel": 'Time Points',
  "ylabel": 'Metric Name',
  "font_size": 14
}
```
### Simulation parameters:
- num_of_timepoints: The number of experiment x-axis points
- num_of_iterations: The number of experiment repetitions
- num_of_metrics: The number of experiment metrics
- metric_id: Metric id for the sample metrics
- window: Variation number
```
gen_args = {
  "num_of_timepoints": 100, 
  "num_of_iterations": 20,  
  "num_of_metrics": 3,      
  "metric_id": 2,           
  "window": 0.8 
}
```

## Sample outputs

![metric_1](https://user-images.githubusercontent.com/105294556/195347274-709cc796-3864-4958-89ee-8035b4e122c9.png)
![metric_2](https://user-images.githubusercontent.com/105294556/195347306-3d56b0db-4e7f-4c87-8108-c5fe921b15a2.png)
