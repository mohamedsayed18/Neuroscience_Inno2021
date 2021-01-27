"""
Drawing a regime map
let V4 = 13mv(gamma-w)
let V3 = -10mv(Betta-w)

Betta_m = V1


TODO:
Bifurcations in the(Istim,βm)-plane (betta_m is v1)
change the idea of global v
"""
import matplotlib.pyplot as plt

from morris_lecar import morris_lecar

def simulate(steps):
    volty = []
    for i in range(steps):
        volty.append(model1.get_v(i))
    

if __name__ == "__main__":

    sim_time = 120
    model1 = morris_lecar()
    model1.v4 = 13
    model1.v3 = -10
    model1.v1 = 0   

    # get the output for 2000 step
    for i in range(sim_time):
        model1.get_v(i)

    v_b1 = model1.volts.copy()
    model1.reset()

    model1.v4 = 13
    model1.v3 = -10
    model1.v1 = -20

    for i in range(sim_time):
        model1.get_v(i)
    
    v_b2 = model1.volts


    # Third model
    model3 = morris_lecar()
    model3.v4 = 13
    model3.v3 = -10
    model3.v1 = -200

    for i in range(sim_time):
        model3.get_v(i)


    time = [i for i in range(sim_time)]
    plt.plot(time, v_b1)
    plt.plot(time, v_b2)
    plt.plot(time, model3.volts)
    plt.show()
