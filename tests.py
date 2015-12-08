import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from nose.tools import assert_equal
% matplotlib inline


def EnergyTest(v1i,v2i,w1i,w2i,v1f,v2f,w1f,w2f,m,r):
    
    KEI1 = .5*m*D3VectorAbs(v1i)**2 + .2*(m*r**2)*D3VectorAbs(w1i)**2
    KEI2 = .5*m*D3VectorAbs(v2i)**2 + .2*(m*r**2)*D3VectorAbs(w2i)**2
    KEF1 = .5*m*D3VectorAbs(v1f)**2 + .2*(m*r**2)*D3VectorAbs(w1f)**2
    KEF2 = .5*m*D3VectorAbs(v2f)**2 + .2*(m*r**2)*D3VectorAbs(w2f)**2
    
    DelKE = KEI1 + KEI2 - KEF1 - KEF2
    
    if DelKE > .1:
        print("ya done fucked up, son")
    
    if DelKE < -.1:
        print("ya done fucked up, son")
    else:
        print("hell yea")
        
     
def test_collision_detection_bb_false():
    r1 = np.array([0,4])
    r2 = np.array([2,0])
    v1 = np.array([2,0])
    v2 = np.array([0,2])
    dt = 1
    exp = False
    obs = collision_detection_bb(r1,r2,v1,v2,dt)
    assert_equal(exp,obs)

def test_collision_detection_bb_true():
    r1 = np.array([0,4])
    r2 = np.array([2,0])
    v1 = np.array([2.00001,0])
    v2 = np.array([0,2.00001])
    dt = 1
    exp = True
    obs = collision_detection_bb(r1,r2,v1,v2,dt)
    assert_equal(exp,obs)
    
def test_collision_detection_bw1():
    r1 = [2,2]
    v1 = [-1,-1]
    dt = 1
    obs = collision_detection_bw(r1,v1,dt)
    exp = False
    assert_equal(exp,obs)
    
def test_collision_detection_bw2():
    r2 = [2,8]
    v2 = [-1,1]
    dt = 1
    obs = collision_detection_bw(r2,v2,dt)
    exp = False
    assert_equal(exp,obs)
    
def test_collision_detection_bw3():
    r3 = [2,8]
    v3 = [1,1]
    dt = 1
    obs = collision_detection_bw(r3,v3,dt)
    exp = False
    assert_equal(exp,obs)
    
def test_collision_detection_bw4():
    r4 = [2,2]
    v4 = [1,-1]
    dt = 1
    obs = collision_detection_bw(r4,v4,dt)
    exp = False
    assert_equal(exp,obs)        
        
        
        