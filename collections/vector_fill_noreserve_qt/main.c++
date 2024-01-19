#include <QtCore/QVector>

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
    QVector<int> vec;
    for(size_t i = 0; i < 1'000'000; ++i)
        vec.append(i);
    return 0;
}