# dataset: Iris flower
# linear regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model


def data_process():
    # --import data from sklearn
    iris_init = datasets.load_iris()
    # print(iris)
    # --binary classification
    iris = iris_init.data[iris_init.target != 2]
    iris_target = iris_init.target[iris_init.target != 2]
    print(iris)
    print(iris_target)


def main():
    data_process()


if __name__ == '__main__':
    main()
