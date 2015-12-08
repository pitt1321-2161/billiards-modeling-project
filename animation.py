import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
import matplotlib.patches as patches


x_coord = #array of x coordinates of balls
y_coord = #array of y coordinates of balls

fig = plt.figure(figsize=(Table_x,Table_y))
ax = plt.axes(xlim=Table_x, ylim=Table_y)

ball1 = plt.Circle((#initial x,initial y),radius,label='ball1')
ball2 = plt.Circle((#initial x,initial y),radius,label='ball2')


def init():
    ball1.center= (#initial x,initial y)
    ax.add_patch(ball1)
    ball2.center=(#initial x,initial y)
    ax.add_patch(ball2)
    return ball1,ball2
    
def animate(i):
        ball1.center = (x_coord[0][i],y_coord[0][i])
        ball2.center = (x_coord[1][i],y_coord[1][i])
        return ball1,ball2    
    
    
anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=10000, 
                               interval=10,
                               blit=False,repeat=False)
                               
                               
FFwriter = animation.FFMpegWriter(fps=30)
Writer = animation.writers['ffmpeg.exe']
writer = Writer(fps=30, metadata=dict(artist='Gabe'), bitrate=1800)

anim.save('billiards.mp4', writer=writer)                              