# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:50:02 2023

@author: student
"""

import gymnasium as gym
import numpy
import pandas as pd
from collections import defaultdict

env = gym.make('Blackjack-v1',render_mode ='human')

def policy(state):
    return 0 if state[0]>19 else 1
state = env.reset()
state = state[0]
print(state)

print(policy(state))
num_timesteps = 100
def generate_episode(policy):
    episode=[]
    state = env.reset()
    state = state[0]
    for t in range(num_timesteps):
        action = policy(state)
        next_state,reward,done,info,trans_prob = env.step(action)
        episode.append((state,action,reward))
        if done:
            break
        state = next_state
    return episode
print(generate_episode(policy))