import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os
import arviz as az

F = len('Agnieszka')
L = len('Welian')

stan_data = {
    "N":F
}

model7 = CmdStanModel(stan_file='code_7.stan')
model8 = CmdStanModel(stan_file='code_8.stan')
model9 = CmdStanModel(stan_file='code_9.stan')
sample7 = model7.sample(stan_data)
sample8 = model8.sample(stan_data)
sample9 = model9.sample(stan_data)

az.plot_density([sample7,sample8,sample9])
plt.show()
