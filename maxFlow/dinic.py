import numpy as np

def rotate(u,t):
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
                  
    return np.dot(R,u)