#include <chrono>
#include <iostream>
#include <cstdint>
#include <memory>
#include <vector>

using namespace std;
using namespace chrono;

struct Data
{
    uint64_t a;
    uint64_t b;

    explicit Data(uint64_t a, uint64_t b) : a(a), b(b) {}
};

auto main() -> int
{
    auto start_time = high_resolution_clock::now();
    //
    {
        vector<unique_ptr<Data>> vec;
        vec.reserve(100'000);
        for(size_t i = 0; i < 100'000; ++i)
            vec.push_back(make_unique<Data>(i, i / 2));

    }
    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
    cout << elapsed_time;

    return 0;
}

