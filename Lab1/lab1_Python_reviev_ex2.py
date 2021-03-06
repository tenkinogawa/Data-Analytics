import cmdstanpy
import numpy
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel
import os

F = len("Agnieszka")
L = len("Welian")
print([0]*F + [1] * L)
stan_data = {
    "N":F+L,
    "y":[0] * F + [1] * L
}

model = CmdStanModel(stan_file='bern_1.stan')
sample = model.sample(stan_data)
theta = sample.stan_variable('theta')
summary = sample.summary()

q5=numpy.quantile(theta,0.05)
q50=numpy.quantile(theta,0.5)
q95=numpy.quantile(theta,0.95)
qMean=theta.mean()

plt.figure()
plt.hist(theta, bins=50)
plt.axvline(q5, color='r')
plt.axvline(q50, color='g')
plt.axvline(q95, color='b')
plt.axvline(qMean, color='k')
plt.grid(True)
plt.legend(['5%','Median','95%','Mean'])
plt.show()