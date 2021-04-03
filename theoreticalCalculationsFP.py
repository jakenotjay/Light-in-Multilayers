import numpy as np
import plotly.express as px

def calcR_FP(R, phi):
    numerator = (4 * R) * np.sin(phi)**2
    denominator = (4 * R * np.sin(phi)**2) + ((1-R)**2)
    return numerator / denominator

def calcT_FP(R, phi):
    numerator = (1-R)**2
    denominator = (4 * R * np.sin(phi)**2) + ((1-R)**2)
    return numerator / denominator

def calcR(n_1, n_2):
    numerator = n_1 - n_2
    denominator = n_1 + n_2
    return (numerator/denominator) ** 2

def calcPhi(lamda, n, d):
    return (2 * np.pi)/lamda * n * d

n_pts = 10000
# range of wavelengths
lamda = np.linspace(700, 1000, num=n_pts)
# RI of GaAs
n_g = 3.5227
# RI of air
n_a = 1.0
# thickness
d = 500000.0
# R constant
R = calcR(n_g, n_a)
print('R value of ', R)

R_FP = np.zeros(n_pts)
T_FP = np.zeros(n_pts)

for i in range(n_pts):
    phi = calcPhi(lamda[i], n_g, d)
    R_FP[i] = calcR_FP(R, phi)
    T_FP[i] = calcT_FP(R, phi)
    print('T + R', R_FP[i] + T_FP[i])

fig = px.line(x=lamda, y=R_FP)
fig.show()

