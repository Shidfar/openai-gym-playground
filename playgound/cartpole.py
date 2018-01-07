import gym
import numpy
from time import sleep

# import np
# import getch

def run_episode(env, parameters):
    observation = env.reset()
    env.render()
    # sleep(5)
    totalreward = 0
    for t in range(200):
        action = 0 if numpy.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        # print(" [ observation ] ", observation)
        totalreward += reward
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
    return totalreward


# print(" ------------------------ ")
#
# print(env.action_space)
# print(env.observation_space)
#
# print(env.observation_space.high)
# print(env.observation_space.low)
#
# print(" ------------------------ ")

# for i_episode in range(20):
# observation = env.reset()
# print(observation)
# thetha1 = (observation) = env.reset()
# thetha2 = numpy.random.rand(4) * 2 - 1
# print(numpy.matmul(thetha1, thetha2))

env = gym.make('CartPole-v0')
# parameters = numpy.random.rand(4) * 2 - 1
# print(run_episode(env, parameters))

bestParams = None
bestReward = 0
for _ in range(10000):
    parameters = numpy.random.rand(4) * 2 - 1
    reward = run_episode(env, parameters)
    print(reward)
    if reward > bestReward:
        bestReward = reward
        bestParams = parameters
        # considered solved if the agent lasts 200 timesteps
        if reward == 200:
            print("[ best params ]", bestParams)
            print("[ best reward ]", bestReward)
            break

# for t in range(200):
#     env.render()
#     # print(observation)
#     # key_press = getch.getch()
#     # print(key_press)
#     action = 0 if numpy.matmul(thetha1, thetha2) < 0 else 1
#     # if key_press == 'd':
#     #     action = 1
#     # if key_press == 'a':
#     #     action = 0
#     observation, reward, done, info = env.step(action)
#     thetha2 = thetha1
#     thetha1 = observation
#     # print(" [ action ] ", action)
#     print(" [ observation ] ", observation)
#     print(" [ reward ] ", reward)
#     # print(" [ info ] ", info)
#     print(" [ done ] ", done)
#     if done:
#         print("Episode finished after {} timesteps".format(t+1))
#         break
