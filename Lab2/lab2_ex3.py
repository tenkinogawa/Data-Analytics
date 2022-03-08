import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}

model4 = CmdStanModel(stan_file='code_4.stan')
model5 = CmdStanModel(stan_file='code_5.stan')
sample = model4.sample(stan_data)
sample = model5.sample(stan_data)