import subprocess
from src import benches


def execute(path: str, bench_type: benches.BenchType) -> float:
    # print(f'Running {benches.pretty_name(bench_type)} file ({path})')
    _ = subprocess.run([path], capture_output=True, text=True)
    # print(_.stdout)
    return float(_.stdout)
