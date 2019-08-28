import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

### Create a file path that determines the location of the 
### csv file/s

IEDF_DATA_PATH = '~/Microthrusters/IEDF/Energyprofile.csv'

### Create a dataframe using pandas, header=label of column
### usecols = tell pandas which column to assign to variable
### repeat for each column in the dataframe
six = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [0])
eight = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [1])
ten = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [2])
twenty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [3])
fourty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [4])
fifty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [5])

### Convert pandas dataframe to numpr array (because pythn is fussy!)
### specify the dimension to extract, or rather, the level of depth of
### dimension, you may have many stacked on top of one another

six_x = np.array(six)[0::]
eight_x = np.array(eight)[0::]
ten_x = np.array(ten)[0::]
twenty_x = np.array(twenty)[0::]
fourty_x = np.array(fourty)[0::]
fifty_x = np.array(fifty)[0::]

### Make a list of x values corresponding to mean energy
### Make a list of y values corresponding to modal energy

mean_values_x = [0,42,41.5,42,47,50,41]
mean_values_y = [0,33,66,99,132,165,198]

mode_values_x = [0,0,0,0,9,12,12]
mode_values_y = [0,33,66,99,132,165,198]

### Plotting regime for the mean and modal energy, requires a list
### The formatting is optional

plt.plot(mean_values_x,mean_values_y,marker='2',color='k',linestyle='--')
plt.plot(mode_values_x,mode_values_y, marker='o',color='w',linestyle='--')

### Create a list of lists ###
### Image_x is a list which itself contains 2D arrays

Image_x = [six_x,eight_x,ten_x,twenty_x,fourty_x,fifty_x]

### Not 100% sure on this step but was unable to plot without using
### the stack function, essentially joins the arrays togther along
### a specified axis, this case the first dimension

Image_x = np.stack(Image_x, axis=0)

### imshow plots an image from a 2D array, which is Image_x in this case
### refer to online documentation for formatting options, see link below 
### https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html

plt.imshow(Image_x.squeeze(),extent = [0,250,0,200],vmin=0,vmax=0.01, interpolation='bilinear',
           cmap='plasma')
plt.colorbar()
plt.show


