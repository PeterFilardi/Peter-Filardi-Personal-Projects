"""
Peter Filardi
Demonstration of central limit theorem
"""

import random
import matplotlib.pyplot as plt


def sample(reps, start, stop):
    """Take a sample from a uniform random distribution.
    reps: (int) sample size
    start: (int) lower bound of sample space
    stop: (int) upper bound of sample space

    Returns the sample mean as a float.
    """
    count = 0
    data = []
    # create a list of randomly sampled integers
    while count < reps:
        uniform_int = random.randint(start, stop)
        data.append(uniform_int)
        count += 1
    
    # calculate sample mean
    average = sum(data)/reps
 
    return average

def standard_dev(sample_means):
    """Calculate the standard deviation of sample means.
    sample_means: (list) list of sample means
    
    Returns the standard deviation of sample means."""

    # average value of a mean
    mean_of_means = sum(sample_means)/len(sample_means)

    delta = []
    for mean in sample_means:
        # absolute distance between each sample mean and the average of sample means
        delta.append(((mean-mean_of_means)**2)**0.5)

    # find the average distance
    standard_dev = sum(delta)/len(sample_means)
    
    return standard_dev

def trial(samples, reps, start, stop):
    """Takes many samples from a uniform random distribution. Plots sample means.
    samples: (int) number of samples to be taken
    reps: (int) sample size
    start: (int) lower bound of sample space
    stop: (int) upper bound of sample space

    Returns a histogram of sample means."""

    sample_means = []
    for i in range(0, samples):

        # call the sample function 
        sample_means.append(sample(reps, start, stop))

    # note the mean of sample means 
    mean_of_means = sum(sample_means)/len(sample_means)

    # call the standard dev function
    sd = standard_dev(sample_means)
    
    # use standard deviation to standardize histogram bins
    bins = round((stop-start)/sd, None)
    
    # test code
    # print(f"sd = {sd} bins = {bins}")

    # plot
    plt.hist(sample_means, bins = bins)

     # estimate max height of histogram
    ymax = 2.8*(samples/bins)

    # add line for mean_of_means
    plt.vlines(mean_of_means, 0, ymax, color='red', linestyle='dashed', label='Population Mean')

    plt.show()
    return sample_means, sd

# 1000 samples, sample of size 100, selected randomly from 0-100
trial(10000, 100, 0, 100)