#include <QtCore/QVector>
#include <QtCore/QSharedPointer>
#include <chrono>
#include <iostream>

struct Data
{
    uint64_t a;
    uint64_t b;

    explicit Data(uint64_t a, uint64_t b) : a(a), b(b) {}
};

int main()
{
    using namespace std;
    using namespace chrono;
    auto start_time = high_resolution_clock::now();
    //
    {
        QVector<QSharedPointer<Data>> vec;
        vec.reserve(100'000);
        for(size_t i = 0; i < 100'000; ++i)
            vec.append(QSharedPointer<Data>(new Data(i, i / 2)));
    }
    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
    cout << elapsed_time;
    return 0;
}
