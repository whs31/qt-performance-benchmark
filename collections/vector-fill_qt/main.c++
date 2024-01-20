#include <QtCore/QVector>
#include <chrono>
#include <iostream>

struct Data
{
    uint64_t a;
    uint64_t b;

    explicit Data(size_t x)
    {
        a = x / 2;
        b = x / (x % 2 + 1);
    }
};

int main()
{
    using namespace std;
    using namespace chrono;
    auto start_time = high_resolution_clock::now();
    //
    QVector<Data> vec;
    for(size_t i = 0; i < 5'000'000; ++i)
        vec.append(Data(i));
    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<milliseconds>(end_time - start_time).count();
    cout << elapsed_time;
    return 0;
}
