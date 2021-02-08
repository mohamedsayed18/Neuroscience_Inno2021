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


if __name__ == "__main__":

    sim_time = 120
    
    # the first model at v1 =0
    model1 = morris_lecar()
    model1.v4 = 13
    model1.v3 = -10
    model1.v1 = 0   
    # get the output for 2000 step
    for i in range(sim_time):
        model1.get_v(i)

#    v_b1 = model1.volts.copy()
#    model1.reset()
    # second model
    model2 = morris_lecar()
    model2.v4 = 13
    model2.v3 = -10
    model2.v1 = -20

    for i in range(sim_time):
        model2.get_v(i)
    
    #v_b2 = model1.volts


    # Third model
    model3 = morris_lecar()
    model3.v4 = 13
    model3.v3 = -10
    model3.v1 = -200

    for i in range(sim_time):
        model3.get_v(i)


    time = [i for i in range(sim_time)]
    plt.plot(time, model1.volts, label="beta =0")
    plt.plot(time, model2.volts, label="beta =-20")
    plt.plot(time, model3.volts, label="beta =-200")
    plt.xlabel("time")
    plt.ylabel("Volt")
    plt.legend()
    plt.show()
