"""
Morris lecar model
"""
import numpy as np
import math
import matplotlib.pyplot as plt

class morris_lecar():

   
    def __init__(self):
         #variable
        self.v = -52.14
        self.v1 = 30
        self.v2 = 15
        self.v3 = 0
        self.v4 = 30
        self.v_ca = 100
        self.v_k = -70
        self.v_l = -50
        self.dt = 0.01

        self.I = 0
        self.n = 0.02
        self.dt = 0.1
        self.c = 6.69810502993
        self.phi = 0.025
        self.gl = 0.5
        self.gca = 1.1
        self.gk = 2

        self.volts = []

    def reset(self):
         #variable
        self.v = -52.14
        self.v1 = 30
        self.v2 = 15
        self.v3 = 0
        self.v4 = 30
        self.v_ca = 100
        self.v_k = -70
        self.v_l = -50
        self.dt = 0.1

        self.I = 0
        self.n = 0.02
        self.dt = 0.1
        self.c = 6.69810502993
        self.phi = 0.025
        self.gl = 0.5
        self.gca = 1.1
        self.gk = 2

        self.volts = []
                
    def m_inf(self):
        return (0.5) * (1 + np.tanh( (self.v-self.v1)/self.v2 ))

    def n_ss(self):
        return 0.5 * (1 + np.tanh( (self.v-self.v3)/self.v4 ))

    def t_n(self):
        return 1 / (self.phi * np.cosh((self.v - self.v3) / (2 * self.v4)))

    def dv_dt(self, current):
        self.I = current
        return (self.I - self.gl * (self.v - self.v_l) - self.gca * self.m_inf() * (self.v - self.v_ca)
            - self.gk * self.n * (self.v - self.v_k)) / self.c

    def dn_dt(self):
        return (self.n_ss() - self.n) / self.t_n()

    def get_v(self, current):
        self.volts.append(self.v)
        self.v = self.v + self.dv_dt(current) * self.dt
        self.n = self.n + self.dn_dt() * self.dt
        
if __name__ == "__main__":
    model1 = morris_lecar() # create an instance

    # get the output for 2000 step
    for i in range(2000):
        if(i>450 and i<550):
            model1.get_v(1)
        else:
            model1.get_v(1)

    plt.plot(model1.volts)
    plt.show()
