import random
from collections import Counter
import math

def sample(reps, start, stop):
    count = 0
    data = []
    frequency = Counter()
    while count < reps:
        a = random.randint(start, stop)
        data.append(a)
        count += 1
    
    frq = Counter(data)
    average = sum(data)/reps
    #print(data)
    #print("average = ", average)
    return average

def standard_dev(sample_means):
    pop_mean = sum(sample_means)/len(sample_means)
    r = []
    for mean in sample_means:
        r.append(((mean-pop_mean)**2)**0.5)
    standard_dev = sum(r)/len(sample_means)
    return pop_mean, standard_dev
#print(standard_dev([1,2,3,4,5]))

def trial(samples, reps, start, stop):
    sample_means = []
    for i in range(0, samples):
        sample_means.append(sample(reps, start, stop))
        #print(sample_means)
    sd = standard_dev(sample_means)
    return sample_means, sd

#print(trial(10, 10, 0, 10))
def distribution(samples, reps, start, stop, bins = 10):

    #start must not be equal to stop
    if start == stop:
        print("input error")
        quit()
    if bins == None:
        bins = 10

    #generate a set of means
    t = trial(samples, reps, start, stop)
    sample_means = t[0]

    
    #print(sample_means)
    #print(sample_means)

    #determine intervals to bin data
    bin_upper = {}
    bin_size = (stop - start)/bins

    for i in range(1,bins+1):
        bin_upper[bin_size*i] = []

    #each mean is grouped
    for mean in sample_means:
        #print(mean)
        added = 1
        #begining with the lowest bin, add means to each bin
        for max in bin_upper:
            if mean <= max:
                bin_upper[max].append(added)
                bin_upper[max].sort(reverse=True)
                added = 0
    return bin_upper, t[1]
     
#print(distribution(10, 10, 0, 10, 5))  
def display_dists(samples, reps, start, stop, bins = 10):

    
    d = distribution(samples, reps, start, stop, bins)
    if bins == None:
        print(d[1])
    bin_upper = d[0]
    if bins == None:
        bins = round(d[1][1]*8)
    bin_size = (stop - start)/bins

    labels = []
    for i in range(1,bins+1):
        labels.append(bin_size*i)

    for i in labels:
        print(i, ":", sum(bin_upper[i]))

display_dists(1000, 4, 0, 110) 
