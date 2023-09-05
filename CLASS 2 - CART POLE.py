# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:29:22 2023

@author: Admin
"""

""" Cart Pole env """


import gymnasium as gym
import time
env = gym.make('CartPole-v1',render_mode='human')

t_s = 20
eps = 100
i=0
while(i<eps):
    print("eps ",i+1,"\n\n")
    env.reset()
    time.sleep(2)
    print("Time Step : 0")
    env.render()
    for t in range(t_s):
        random_action = env.action_space.sample()
        next_state,reward,done,info,prob=env.step(random_action)
        print("Time Step {}".format(t+1))
        print(random_action)
        if(done):
            if(reward == 1):
                print("good work")
                i = eps+1
            
    env.reset()
    i+=1
