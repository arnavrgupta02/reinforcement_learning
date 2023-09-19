import gymnasium as gym

import time

env = gym.make("CartPole-v1", render_mode= 'human')

env.reset()

env.render() 
ep=0
eps, timeStep, maxRew, num= 10,30,0,0 
for i in range(eps):

    env.reset()
    obs = []
    ret=0
    
    for t in range(timeStep):
    
        env.render()
        
        random_action = env.action_space.sample() 
        n_s, reward, done, info, prob = env.step(random_action)
        obs += [n_s]
        print(n_s)
        ret += reward
        if done:        
            break
    print(ret," - ", i+1)
    if ret> maxRew:
    
        maxRew = ret 
        ep = i+1
        
        obsList = obs

print(ep,maxRew, obsList)