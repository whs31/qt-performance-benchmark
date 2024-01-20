from src import suite, benches
import matplotlib as mpl
import matplotlib.pyplot as plt
import mplcatppuccin

if __name__ == '__main__':
    mpl.style.use("mocha")
    suite.Suite(
        'collections/vector-fill',
        'Fill vector with 500 000 structs', 1000,
        {
            suite.Bench(benches.BenchType.C),
            suite.Bench(benches.BenchType.CXXSTD),
            suite.Bench(benches.BenchType.QTCXX),
            suite.Bench(benches.BenchType.RUST),
            suite.Bench(benches.BenchType.CXXSTD, 'C++ with emplace_back()', '_uf'),
            # benches.BenchType.PYTHON,
        }
    ).plot_all()
    plt.show()
