import os

import compile
import subprocess
import time
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplcyberpunk


def __run(path: str, times: int, name: str) -> list:
    print(f'Running {name} implementation {times} times')
    start = time.time()
    iters = list()
    for _ in range(times):
        __s = time.time()
        subprocess.run([path], stdout=open(os.devnull, 'wb'))
        iters.append((time.time() - __s) * 1000)
    del iters[0]
    end = time.time()
    avg = (end - start) / times * 1000
    print(f'Elapsed average time: {avg} ms')
    return iters


def compile_and_run(path: str, times: int, c: bool, cpp: bool, qt: bool) -> dict:
    result = dict()
    if c:
        c_exe = compile.compile_c(path + '.c')
        res = __run(c_exe, times, 'C')
        result['C'] = res
    if cpp:
        cpp_exe = compile.compile_cpp(path + '.c++')
        res = __run(cpp_exe, times, 'C++')
        result['C++'] = res
    if qt:
        qt_exe = compile.compile_qt(path)
        res = __run(qt_exe, times, 'Qt')
        result['Qt'] = res
    return result


def plot(dict: dict, title: str):
    df = pd.DataFrame.from_dict(dict)
    df.plot(kind='line', subplots=False)
    #plt.grid()
    plt.title(title)
    plt.legend(loc='upper right')
    plt.xlabel('Iteration')
    plt.xticks([])
    plt.ylabel('Time (ms)')
    plt.tight_layout()
    mplcyberpunk.add_glow_effects(gradient_fill=True)
    #mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.3)
    plt.show()


if __name__ == '__main__':
    #plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.style.use("cyberpunk")

    plot(compile_and_run('collections/vector_fill_noreserve', times=100, c=False, cpp=True, qt=True), 'Collections - Vector Fill (No Reserve)')
    plot(compile_and_run('file-io/write_to_file', times=50, c=True, cpp=True, qt=True), 'File I/O - Write to File')
    #dataframe['Callbacks'] = compile_and_run('async/callback', times=50, c=True, cpp=True, qt=False)
