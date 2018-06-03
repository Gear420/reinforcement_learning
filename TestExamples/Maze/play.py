# -*- coding: UTF-8 -*-

"""
游戏的主程序，调用机器人的 Q learning 决策大脑 和 Maze 环境
"""

from env import Maze
from q_learning import QLearning


def update():
    for episode in range(100):
        # 初始化 state（状态）
        state = env.reset()

        step_count = 0

        while True:

            env.render()


            action = RL.choose_action(str(state))


            state_, reward, done = env.step(action)

            step_count += 1  # 增加步数


            RL.learn(str(state), action, reward, str(state_))


            state = state_

            if done:
                print("回合 {} 结束. 总步数 : {}\n".format(episode+1, step_count))
                break

    # 结束游戏并关闭窗口
    print('游戏结束')
    env.destroy()


if __name__ == "__main__":
    # 创建环境 env 和 RL
    env = Maze()
    RL = QLearning(actions=list(range(env.n_actions)))

    # 开始可视化环境
    env.after(100, update)
    env.mainloop()

    print('\nQ 表:')
    print(RL.q_table)
