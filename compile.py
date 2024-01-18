import os
from sys import platform
import shutil


QT_PREFIX_PATH = 'C:\\Qt\\6.7.0\\mingw_64'
QT_BINARY_PATH = QT_PREFIX_PATH + '\\bin'
QT_CORE_DLL_PATH = QT_BINARY_PATH + '\\Qt6Core.dll'


def compile_c(path: str) -> str:
    print(f'Compiling C file: {path}')
    os.system(f'gcc {path} -O3 -o {path}.out')
    return f'{path}.out'


def compile_cpp(path: str) -> str:
    print(f'Compiling C++ file: {path}')
    os.system(f'g++ {path} -O3 -o {path}.out')
    return f'{path}.out'


def compile_qt(path: str) -> str:
    print(f'Compiling Qt file: {path}')
    os.chdir(path + '_qt')
    try:
        os.mkdir('build')
    except:
        pass
    os.chdir('build')

    if platform == "win32":
        os.system(f'cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=C:\\Qt\\6.7.0\\mingw_64 ..')
        shutil.copyfile(QT_CORE_DLL_PATH, 'Qt6Core.dll')
    else:
        os.system(f'cmake -GNinja -DCMAKE_BUILD_TYPE=Release ..')
    os.system(f'cmake --build .')
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    if platform == 'win32':
        return f'{path}_qt/build/out.out.exe'
    else:
        return f'{path}_qt/build/out.out'