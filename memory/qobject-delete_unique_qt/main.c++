#include <chrono>
#include <iostream>
#include <memory>
#include <vector>
#include <QtCore/QObject>

using namespace std;
using namespace chrono;

class Object : public QObject
{
    Q_OBJECT

    public:
        explicit Object(QObject *parent = nullptr) : QObject(parent) {}
        virtual ~Object() override {};
};

int main(int argc, char *argv[])
{
    auto vec = new vector<unique_ptr<Object>>;
    vec->reserve(10'000);
    for(size_t i = 0; i < 10'000; ++i)
        vec->push_back(make_unique<Object>(nullptr));

    auto start_time = high_resolution_clock::now();
    //
    {
        delete vec;
    }
    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
    cout << elapsed_time;
    return 0;
}

#include "main.moc"