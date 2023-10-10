
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:05:22 2023
@author: Admin
"""
import gymnasium as gym
import numpy as np
env = gym.make('FrozenLake-v1',  render_mode="human")
def compute_value_function(policy):
    num_iteration = 1000
    threshold = 1e-20
    gamma = 1.0
    value_table = np.zeros(env.observation_space.n)
    for i in range(num_iteration):
        updated_val_table = np.copy(value_table)
        for s in range(env.observation_space.n):
            a = policy[s]
            value_table[s] = sum([
                prob * (r + gamma * updated_val_table[s_])
                for prob,s_,r, _ in env.P[s][a]
                ])
        if (np.sum (np.fabs(updated_val_table - value_table)) <= threshold) :
            break
    return(value_table)
    
def extract_policy(value_table):
    gamma = 1.0
    policy = np.zeros(env.observation_space.n)
    
    for s in range(env.observation_space.n) :
        Q_vaules = [sum([prob * (r + gamma * value_table[s_])
                         for prob, s_, r, _ in env.P[s][a]])
                            for a in range(env.action_space.n)]
        policy[s] = np.argmax(np.array(Q_vaules))
    
    return policy
def policy_iteration(env):
    num_iteration = 1000
    policy = np.zeros(env.observation_space.n)
    for i in range(num_iteration):
        value_function = compute_value_function(policy)
        new_policy = extract_policy(value_function)
        
        if(np.all(policy == new_policy)):
            break
        policy = new_policy
    return policy
env.reset()
env.render()
optimal_policy = policy_iteration(env)
print(optimal_policy)
state = env.reset()
s = state[0]
done = False
tot_reward = 0
while not done:
    (next_state, reward, done, _, _) = env.step(int(optimal_policy[s]))
    env.render()
    s = next_state
    tot_reward += reward 
    if done:
        break
    
print("Return = ", tot_reward)
env.close()
        