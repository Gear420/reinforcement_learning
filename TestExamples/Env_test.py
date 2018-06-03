

import gym
#建立一个环境
env = gym.make('Jamesbond-v4')

env.reset()

while True:
    env.render()
    action = env.action_space.sample()
    print(action)
    observation, reward, done, info = env.step(action)
    print(done)
    print(reward)
    #if done:
        #print("Episode {} finished after {} timesteps".format(i_episode + 1, t + 1))
        #break