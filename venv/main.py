import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import control as ctl
import math
import symbolic

s = ctl.TransferFunction.s

# Sistema
P1 = 1e3
P2 = 100e3
P3 = 500e3
A0 = 1e3
Z1 = 500
H = (A0*s*(s+Z1))/((s/P1+1)*(s/P2+1)*(s/P3+1))
print("Transferencia")
print(H)

#Separo en parte real e imaginaria de los polos y ceros para hacer diagrama de polos y ceros
x_polos = ctl.pole(H).real
y_polos = ctl.pole(H).imag

x_zeros = ctl.zero(H).real
y_zeros = ctl.zero(H).imag

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_polos,y_polos,marker="x")
ax.scatter(x_zeros, y_zeros, marker="o")
ax.set_xlabel('sigma')
ax.set_ylabel('jw')
ax.set_title("Polos de la transferencia")


#Hago el bode
fig2 = plt.figure()

ctl.bode(H,dB=1, deg = 1);


#Módulo en 3D, en el plano S
fig3 = plt.figure()
ax = fig3.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
# xlen = len(X)
Y = np.arange(-5, 5, 0.25)
# ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# colortuple = ('y', 'b')
# colors = np.empty(X.shape, dtype=str)
# for y in range(ylen):
#     for x in range(xlen):
#         colors[x, y] = colortuple[(x + y) % len(colortuple)]
#
# # Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(X, Y, Z, linewidth=0)

# Customize the z axis.
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))



plt.show()