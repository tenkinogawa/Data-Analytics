import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

stan_data = {
    "N":12,
    "y":[0,1,0,1,0,0,0,1,0,1,0,1]
}

model10 = CmdStanModel(stan_file='code_10.stan')
sample = model10.sample(stan_data)