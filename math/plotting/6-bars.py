#!/usr/bin/env python3
"""plot a stacked bar graph"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """plot a stacked bar graph"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    labels = ['Apples', 'Bananas', 'Oranges', 'Peaches']

    bottom = np.zeros(3)
    for i in range(4):
        plt.bar(people, fruit[i], bottom=bottom,
                color=colors[i], label=labels[i], width=0.5)
        bottom += fruit[i]

    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()

    plt.show()
