import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random


# imported pandas and reading csv file

# file = pd.read_csv('random_plot_data.csv',delimiter = ',')
# print(file)

# def animate(i):
#   file = pd.read_csv('random_plot_data.csv.txt',delimiter = ',')
#   x = file['Column 1']
#   y = file['Column 2']
#   z = file['Column 3']
#   plt.plot(x,y, label = 'Data 1', color = 'green')
#   plt.plot(x,z,label = 'Data 2',color = 'blue')
  
# ani = FuncAnimation(plt.gcf(), animate,interval = 1000)
# plt.tight_layout()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

index = count()
print(next(index))
print(next(index))
print(next(index))

reverse = count(20,-1)
print(next(reverse))
print(next(reverse))
print(next(reverse))
x =[]
y=[]
a = []
b  = []
def animate(i):
  x.append(next(index))
  y.append(next(index))
  a.append(next(reverse))
  b.append(next(index))
  plt.plot(x,y,color = 'blue')
  plt.plot(b,a,color = 'green')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('X Y graph')
ani = FuncAnimation(plt.gcf(), animate,interval =1000)
plt.show()

randx = []
randy = []
# def animateRandom(i):
#   randx.append(random.random())
#   randy.append(random.random())
#   plt.plot(randx,randy,color = 'blue')
#   plt.plot(randy,randx,color = 'green')
#   plt.xlabel('random x')
#   plt.ylabel('random y')
#   plt.title('random x and y title')
# ani = FuncAnimation(plt.gcf(), animateRandom,frames = 1000)
# plt.show()

# Animate qaudratic plot

index = count(-100,0.1)
quadx = []
quady = []
def quadPlot(i):
  quadx.append(next(index))
  quady.append(next(index)**2)
  plt.plot(quadx,quady,color = 'red')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Qaudratic animation')
  plt.legend('X^2')
ani = FuncAnimation(plt.gcf(), quadPlot,frames = 1)
plt.show()
plt.savefig('Quadratic Animation')



