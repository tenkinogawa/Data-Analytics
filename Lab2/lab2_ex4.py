import cmdstanpy
import numpy as np
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

F = len('Agnieszka')
L = len('Welian')

stan_data = {
    "y_guess":[1],
    "theta":[(F+L)/2]
}

model6 = CmdStanModel(stan_file='code_6.stan')
tunes = model6.sample(data = stan_data, fixed_param=True, iter_sampling=1, iter_warmup=0)
tunes.draws_pd()
ex = tunes.stan_variable('y')
print("Standard deviation = ", np.exp(ex))
# don't know how to access the sigma to make it printed