import gym
env = gym.make("CartPole-v0")
env.reset()



while True:
    env.render()