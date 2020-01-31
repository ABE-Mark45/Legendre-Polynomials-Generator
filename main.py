import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-1, 1, 100)

p = []

n = 30

for i in range(n):
    Y = np.zeros_like(x)
    c = 1
    j = 1
    if i % 2 == 0:
        Y += 1
        j = 0
    else:
        Y = x.copy()


    while(j < i):
        c *= (j-i)*(j+i+1)/((j+1)*(j+2))
        Y += c*np.power(x, j+2)
        j += 2
    Y /= Y[-1]
    p.append(Y)


fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1.1))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    global x, p
    line.set_data([x]*i, p[:i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=30, interval=600, blit=True)

anim.save('basic_animation.mp4', fps=3, extra_args=['-vcodec', 'libx264'])
plt.show()
