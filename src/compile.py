import os
from sys import platform
import shutil
from src import benches
import subprocess
import time


QT5_WINDOWS_PREFIX_PATH = 'C:\\Qt\\5.15.2\\mingw81_64'
QT5_WINDOWS_BINARY_PATH = f'{QT5_WINDOWS_PREFIX_PATH}\\bin'
QT5_WINDOWS_QT5CORE_DLL_PATH = f'{QT5_WINDOWS_BINARY_PATH}\\Qt5Core.dll'


def compile(path: str, bench_type: benches.BenchType, suffix: str = '') -> (str, float):
    print(f'Compiling {benches.pretty_name(bench_type)} file ({path}{suffix}.{benches.extension(bench_type)})')

    # measure time for compilation
    start_time = time.time()
    out = str()

    if bench_type == benches.BenchType.C:
        os.system(f'gcc {path}{suffix}.{benches.extension(bench_type)} -O3 -o {path}.out')
        out =  f'{path}.out'

    elif bench_type == benches.BenchType.CXXSTD:
        os.system(f'g++ {path}{suffix}.{benches.extension(bench_type)} -O3 -o {path}.out')
        out =  f'{path}.out'

    elif bench_type == benches.BenchType.PYTHON:
        out =  f'{path}{suffix}.{benches.extension(bench_type)}'

    elif bench_type == benches.BenchType.QTCXX:
        os.chdir(path + suffix + benches.path_suffix(bench_type))
        try:
            os.mkdir('__build__')
        except:
            pass
        os.chdir('__build__')
        if platform == "win32":
            # silent
            subprocess.run(['cmake', '-GNinja', '-DCMAKE_BUILD_TYPE=Release', f'-DCMAKE_PREFIX_PATH={QT5_WINDOWS_PREFIX_PATH}', '..'], stdout=subprocess.DEVNULL)
            shutil.copyfile(QT5_WINDOWS_QT5CORE_DLL_PATH, 'Qt5Core.dll')
        else:
            subprocess.run(['cmake', '-GNinja', '-DCMAKE_BUILD_TYPE=Release', '..'], stdout=subprocess.DEVNULL)
        subprocess.run(['cmake', '--build', '.'], stdout=subprocess.DEVNULL)
        # if platform == 'win32':
        #     os.rename('out.out.exe', f'{path}.out')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        if platform == 'win32':
            out = f'{path}{suffix}{benches.path_suffix(bench_type)}\\__build__\\out.out.exe'
        else:
            out =  f'{path}{suffix}{benches.path_suffix(bench_type)}/__build__/out.out'

    elif bench_type == benches.BenchType.RUST:
        os.system(f'rustc {path}{suffix}.{benches.extension(bench_type)} -C opt-level=3 -o {path}.out')
        out = f'{path}.out'

    elif bench_type == benches.BenchType.KOTLIN:
        os.system(f'kotlinc {path}{suffix}.{benches.extension(bench_type)} -include-runtime -d {path}.jar')
        out = f'{path}.jar'

    end_time = time.time()
    compilation_time = end_time - start_time
    print(f"Compilation time: {compilation_time} seconds")
    return out, compilation_time


def cleanup(path: str):
    if os.path.exists(path):
        os.remove(path)
    pdb = path[:-3:] + 'pdb'
    if os.path.exists(pdb):
        os.remove(pdb)

    # if platform == 'win32':
    #     if os.path.exists(f'{path}{benches.path_suffix(benches.BenchType.QTCXX)}\\__build__'):
    #         shutil.rmtree(f'{path}{benches.path_suffix(benches.BenchType.QTCXX)}\\__build__')
    # else:
    #     if os.path.exists(f'{path}{benches.path_suffix(benches.BenchType.QTCXX)}/__build__'):
    #         shutil.rmtree(f'{path}{benches.path_suffix(benches.BenchType.QTCXX)}/__build__')