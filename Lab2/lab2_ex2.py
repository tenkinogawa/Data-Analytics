import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import scipy.stats as stats

F = len('Agnieszka')
L = len('Welian')

# array_sample = [0] * F
# print(array_sample)
stan_data = {
    "N":2,
    # "theta": 1,
    "y": [0,1] #cannot set 'y':[0,2] - out of range
}

model2 = CmdStanModel(stan_file='code_2.stan')
sample_model2 = model2.sample(stan_data)
theta2 = sample_model2.stan_variable('theta')

df2 = pd.DataFrame({'theta': theta2})
df2.plot.hist(bins=50, title ='theta2')

model3 = CmdStanModel(stan_file='code_3.stan')
sample_model3 = model3.sample(stan_data)
theta3 = sample_model3.stan_variable('theta')

df = pd.DataFrame({'theta': theta3})
df.plot.hist(bins=50, title ='theta3')
plt.show()
