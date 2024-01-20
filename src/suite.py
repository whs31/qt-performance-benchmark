import os
import subprocess
import pandas
import matplotlib.pyplot as plt
from src import compile, benches, execute


class Suite:
    def __init__(self, path: str, name: str, times: int, bench_set: set[benches.BenchType]):
        self.path = path
        self.name = name
        self.bench_set = bench_set
        self.times = times
        self.__d = dict()

        self.run()

    def run(self):
        for bench_type in self.bench_set:
            compiled = compile.compile(self.path, bench_type)
            print(f'Running {benches.pretty_name(bench_type)} {self.times} times')
            ls = list()
            for _ in range(self.times):
                ls.append(execute.execute(compiled, bench_type))
            print(f'Average time for {benches.pretty_name(bench_type)}: {sum(ls) / len(ls)} ms')
            self.__d[benches.pretty_name(bench_type)] = ls
            compile.cleanup(compiled)

    def results(self):
        return self.__d

    def as_dataframe(self):
        return pandas.DataFrame(self.__d)

    def plot(self):
        self.as_dataframe().plot(kind='line')
        plt.title(self.name)
        plt.legend(loc='upper right')
        plt.ylabel('ms')
        plt.xlabel('times')
        plt.grid(True)
        plt.show()