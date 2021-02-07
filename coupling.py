# Task 4: testing model with coupling connected neurons
# TODO Add the noise

import matplotlib.pyplot as plt
import numpy as np

from morris_lecar import morris_lecar

class coupled_neurons(morris_lecar):

    def __init__(self):
        self.g_syn = 4
        self. D = 0.1
        self.index = 0
        super().__init__()
        

    def I_syn(self,neurons):
        if(self.index == len(neurons)-1):
            #Isyn = self.g_syn * (self.v - 0) # TODO remove the Isyn totally for the last neuron
            return 0
        else:
            Isyn = self.g_syn * (self.v - neurons[self.index+1].v)
        return Isyn

    def dv_dt(self, neurons):
        return ((self.I - self.gl * (self.v - self.v_l) - self.gca * self.m_inf() * (self.v - self.v_ca)
            - self.gk * self.n * (self.v - self.v_k)- self.I_syn(neurons)) / self.c) + (self.D * np.random.normal(0,1))

    def get_v(self, neurons):
        self.volts.append(self.v)
        self.v = self.v + self.dv_dt(neurons) * self.dt
        self.n = self.n + self.dn_dt() * self.dt

if __name__ == "__main__":
    no_neurons = 2
    neurons = []

    # Create a list of neurons
    for i in range(no_neurons):
        neurons.append(coupled_neurons())
        neurons[i].index = i

    # change initial v
    #neurons[1].v = -52

    for _ in range(1000):
        for i in range(no_neurons):
            neurons[i].get_v(neurons)

    neurons[0].volts

    plt.plot(neurons[0].volts)
    plt.plot(neurons[1].volts)
    plt.show()



