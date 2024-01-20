from src import suite, benches

if __name__ == '__main__':
    a = suite.Suite(
        'collections/vector-fill',
        'Fill vector with 1 000 000 structs', 100,
        {
            benches.BenchType.C,
            benches.BenchType.CXXSTD
            #benches.BenchType.QTCXX
        }
    )
    a.run()
    print(a.results())