# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:41:13 2023

@author: ADMIN
"""
import gymnasium as gym
import time
env = gym.make('FrozenLake-v1',render_mode='human')

t_s = 20

env.reset()
time.sleep(2)
print("Time Step : 0")
env.render()
for t in range(t_s):
    random_action = env.action_space.sample()
    next_state,reqard,done,info,prob=env.step(random_action)
    print("Time Step {}".format(t+1))
    if(done):
        break