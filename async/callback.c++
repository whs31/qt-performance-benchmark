#include <functional>
#include <cstdint>

using namespace std;

using Callback = function<int (int)>;

int q = 0;
void iota(Callback callback)
{
    callback(++q);
}

auto main() -> int
{
    auto callback = [](int i) -> int
    {
        return i;
    };
    uint64_t sum = 0;
    for(int i = 0; i < 100'000'000; ++i)
        sum += iota([](int x) -> int { return x; });
    return 0;
}