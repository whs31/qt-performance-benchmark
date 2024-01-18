import compile
import subprocess


def compile_and_run(path: str):
    c_exe = compile.compile_c(path)
    subprocess.run([c_exe])


if __name__ == '__main__':
    compile_and_run('file-io/write_to_file.c')