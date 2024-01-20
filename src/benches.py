import enum

class BenchType(enum.Enum):
    C = 1
    CXXSTD = 2
    QTCXX = 3
    RUST = 4
    PYTHON = 5
    KOTLIN = 6
    CSHARP = 7


def path_suffix(bench_type: BenchType) -> str:
    return '_qt' if bench_type == BenchType.QTCXX else ""


def extension(bench_type: BenchType) -> str:
    if bench_type == BenchType.C: return 'c'
    elif bench_type == BenchType.CXXSTD: return 'c++'
    elif bench_type == BenchType.QTCXX: return 'c++'
    elif bench_type == BenchType.RUST: return 'rs'
    elif bench_type == BenchType.PYTHON: return 'py'
    elif bench_type == BenchType.KOTLIN: return 'kt'
    elif bench_type == BenchType.CSHARP: return 'cs'


def pretty_name(bench_type: BenchType) -> str:
    if bench_type == BenchType.C: return 'C'
    elif bench_type == BenchType.CXXSTD: return 'C++'
    elif bench_type == BenchType.QTCXX: return 'C++ (Qt)'
    elif bench_type == BenchType.RUST: return 'Rust'
    elif bench_type == BenchType.PYTHON: return 'Python'
    elif bench_type == BenchType.KOTLIN: return 'Kotlin'
    elif bench_type == BenchType.CSHARP: return 'C#'
