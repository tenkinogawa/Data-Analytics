import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import scipy.stats as stats

F = len('Agnieszka')
L = len('Welian')

model4 = CmdStanModel(stan_file='code_4.stan')
sample4 = model4.sample(output_dir='samples')
sample4.diagnose()

N=1000
x4 = np.linspace(0,8,N)
probability_density_fun4 = stats.gamma.pdf(x4, 1.25, scale = 1 / 1.25)
plt.plot(x4, probability_density_fun4, linewidth=1)

plt.gca().set_xlabel("theta")
plt.gca().set_ylabel("Probability Density Function")


model5 = CmdStanModel(stan_file='code_5.stan')
sample5 = model5.sample(output_dir='samples')
sample5.diagnose()

N=1000
x5 = np.linspace(0,8,N)
probability_density_fun5 = stats.gamma.pdf(x5, 1.25, scale = 1 / 1.25)
plt.plot(x5, probability_density_fun5, linewidth=2)

plt.gca().set_xlabel("theta")
plt.gca().set_ylabel("Probability Density Function")
plt.show()
