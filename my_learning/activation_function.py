import matplotlib.pylab as plt
import numpy as np


def step_function(x):
    return np.array(x > 0, dtype=int)


def sigmoid_function(x):
    return 1/(1+np.exp(-x))


def relu_function(x):
    return np.maximum(0, x)


def identity_function(x):
    return x


def softmax_function(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    # 　オーバフロー対策，ソフトマックス関数でなんらかの定数を足しても引いても変化しない、eの1000乗とかになるとオーバーフローする
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y


if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu_function(x)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()
