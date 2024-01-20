import os
import subprocess
from src import compile, benches, execute


class Suite:
    def __init__(self, path: str, name: str, times: int, bench_set: set[benches.BenchType]):
        self.path = path
        self.name = name
        self.bench_set = bench_set
        self.times = times
        self.__d = dict()

    def run(self):
        for bench_type in self.bench_set:
            compiled = compile.compile(self.path, bench_type)
            print(f'Running {benches.pretty_name(bench_type)} {self.times} times')
            ls = list()
            for _ in range(self.times):
                ls.append(execute.execute(compiled, bench_type))
            self.__d[benches.pretty_name(bench_type)] = ls
            compile.cleanup(compiled)

    def results(self):
        return self.__d