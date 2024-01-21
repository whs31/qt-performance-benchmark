from src.suite import Suite
from src.suite import Bench
from src.benches import BenchType
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplcatppuccin


predefined_suites = {
    'collections/vector-fill': (
        'Fill vector with 100 000 structs',
        250,
        50,
        {
            Bench(BenchType.C),
            Bench(BenchType.CXXSTD),
            Bench(BenchType.QTCXX),
            Bench(BenchType.RUST),
            Bench(BenchType.CXXSTD, 'C++ with emplace_back()', '_emplace_back'),
            Bench(BenchType.KOTLIN),
            # BenchType.PYTHON
        }
    ),
    'memory/smart-pointer': (
        'Create 100 000 smart pointers',
        250,
        50,
        {
            Bench(BenchType.C),
            Bench(BenchType.CXXSTD),
            Bench(BenchType.QTCXX),
            Bench(BenchType.RUST),
        }
    ),
    'memory/qobject-delete': (
        'Delete 10 000 QObject instances',
        250,
        50,
        {
            Bench(BenchType.QTCXX, 'Raw delete', '_raw'),
            Bench(BenchType.QTCXX, 'Smart pointer delete', '_unique'),
            Bench(BenchType.QTCXX, 'Delete via qobject tree', '_this'),
        }
    )
}


def run_suites(suites: list[str]):
    for suite in suites:
        __suite = predefined_suites[suite]
        Suite(suite, __suite[0], __suite[1], __suite[2], __suite[3]).plot_all()


if __name__ == '__main__':
    mpl.style.use("frappe")
    run_suites(
        [
            # 'collections/vector-fill',
            #'memory/smart-pointer'
            'memory/qobject-delete'
        ]
    )
    plt.show()
