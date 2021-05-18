########################
## KSHITIJ SRIVASTAVA ##
####### MT 18099 #######
########################

import gym
import gym_maze
import numpy as np
import matplotlib.pyplot as plt
import math


def training():

    rewards_arr = []
    alpha = ALPHA
    gamma = GAMMA
    eps = EPSILON
    # state_0_0 = []
    for ep in range(NUM_EP):
        new_env = env.reset()
        init_state = get_state_coordinates(new_env)
        total_reward = 0
        print("EPISODE = ", ep)
        # print(q_table)
        # state_0_0.append([q_table[0][0][0], q_table[0][0][1], q_table[0][0][2], q_table[0][0][3]])
        for i in range(MAX_MOVES):

            if EXPLORATION:
                if np.random.uniform(0, 1) <= eps:
                    action = env.action_space.sample()
                else:
                    action = int(np.argmax(q_table[init_state]))
            else:
                action = int(np.argmax(q_table[init_state]))


            # reference [https://gym.openai.com/docs/]
            observation, reward, done, info = env.step(action)

            state_new = get_state_coordinates(observation)
            total_reward += reward

            # reference for q-function [run.py given with the assignment]

            #Q-LEARNING
            # q_table[init_state + (action,)] += alpha * (
            #         reward + gamma * np.amax(q_table[state_new]) - q_table[init_state + (action,)])

            #SARSA
            q_table[init_state + (action,)] += alpha * (
                    reward + gamma * q_table[state_new][action] - q_table[init_state + (action,)])
            init_state = state_new
            env.render()

            if done:
                print("Episode %f, Time %f, Total reward = %f" % (ep, i, total_reward))
                rewards_arr.append(total_reward)
                # print(q_table)
                break
        alpha = update_parameter(alpha)
        eps = update_parameter(eps)

    # state_0_0 = np.array(state_0_0)
    # print(state_0_0)
    return rewards_arr


def testing():
    env2 = gym.make("maze-random-5x5-v0")
    # new_env = env.reset()
    # init_state = get_state_coordinates(new_env)
    # total_reward = 0
    for ep in range(NUM_EP):
        new_env = env2.reset()
        init_state = get_state_coordinates(new_env)
        total_reward = 0
        print("EPISODE = ", ep)

        for i in range(MAX_MOVES):
            action = int(np.argmax(q_table[init_state]))

            # reference [https://gym.openai.com/docs/]
            observation, reward, done, info = env2.step(action)

            state_new = get_state_coordinates(observation)
            total_reward += reward
            init_state = state_new
            # env2.render()

            if done:
                print("Episode %f, Time %f, Total reward = %f" % (ep, i, total_reward))
                # print(q_table)
                break


def update_parameter(param):
    return max(0.1, param-0.1)


def plot_learning_curve():
    plt.plot(rewards)
    plt.ylabel("Total Reward")
    plt.xlabel("Episode")
    plt.show()


def get_state_coordinates(state):
    return tuple(state.astype(int).tolist())


if __name__ == '__main__':
    # Hyper-parameters
    EPSILON = 0.9

    GAMMA = 0.9
    ALPHA = 0.9

    NUM_EP = 50
    MAX_MOVES = 1000
    EXPLORATION = False

    env = gym.make("maze-random-5x5-v0")
    env.render()

    maze_size = (5, 5)
    q_table = np.zeros(maze_size + (env.action_space.n,))
    rewards = training()

    plot_learning_curve()
    # testing()
