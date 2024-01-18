import os


def compile_c(path: str) -> str:
    print(f'Compiling C file: {path}')
    os.system(f'gcc {path} -O3 -o {path}.out')
    return f'{path}.out'