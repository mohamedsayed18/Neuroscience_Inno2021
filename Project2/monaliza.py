"""
Analysing the EEG data for seeing monaliza

Todo:
* Reading .dat file done
"""
import numpy as np
import os
from scipy import signal
from scipy import stats
import matplotlib.pyplot as plt

# Read data
all_participants = []
person_data = []
alphas = []
all_alphas = []

alpha_cut = [8, 12]
beta_cut = [15, 30]


for folder in os.listdir("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"):
    
    if folder.startswith("Participant"):
        #print(folder)
        for filename in os.listdir("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"+folder+"/Figs_for_spectra/"):
            signals = np.loadtxt("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"+folder+"/Figs_for_spectra/"+filename)
            person_data.append(signals)
            
            #print(len(person_data))

        all_participants.append(person_data)
        person_data = []

all_people = np.array(all_participants)

#print(all_people.shape)
#print(all_people[0,0].shape)

for person in all_people:
    #print("new person", person.shape)
    for intensity in person.T:
        #print("el raw", intensity.shape)
        coff = signal.firwin(intensity.shape[0], beta_cut, pass_zero=False, fs=250)
        new_values = np.zeros_like(intensity)
        #print(new_values.shape, intensity.shape)
        for i in range(intensity.shape[1]):
            
            new_values[:,i] = np.convolve(intensity[:,i], coff, 'same')
        
        alpha_values = []
        for i in range(new_values.shape[1]-1):
            for j in range(i+1, new_values.shape[1]):
                p_coff, _ = stats.pearsonr(new_values[:,i], new_values[:,j])
                alpha_values.append(p_coff)

        alphas.append(np.average(alpha_values))
    all_alphas.append(alphas)
    alphas = []
    #print(len(all_alphas[-1])) 
    #break

#print(len(all_alphas))

np.save("mydata", all_alphas)
inten = np.linspace(0.1,1, 10)

for i in all_alphas:
    plt.plot(inten, i)

plt.xlabel("intensity")
plt.ylabel("alpha")
plt.show()

