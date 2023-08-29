# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:41:13 2023

@author: ADMIN
"""
import gymnasium as gym
import time
env = gym.make('FrozenLake-v1',render_mode='human')

t_s = 20
eps = 100
l_actions=[]
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
        #l_action[ep].append()
        print("Time Step {}".format(t+1))
        if(done):
            if(reward == 1):
                print("good work")
                i = eps+1
            break
    i+=1