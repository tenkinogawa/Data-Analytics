import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}

model2 = CmdStanModel(stan_file='code_2.stan')
model3 = CmdStanModel(stan_file='code_3.stan')
sample = model2.sample(stan_data)
sample = model3.sample(stan_data)