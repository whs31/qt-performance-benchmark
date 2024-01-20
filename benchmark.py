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
            benches.BenchType.C,
            benches.BenchType.CXXSTD,
            benches.BenchType.QTCXX,
            benches.BenchType.RUST,
            benches.BenchType.CXXSTDUNIQUES,
            # benches.BenchType.PYTHON,
        }
    ).plot_all()
    plt.show()
