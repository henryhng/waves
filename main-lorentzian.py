import numpy as np
from scipy.ndimage import laplace
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import init

nx, ny = 50, 50 # number of grid points along x & y axes
x = np.linspace(-1, 1, nx)
y = np.linspace(-1, 1, ny)
X, Y = np.meshgrid(x, y)

# initial conditions, regular wave propagation using gaussian
# reg-gaussian
image = init.gaussian(X, Y, a=0.5, b=0, sigma=0.20, A=1.5) # def sigma 0.15, A=2.0

# hat wave using gaussian
# inner = init.gaussian(X, Y, 0, 0, 0.1, 1.0)
# outer = init.gaussian(X, Y, 0, 0, 0.2, 0.5)
# image = inner - outer

# hat wave using lorentzian
inner = init.lorentzian(X, Y, 0, 0, 0.1, 1.5)
outer = init.lorentzian(X, Y, 0, 0, 0.2, 0.7)
image = inner - outer

# define how fast simulation runs
dt = 0.15

# initialize wave speeds with zero everywhere
c = np.zeros([nx, ny]) 

# define where wave propagation occurs
c[:,26:] = 1 # columns 26-49 for each row, speed=1
c[:,:24] = 1
c[17:22,23:27] = 1 #rows 17-21, cols 23-26, speed =1
c[28:33,23:27] = 1

# random propagation
# c = np.ones((nx, ny))


v=0
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# surf = ax.plot_surface(
#     X, Y, image,
#     cmap='RdBu', vmin=-0.05, vmax=0.05 #colormap ranges
# )

def animate(i, ax, fig):
    ax.cla()
    global image
    global v
    a = laplace(image, mode='constant') * np.power(c, 2)
    v += a * dt #update velocity
    image += v * dt #update displacement
    surf = ax.plot_surface(
        X, Y, image,
        cmap='RdBu', vmin=-0.20, vmax=0.20
    )
    ax.set_zlim(-1, 1)
    return surf

anim = FuncAnimation(
    fig,
    animate,
    interval=1,
    cache_frame_data=False,
    fargs=(ax, fig),
    frames=500
)

# to save into gif
anim.save('hat-lorentzian.gif', writer='ffmpeg', fps=30)

# to make it run in matplot instead, use:
# plt.show()