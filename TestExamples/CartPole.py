import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        #确定事件
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        print(done)
        if done:
            print("Episode {} finished after {} timesteps".format(i_episode+1,t+1))
            break
