# IPython log file

get_ipython().run_line_magic('logstart', '')
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,5,1)
x = np.linspace(0.0,4.0,100)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"g.", label="squared")
plt.plot(x,y2,"r", label="cubed")
plt.legend()
plt.title("Things 1 and 2")
plt.xlabel("Thing1,x")
plt.ylabel("Thing2,y")
exit()
