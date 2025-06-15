import numpy as np

def gaussian(X, Y, a, b, sigma, A):
    power = -0.5*(((X - a)**2 + (Y - b)**2) / (sigma**2))
    return A * np.exp(power)
# center (a,b), amplitude A, stdev sigma
# 2d gaussian bump function

def lorentzian(X, Y, a, b, gamma, A):
    r2 = (X-a)**2 + (Y-b)**2
    return A / (1 + r2 / (gamma**2))

