"""A solver for the 1D diffussion equation."""
#mkdir ivy_diffusion: make a new directory
#lab : ~ $ cd ivy_diffusion/: opens the directory
#touch solver.py: make a new python file
#ls: lists files in a directory
#ls -l: tells how many conents are in a file
#pass is a place holder

import numpy as np

np.set_printoptions(formatter={"float":"{: 6.1f}".format})


def solve1d(concentration, spacing, time_step, diffusivity): #making a function!! yay with parameters yass
    flux = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing #C[1:-1] = C[1:-1] - dt * np.diff(q) / dx
    return concentration 
#pass by reference rather that 0 the return

def _example():
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    print(C)
    
    for _ in range(1,5): 
        C = solve1d(C, dx, dt, D)
        print(C)
    

if __name__== "__main__":
    _example()
    