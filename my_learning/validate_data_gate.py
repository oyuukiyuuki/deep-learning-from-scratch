import numpy as np

# 重みwとバイアスbを変えてそれぞれのゲートを表現


def AND(x1, x2):
    """_summary_

    Args:
        x1 (_type_): _description_
        x2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


if __name__ == "__main__":
    print(AND(0, 0))
    print(AND(1, 1))
    print(NAND(1, 1))
    print(OR(1, 0))
    print(XOR(1, 0))
