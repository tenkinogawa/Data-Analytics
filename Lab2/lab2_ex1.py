import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import scipy.stats as stats

plt.close('all')

F = len('Agnieszka')
L = len('Welian')

array_sample = [0] * F
print(array_sample)
stan_data = {
    "M":F,
    "y":array_sample
}
model = CmdStanModel(stan_file='code_1.stan')
sample = model.sample(stan_data)

data_from_stan = sample.draws_pd()
print(data_from_stan)

Lambda = data_from_stan['lambda']
Lambda.plot.hist(bins=50, title = 'Lambda')

data_all_y = data_from_stan.drop(data_from_stan.columns[0:3],axis=1)
data_all_y.plot.hist(subplots=True, bins=50, title = 'y[k]')
plt.show()