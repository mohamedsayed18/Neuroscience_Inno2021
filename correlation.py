"""
characteristic correlation time
"""

import matplotlib.pyplot as plt
import numpy as np

from coupling import coupled_neurons

def corr(data, shift=3):
    d1 = data[3:]
    d2 = data[:-3]
    return np.correlate(d1, d2)


if __name__ == "__main__":

    # Get all the values to plot
    """
    1. initate all the 25 instances and set their noise
    2. calculate the value 
    3. calculate the correllation for each neuron
    """
    no_neurons = 25  # define the number of neurons
    corr_time = []
    
    # Calculate auto correlation at each D(noise) value
    noise_values = np.linspace(0.01,1,100)
    for noise in noise_values:
        # Create a list of neurons
        neurons = []
        for i in range(no_neurons):
            neurons.append(coupled_neurons())
            neurons[i].index = i
            neurons[i].D = noise

        # Calculate the volts
        for _ in range(1000):
            for i in range(no_neurons):
                neurons[i].get_v(neurons)

        #Calculate the correllation time 
        Auto_co = []
        for i in range(no_neurons):
            Auto_co.append(corr(neurons[i].volts))

        # calculate the time
        corr_time.append(np.sum(np.square(Auto_co)))

plt.plot(noise_values, corr_time)
plt.xlabel("D (noise)")
plt.ylabel("Correlation")
plt.show()
        

    
        


