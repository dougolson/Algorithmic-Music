import random
import matplotlib.pyplot as plt

def random_walk(n):
    nums = [-1,0,1]
    total = 0
    accumulator = []
    for i in range(n):
        choice = random.choice(nums)
        total += choice
        accumulator.append(total)
    return accumulator


if __name__ == '__main__':
    test = random_walk(300)

    plt.plot(test)
    plt.show()