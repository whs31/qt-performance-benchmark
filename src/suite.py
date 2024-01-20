import os
import subprocess
import pandas
import matplotlib.pyplot as plt
import statistics
from src import compile, benches, execute


class Bench:
    def __init__(self, bench_type: benches.BenchType, name_override: str = '', filename_suffix: str = ''):
        self.bench_type = bench_type
        self.name_override = name_override
        self.filename_suffix = filename_suffix

    def name(self):
        return benches.pretty_name(self.bench_type) if self.name_override == '' else self.name_override


class Suite:
    def __init__(self, path: str, name: str, times: int, window: int, bench_set: set[Bench]):
        self.path = path
        self.name = name
        self.bench_set = bench_set
        self.times = times
        self.window = window
        self.__d = dict()
        self.__avgs = dict()

        self.run()

    def run(self):
        for bench_type in self.bench_set:
            compiled = compile.compile(self.path, bench_type.bench_type, bench_type.filename_suffix)
            print(f'Running {bench_type.name()} {self.times} times')
            ls = list()
            for _ in range(self.times):
                ls.append(execute.execute(compiled, bench_type.bench_type))
            print(f'Average time for {bench_type.name()}: {sum(ls) / len(ls)} μs')
            print(f'Standard deviation for {bench_type.name()}: {statistics.stdev(ls)} μs')
            print(f'Median time for {bench_type.name()}: {statistics.median(ls)} μs')
            self.__avgs[bench_type.name()] = statistics.median(ls)
            self.__d[bench_type.name()] = ls

            if not bench_type == benches.BenchType.PYTHON:
                compile.cleanup(compiled)

    def results(self):
        return self.__d

    def as_dataframe(self):
        return pandas.DataFrame(self.__d)

    def plot(self):
        self.as_dataframe().rolling(window=self.window).mean().plot(kind='line')
        plt.title(self.name)
        plt.legend(loc='upper right')
        plt.ylabel('μs')
        plt.xlabel('times')
        plt.grid(True)

    def plot_averages(self):
        # sort self averages by average
        self.__avgs = dict(sorted(self.__avgs.items(), key=lambda item: item[1]))
        _ = pandas.DataFrame(self.__avgs, index=[0])
        _.plot(kind='bar')
        plt.title(self.name + ' (averages)')
        plt.legend(loc='upper right')
        plt.ylabel('μs')
        plt.xlabel('')
        plt.grid(True)

    def plot_all(self):
        self.plot()
        self.plot_averages()