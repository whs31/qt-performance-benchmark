import subprocess
from src import benches


def execute(path: str, bench_type: benches.BenchType) -> float:
    # print(f'Running {benches.pretty_name(bench_type)} file ({path})')
    if bench_type == benches.BenchType.PYTHON:
        x = subprocess.run(['python', path], capture_output=True, text=True)
    else:
        x = subprocess.run([path], capture_output=True, text=True)
    return float(x.stdout)
