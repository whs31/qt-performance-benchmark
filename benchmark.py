import compile
import subprocess


def compile_and_run(path: str):
    c_exe = compile.compile_c(path + '.c')
    cpp_exe = compile.compile_cpp(path + '.c++')
    qt_exe = compile.compile_qt(path)
    subprocess.run([c_exe])
    subprocess.run([cpp_exe])
    subprocess.run([qt_exe])


if __name__ == '__main__':
    compile_and_run('file-io/write_to_file')