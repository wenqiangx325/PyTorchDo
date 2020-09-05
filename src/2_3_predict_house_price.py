
from pdb import main
from re import T
from numpy.ma.core import size

import torch
import matplotlib.pyplot as plt
from torch import tensor
from torch.autograd import Variable

if __name__ == "__main__":
    # random data form dataset
    x = torch.linspace(0, 100)
    y = x + torch.rand(100) * 100
    # plot dataset
    # plt.plot(x, y, "b*")
    # plt.show()

    # prepare train set and test set
    x_train = x[:-10]
    y_train = y[:-10]
    x_test = x[-10:]
    y_test = y[-10:]

    # predict function
    # y = a * x + b
    a = torch.rand(1, requires_grad=True)
    b = torch.rand(1, requires_grad=True)

    # learning rate
    r = 0.0002

    #
    for ii in range(10000):
        # y = a * x + b
        predictions = a * x_train + b
        # lost function
        # L =
        loss = torch.mean((predictions - y_train) ** 2)

        print(f"loss: {loss}")

        # auto grad
        loss.backward()

        # update a, b by grad
        a.data.add_(- r * a.grad.data)
        b.data.add_(- r * b.grad.data)

        # clear a, b 's grad
        a.grad.data.zero_()
        b.grad.data.zero_()

    plt.plot(x, y, "b*")
    plt.plot(x_train, a.data * x_train + b.data)
    plt.show()


