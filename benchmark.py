import os

import compile
import subprocess
import time
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def __run(path: str, times: int, name: str) -> float:
    print(f'Running {name} implementation {times} times')
    start = time.time()
    for _ in range(times):
        subprocess.run([path], stdout=open(os.devnull, 'wb'))
    end = time.time()
    avg = (end - start) / times * 1000
    print(f'Elapsed average time: {avg} ms')
    return avg


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


if __name__ == '__main__':
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

    dataframe = dict()
    dataframe['File IO'] = compile_and_run('file-io/write_to_file', times=50, c=True, cpp=True, qt=True)
    df = pd.DataFrame.from_dict(dataframe)
    df = df.transpose()
    df.columns = ['C', 'C++', 'Qt']
    print(df)

    df.plot(kind='bar')
    plt.legend(loc='upper left')
    plt.xlabel('Implementation')
    plt.ylabel('Time (ms)')
    plt.show()
