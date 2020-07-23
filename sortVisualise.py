import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random
import selectionSort
import quickSort
import mergeSort
import insertionSort
import bubbleSort


class Visualize:  
    def __init__(self, n, dataset, algo):
        self.n=n
        self.dataset=dataset
        self.algo=algo
        self.datasetName=''
        self.algoName=''

        if dataset=="1":
            # for random unique values
            # n=int(input("enter array size\n"))
            self.a=[i for i in range(1, n+1)]
            random.shuffle(self.a)
            self.datasetName='Random'

        elif dataset=="2":
            # few unique elements
            self.a = [i for i in range(1, n//2)]
            self.k = random.randint(n//3, n//2)
            self.a = [ele for ele in self.a for i in range(k)]
            random.shuffle(self.a)
            self.a=self.a[:n]
            self.datasetName='Few Unique Elements'

        else:
            # reverse sorted array
            self.a=[i for i in range(1, n+1)]
            self.a.reverse()
            self.datasetName='Reverse Sorted'


        if algo=="a": 
            self.generator=selectionSort.selection(self.a)
            self.algoName='Selection Sort'
            # aFrame=(i[0] for i in generator)
            # highlight=(i[1] for i in generator)

        elif algo=="b":
            self.generator=bubbleSort.bubblesort(self.a)
            self.algoName='Bubble Sort'

        elif algo=="c":
            self.generator = mergeSort.mergesort(self.a, 0, len(self.a)-1)
            self.algoName='Merge Sort'

        elif algo=="d":
            self.generator=insertionSort.insertionsort(self.a)
            self.algoName='Insertion Sort'
            
        else:
            self.generator=quickSort.quicksort(self.a, 0, n-1)
            self.algoName='Quick Sort'


        plt.style.use('fivethirtyeight')

        self.data_normalizer = mp.colors.Normalize()
        self.color_map = mp.colors.LinearSegmentedColormap(
            "my_map",
            {
                "red": [(0, 1.0, 1.0),
                        (1.0, .5, .5)],
                "green": [(0, 0.5, 0.5),
                          (1.0, 0, 0)],
                "blue": [(0, 0.50, 0.5),
                         (1.0, 0, 0)]
            }
        )
       
    
    def visual2d(self):
        fig, ax = plt.subplots()
        bar_rects = ax.bar(range(len(self.a)), self.a, align="edge", color=self.color_map(self.data_normalizer(range(self.n))))
        ax.set_xlim(0, len(self.a))
        ax.set_ylim(0, int(1.1*len(self.a)))
        ax.set_title("ALGORITHM : "+self.algoName+"\n"+"DATA SET : "+self.datasetName, fontdict={'fontsize': 13, 'fontweight': 'medium', 'color' : '#E4365D'})
        text = ax.text(0.01, 0.95, "", transform=ax.transAxes, color="#E4365D")
        iteration = [0]

        def animate(A, rects, iteration):
            for rect, val in zip(rects, A):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("iterations : {}".format(iteration[0]))

        anim = FuncAnimation(fig, func=animate,
            fargs=(bar_rects, iteration), frames=self.generator, interval=50,
            repeat=False)
        plt.show()

    def visual3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        z = np.zeros(self.n)
        dx = np.ones(self.n)
        dy = np.ones(self.n)
        dz = [i for i in range(len(self.a))]
        rects = ax.bar3d(range(len(self.a)), self.a, z, dx, dy, dz, color=self.color_map(self.data_normalizer(range(self.n))))
        ax.set_xlim(0, len(self.a))
        ax.set_ylim(0, int(1.1*len(self.a)))
        ax.set_title("ALGORITHM : "+self.algoName+"\n"+"DATA SET : "+self.datasetName, fontdict={'fontsize': 13, 'fontweight': 'medium', 'color' : '#E4365D'})
        text = ax.text2D(0.1,0.95, "", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color="#E4365D")
        iteration = [0]

        def animate(A, rects, iteration):
            ax.collections.clear()
            ax.bar3d(range(len(self.a)), A, z, dx, dy, dz, color=self.color_map(self.data_normalizer(range(self.n))))
            iteration[0] += 1
            text.set_text("iterations : {}".format(iteration[0]))

        anim = FuncAnimation(fig, func=animate,
            fargs=(rects, iteration), frames=self.generator, interval=50,
            repeat=False)
        plt.show()

# v=Visualize(10, "1", "c")
# v.visual2d()
# v.visual3d()
