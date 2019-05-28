#coding = utf-8
"""
boids.py
Implementation of Craig Reynold's BOIDs
Author: Mahesh Venkitachalam
"""

import sys, argparse
##导入math
import math
#将numpy库导入为np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist, cdist
from numpy.linalg import norm
#设置屏幕上模拟窗口的宽度和高度
width, height = 640, 480


class Boids:
    """Class that represents Boids simulation"""

    def __init__(self, N):
        """ initialize the Boid simulation"""
        # #创建一个numpy的pos 对窗口中心加上10个单元以内的随机偏移
        # #np.random.rand(2*N)创建了一个一维数组，包含范围在[0,1]的2N个随机数
        # #它将是用余保存类鸟群个体的位置
        # #也要注意，numpy的广播规则在这里生效：1x2的数组加到Nx2的数组的每个元素上
        self.pos = [width / 2.0, height / 2.0] + 10 * np.random.rand(2 * N).reshape(N, 2)
        # 生成一个数组，包含N个随机角度，范围在[0,2pi]
        angles = 2 * math.pi * np.random.rand(N)
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.N = N
        # min dist of approach
        self.minDist = 25.0
        # max magnitude of velocities calculated by "rules"
        self.maxRuleVel = 0.03
        # max maginitude of final velocity
        self.maxVel = 2.0

    #在每个时间步骤被调用，以便更新动画
    def tick(self, frameNum, pts, beak):
        # 用一次时间步长更新模拟
        self.distMatrix = squareform(pdist(self.pos))
        # 应用规则
        self.vel += self.applyRules()
        self.limit(self.vel, self.maxVel)
        self.pos += self.vel
        self.applyBC()
        # update data
        pts.set_data(self.pos.reshape(2 * self.N)[::2],
                     self.pos.reshape(2 * self.N)[1::2])
        vec = self.pos + 10 * self.vel / self.maxVel
        beak.set_data(vec.reshape(2 * self.N)[::2],
                      vec.reshape(2 * self.N)[1::2])

    # 限制某些矢量的值，否则速度将会在每个时间步骤无限制地增加，模拟将崩溃
    def limitVec(self, vec, maxVal):
        """limit magnitide of 2D vector"""
        mag = norm(vec)
        if mag > maxVal:
            vec[0], vec[1] = vec[0] * maxVal / mag, vec[1] * maxVal / mag

    # 定义了limit()方法，限制了数组中的值，采用模拟规则计算出的值
    def limit(self, X, maxVal):
        """limit magnitide of 2D vectors in array X to maxValue"""
        for vec in X:
            self.limitVec(vec, maxVal)

    def applyBC(self):
        """应用边界条件"""
        deltaR = 2.0
        for coord in self.pos:
            if coord[0] > width + deltaR:
                coord[0] = - deltaR
            if coord[0] < - deltaR:
                coord[0] = width + deltaR
            if coord[1] > height + deltaR:
                coord[1] = - deltaR
            if coord[1] < - deltaR:
                coord[1] = height + deltaR

    def applyRules(self):
        # apply rule #1 - Separation
        D = self.distMatrix < 25.0
        vel = self.pos * D.sum(axis=1).reshape(self.N, 1) - D.dot(self.pos)
        self.limit(vel, self.maxRuleVel)

        # different distance threshold
        D = self.distMatrix < 50.0

        # apply rule #2 - Alignment
        vel2 = D.dot(self.vel)
        self.limit(vel2, self.maxRuleVel)
        vel += vel2;

        # apply rule #1 - Cohesion
        vel3 = D.dot(self.pos) - self.pos
        self.limit(vel3, self.maxRuleVel)
        vel += vel3

        return vel

    def buttonPress(self, event):
        """event handler for matplotlib button presses"""
        # left click - add a boid
        if event.button is 1:
            self.pos = np.concatenate((self.pos,
                                       np.array([[event.xdata, event.ydata]])),
                                      axis=0)
            # random velocity
            angles = 2 * math.pi * np.random.rand(1)
            v = np.array(list(zip(np.sin(angles), np.cos(angles))))
            self.vel = np.concatenate((self.vel, v), axis=0)
            self.N += 1
            # right click - scatter
        elif event.button is 3:
            # add scattering velocity
            self.vel += 0.1 * (self.pos - np.array([[event.xdata, event.ydata]]))


def tick(frameNum, pts, beak, boids):
    # print frameNum
    """update function for animation"""
    boids.tick(frameNum, pts, beak)
    return pts, beak


# main() function
def main():
    # use sys.argv if needed
    print('starting boids...')
    #创建一个解析对象，方法参数须知：一般我们只选择用description
    parser = argparse.ArgumentParser(description="Implementing Craig Reynold's Boids...")
    # add arguments向该对象中添加你要关注的命令行参数和选项
    parser.add_argument('--num-boids', dest='N', required=False)
    #parser.parse_args()  进行解析
    args = parser.parse_args()

    # number of boids
    N = 20
    if args.N:
        N = int(args.N)

    # 创建Boids
    boids = Boids(N)

    # setup plot
    fig = plt.figure()
    ax = plt.axes(xlim=(0, width), ylim=(0, height))

    pts, = ax.plot([], [], markersize=10,
                   c='k', marker='o', ls='None')
    beak, = ax.plot([], [], markersize=4,
                    c='r', marker='o', ls='None')
    anim = animation.FuncAnimation(fig, tick, fargs=(pts, beak, boids),
                                   interval=50)

    # add a "button press" event handler
    cid = fig.canvas.mpl_connect('button_press_event', boids.buttonPress)

    plt.show()


# call main
if __name__ == '__main__':
    main()
