#include <cstdint>
#include <vector>
#include <chrono>
#include <iostream>

using namespace std;
using namespace chrono;

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

auto main() -> int
{
    auto start_time = high_resolution_clock::now();

    //
    vector<int> vec;
    for(size_t i = 0; i < 10'000'000; ++i)
        vec.push_back(i);

    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<milliseconds>(end_time - start_time).count();
    cout << elapsed_time;
    return 0;
}