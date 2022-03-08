import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}

model7 = CmdStanModel(stan_file='code_7.stan')
model8 = CmdStanModel(stan_file='code_8.stan')
model9 = CmdStanModel(stan_file='code_9.stan')
sample = model7.sample(stan_data)
sample = model8.sample(stan_data)
sample = model9.sample(stan_data)