from src import suite, benches
import matplotlib as mpl
import mplcatppuccin

if __name__ == '__main__':
    mpl.style.use("mocha")
    suite.Suite(
        'collections/vector-fill',
        'Fill vector with 5 000 000 structs', 100,
        {
            benches.BenchType.C,
            benches.BenchType.CXXSTD
            #benches.BenchType.QTCXX
        }
    ).plot()
