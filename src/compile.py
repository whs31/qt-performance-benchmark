import os
from sys import platform
import shutil
from src import benches


QT5_WINDOWS_PREFIX_PATH = 'C:\\Qt\\5.15.2\\mingw81_64'
QT5_WINDOWS_BINARY_PATH = f'{QT5_WINDOWS_PREFIX_PATH}\\bin'
QT5_WINDOWS_QT5CORE_DLL_PATH = f'{QT5_WINDOWS_BINARY_PATH}\\Qt5Core.dll'


def compile(path: str, bench_type: benches.BenchType) -> str:
    print(f'Compiling {benches.pretty_name(bench_type)} file ({path}.{benches.extension(bench_type)})')

    if bench_type == benches.BenchType.C:
        os.system(f'gcc {path}.{benches.extension(bench_type)} -O3 -o {path}.out')
        return f'{path}.out'

    elif bench_type == benches.BenchType.CXXSTD:
        os.system(f'g++ {path}.{benches.extension(bench_type)} -O3 -o {path}.out')
        return f'{path}.out'

    elif bench_type == benches.BenchType.QTCXX:
        os.chdir(path + benches.path_suffix(bench_type))
        try:
            os.mkdir('__build__')
        except:
            pass
        os.chdir('__build__')
        if platform == "win32":
            os.system(f'cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH={QT5_WINDOWS_PREFIX_PATH} ..')
            shutil.copyfile(QT5_WINDOWS_QT5CORE_DLL_PATH, 'Qt5Core.dll')
        else:
            os.system(f'cmake -GNinja -DCMAKE_BUILD_TYPE=Release ..')
        os.system(f'cmake --build .')
        if platform == 'win32':
            os.rename(f'{path}.out.exe', f'{path}.out')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        return f'{path}.out'

    elif bench_type == benches.BenchType.RUST:
        os.system(f'rustc {path}.{benches.extension(bench_type)} -C opt-level=3 -o {path}.out')
        return f'{path}.out'


def cleanup(path: str):
    if os.path.exists(path):
        os.remove(path)
    pdb = path[:-3:] + 'pdb'
    if os.path.exists(pdb):
        os.remove(pdb)