from src.suite import Suite
from src.suite import Bench
from src.benches import BenchType
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplcatppuccin

if __name__ == '__main__':
    mpl.style.use("frappe")
    Suite(
        'collections/vector-fill',
        'Fill vector with 100 000 structs', times=250, window=50, bench_set=
        {
            Bench(BenchType.C),
            Bench(BenchType.CXXSTD),
            Bench(BenchType.QTCXX),
            Bench(BenchType.RUST),
            Bench(BenchType.CXXSTD, 'C++ with emplace_back()', '_emplace_back'),
            Bench(BenchType.KOTLIN),
            # BenchType.PYTHON,
        }
    ).plot_all()
    ## This suite is not working for now
    # Suite(
    #     'async/signals',
    #     'Emit signal 10 000 times', times=250, window=50, bench_set=
    #     {
    #         Bench(BenchType.QTCXX),
    #     }
    # ).plot_all()
    plt.show()
