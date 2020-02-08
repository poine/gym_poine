#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time, numpy as np, gym

import gym_poine
#from . import *


import pdb
class NullActor:
    def __init__(self, env):
        pass
    def predict(self, state):
        return[0.]
    
if __name__ == '__main__':
    np.set_printoptions(linewidth=300, suppress=True)
    env_name = 'pendulum-legacy-v0'
    env = gym.make(env_name)
    env.seed(123)
 
    actor = NullActor(env)
    state = env.reset()
    if 0:
        env.render()
        time.sleep(10)
    else:
        nb_step=1000
        for i in range(nb_step):
            env.render()
            action =  actor.predict(state)
            state, reward, done, info = env.step(action)
            if done: break
            time.sleep(0.01)
