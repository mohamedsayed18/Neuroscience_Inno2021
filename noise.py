"""
Add Gaussian white noise
TODO: 
Try the different D values(amplitude) for noise(1, 0.1, 0.01, 0.001)
"""
import numpy as np
import matplotlib.pyplot as plt

from morris_lecar import morris_lecar

class noisy_model(morris_lecar):
    def dv_dt(self, current):
        self.I = current
        return ((self.I - self.gl * (self.v - self.v_l) - self.gca * self.m_inf() * (self.v - self.v_ca)
            - self.gk * self.n * (self.v - self.v_k)) / self.c) + np.random.normal(0.001,1)


if __name__ == "__main__":
    mymodel = noisy_model() # create an instance

    # get the output for 2000 step
    for i in range(2000):
        if(i>450 and i<550):
            mymodel.get_v(1)
        else:
            mymodel.get_v(1)

    plt.plot(mymodel.volts)
    plt.show()