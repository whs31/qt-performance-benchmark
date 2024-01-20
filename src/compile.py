import os
from sys import platform
import shutil
from src import benches
import subprocess


QT5_WINDOWS_PREFIX_PATH = 'C:\\Qt\\5.15.2\\mingw81_64'
QT5_WINDOWS_BINARY_PATH = f'{QT5_WINDOWS_PREFIX_PATH}\\bin'
QT5_WINDOWS_QT5CORE_DLL_PATH = f'{QT5_WINDOWS_BINARY_PATH}\\Qt5Core.dll'


def compile(path: str, bench_type: benches.BenchType, suffix: str = '') -> str:
    print(f'Compiling {benches.pretty_name(bench_type)} file ({path}{suffix}.{benches.extension(bench_type)})')

    if bench_type == benches.BenchType.C:
        os.system(f'gcc {path}{suffix}.{benches.extension(bench_type)} -O3 -o {path}.out')
        return f'{path}.out'

    elif bench_type == benches.BenchType.CXXSTD:
        os.system(f'g++ {path}{suffix}.{benches.extension(bench_type)} -O3 -o {path}.out')
        return f'{path}.out'

    elif bench_type == benches.BenchType.PYTHON:
        return f'{path}{suffix}.{benches.extension(bench_type)}'

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
            return f'{path}{suffix}{benches.path_suffix(bench_type)}\\__build__\\out.out.exe'
        else:
            return f'{path}{suffix}{benches.path_suffix(bench_type)}/__build__/out.out'

    elif bench_type == benches.BenchType.RUST:
        os.system(f'rustc {path}{suffix}.{benches.extension(bench_type)} -C opt-level=3 -o {path}.out')
        return f'{path}.out'


def cleanup(path: str):
    if os.path.exists(path):
        os.remove(path)
    pdb = path[:-3:] + 'pdb'
    if os.path.exists(pdb):
        os.remove(pdb)