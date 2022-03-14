import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import scipy.stats as stats

F = len('Agnieszka')
L = len('Welian')

stan_data = {
    "N":F
}
model9 = CmdStanModel(stan_file='code_9.stan')
sample9 = model9.sample(stan_data)

model10 = CmdStanModel(stan_file='code_10.stan')
# sample10 = model10.sample(stan_data)
y_mean = model10.generate_quantities(data=stan_data, mcmc_sample = sample9)
# print(dir(y_mean))
df = y_mean.generated_quantities_pd
df.plot.hist(bins=50)

# cannot find attribute generated_quantities_pd