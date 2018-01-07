import gym
import numpy
from time import sleep
import getch

# General episode runner
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

def manual_control(env):
    for t in range(200):
        env.render()
        # print(observation)
        key_press = getch.getch()
        print(key_press)
        action = 0
        if key_press == 'd':
            action = 1
        if key_press == 'a':
            action = 0
        observation, reward, done, info = env.step(action)
        print(" [ action ] ", action)
        print(" [ observation ] ", observation)
        print(" [ reward ] ", reward)
        print(" [ info ] ", info)
        print(" [ done ] ", done)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break

def random_search(env):
    best_params = None
    best_reward = 0
    for _ in range(10000):
        parameters = (numpy.random.rand(4) * 2 - 1)
        reward = run_episode(env, parameters)
        print(reward)
        if reward > best_reward:
            best_reward = reward
            best_params = parameters
            # considered solved if the agent lasts 200 timesteps
            if reward == 200:
                print("[ best params ]", best_params)
                print("[ best reward ]", best_reward)
                break

def hill_climbing(env):
    noise_scaling = 0.1
    parameters = numpy.random.rand(4) * 2 - 1
    bestreward = 0
    for _ in range(10000):
        newparams = parameters + (numpy.random.rand(4) * 2 - 1) * noise_scaling
        reward = 0
        run = run_episode(env, newparams)
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            if reward == 200:
                break


env = gym.make('CartPole-v0')
# print(" ------------------------ ")
#
# print(env.action_space)
# print(env.observation_space)
#
# print(env.observation_space.high)
# print(env.observation_space.low)
#
# print(" ------------------------ ")

# Start any type of agent
# manual_control(env)
# random_search(env)
hill_climbing(env)
