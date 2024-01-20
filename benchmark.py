from src import suite, benches
import matplotlib as mpl
import mplcatppuccin

if __name__ == '__main__':
    mpl.style.use("mocha")
    suite.Suite(
        'collections/vector-fill',
        'Fill vector with 500 000 structs', 250,
        {
            benches.BenchType.C,
            benches.BenchType.CXXSTD,
            benches.BenchType.QTCXX,
            benches.BenchType.RUST,
            benches.BenchType.CXXSTDUNIQUES,
        }
    ).plot()
