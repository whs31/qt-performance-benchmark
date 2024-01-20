from src import suite, benches
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplcatppuccin

if __name__ == '__main__':
    mpl.style.use("frappe")
    suite.Suite(
        'collections/vector-fill',
        'Fill vector with 100 000 structs', times=250, window=50, bench_set=
        {
            suite.Bench(benches.BenchType.C),
            suite.Bench(benches.BenchType.CXXSTD),
            suite.Bench(benches.BenchType.QTCXX),
            suite.Bench(benches.BenchType.RUST),
            suite.Bench(benches.BenchType.CXXSTD, 'C++ with emplace_back()', '_emplace_back'),
            suite.Bench(benches.BenchType.KOTLIN),
            # benches.BenchType.PYTHON,
        }
    ).plot_all()
    plt.show()
