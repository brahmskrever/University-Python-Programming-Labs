##############################
# APS106 Winter 2021 - Lab 2 #
##############################

###########################################
# PART 1 - Cartesian to Polar Coordinates #
###########################################
import math

def magnitude(x, y):
    
    x = float(x)
    y = float(y)
    
    magnitude = math.sqrt((x)**2+(y)**2)
    
    return magnitude

def phase(x,y):
    
    x = float(x)
    y = float(y)
    
    angle = math.atan2(y,x)
    return angle

# PART 2 - Particle Height Calculation  #
#########################################

def particle_height(q,E,m,t,L):
    
    ## TODO: Write your solution here
    q = float(q)
    E = float(E)
    m = float(m)
    t = float(t)
    L = float(L)
    
    height = (-1/20000) * (q*E/m) * (t**2) + (L/2)
    return min(height, L)