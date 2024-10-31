"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,9,10)
y=np.array([75,68,79,99,89,90,74,18,90,73])
plt.hist(y)
plt.title('performance of student')
plt.xlabel('student number')
plt.ylabel('marks')
plt.show()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,9,10)
y=np.array([75,68,79,99,89,90,74,18,90,73])
plt.bar(x,y)
plt.title('performance of student')
plt.xlabel('student number')
plt.ylabel('marks')
plt.show()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,1)
y=np.array([0,68,79,99,89,90,74,18,90,73])
plt.scatter(x,y)
plt.title('performance of student')
plt.xlabel('student number')
plt.ylabel('marks')
plt.show()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,1)
y=np.array([0,68,79,99,89,90,74,18,90,73])
plt.plot(x,y)
plt.title('performance of student')
plt.xlabel('student number')
plt.ylabel('marks')
plt.show()
"""
import math
import numpy as np
import matplotlib.pyplot as plt
vm=100
t=np.arange(0,10,0.00001)
v=vm*np.sin(2*math.pi*50*t)
v2=vm*np.cos(2*math.pi*50*t)
plt.plot(t,v)
plt.plot(t,v2)
plt.xlabel('timecse')
plt.ylabel('magnitude vost')
plt.title('wave forms')
plt.legend('sine','cosine',sin+cos)
plt.grid()
plt.show()

