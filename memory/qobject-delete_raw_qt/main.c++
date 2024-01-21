#include <chrono>
#include <iostream>
#include <QtCore/QObject>
#include <QtCore/QVector>

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
    QVector<Object*> vec;
    vec.reserve(10'000);
    for(size_t i = 0; i < 10'000; ++i)
        vec.append(new Object(nullptr));

    auto start_time = high_resolution_clock::now();
    //
    {
        for(size_t i = 0; i < 10'000; ++i)
            delete vec[i];
    }
    //
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
    cout << elapsed_time;
    return 0;
}

#include "main.moc"