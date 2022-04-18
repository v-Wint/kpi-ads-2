from algorithm import bubble_sort, comb_sort
from random import sample
from math import log
import json
import matplotlib.pyplot as plt


class Tester:
    results = {}

    def __init__(self, filename):
        self.modes = ["best", "reversed", "random"]
        self.lengths = [10, 100, 1000, 5000, 10000, 20000, 50000]
        self.styles = {"best": ',:g', "reversed": ',--r', "random": ',-.b', "O": ',-m', "omega": ',-y'}
        self.filename = filename

    def add_functions(self, *functions):
        self.functions = functions

    def test_function(self, function):
        result = {}
        for mode in self.modes:
            result[mode] = []
            for length in self.lengths:
                result[mode].append([length, 0, 0])
                a = list(range(length))
                if mode == "reversed":
                    a = a[::-1]
                if mode == "random":
                    a = sample(a, length)
                _, result[mode][-1][1], result[mode][-1][2] = function(a)
        return {function.__name__: result}

    def start_testing(self):
        for function in self.functions:
            self.results.update(self.test_function(function))
        self.add_asympt()

    def add_asympt(self):
        self.results["bubble_sort"]["O"] = [[length, length ** 2, length ** 2] for length in self.lengths]
        self.results["bubble_sort"]["omega"] = [[length, length ** 2, 0] for length in self.lengths]
        self.results["comb_sort"]["O"] = [[length, int(length * log(length)), length ** 2] for length in self.lengths]
        self.results["comb_sort"]["omega"] = [[length, int(length * log(length)), 0] for length in self.lengths]

    def save_results(self):
        with open(self.filename, 'w') as file:
            json.dump(self.results, file)

    def get_results(self):
        try:
            with open(self.filename, 'r') as file:
                self.results = json.load(file)
        except IOError:
            print("File seems to not exist")

    def print_results(self):
        k = "|   "
        for func_name, result in self.results.items():
            print(func_name.upper())
            for mode, res in result.items():
                print(k + mode.upper())
                k = "|   |   "
                print(k + "{:<15} {:<15} {:<15}".format("n", "comps", "swaps"))
                for line in res:
                    print(k + "{:<15} {:<15} {:<15}".format(*line))
                k = "|   "
                print(k)

    def graph_results(self):
        fig, axs = plt.subplots(len(self.results), 3)
        j = 0
        for result in self.results.values():
            for key, res in reversed(result.items()):
                x = [res[i][0] for i in range(len(res))]
                y_c = [res[i][1] for i in range(len(res))]
                y_s = [res[i][2] for i in range(len(res))]
                y_sum = [res[i][1] + res[i][2] for i in range(len(res))]
                axs[j, 0].plot(x, y_c, self.styles[key])
                axs[j, 1].plot(x, y_s, self.styles[key])
                axs[j, 2].plot(x, y_sum, self.styles[key])
            axs[0, 0].set_title("Number of comparisons")
            axs[0, 1].set_title("Number of swaps")
            axs[0, 2].set_title("Swaps + comparisons")
            j += 1
        fig.legend(['omega', 'O', 'random', 'reversed', 'best'], loc=7, bbox_to_anchor=(1, 0.5))
        plt.plot()
        plt.show()

    def perform_testing(self):
        self.add_functions(bubble_sort, comb_sort)
        self.start_testing()
        self.save_results()

    def show_testing_results(self):
        self.get_results()
        self.print_results()
        self.graph_results()
