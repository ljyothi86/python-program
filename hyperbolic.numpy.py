import numpy as np
import matplotlib. pyplot as plt
#hyperbolic tangent (htan) activation function
def htan(x):
    return(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
# htan derivative
def der_htan(x):
    return1-htan(x)*htan(x)
#generating data for graph
    x_data=np.linspace(-6,6,100)
    y_data=htan(x-data)
    dy_data=der_htan(x_data)
 #graph
    plt.plot(x_data,y_data,x_data,dy_data)
    plt.title('htan activation function & Derivation')
    plt.legend(['htan','der_htan'])
    plt.grid()














    t.show()        
