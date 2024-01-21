#include <chrono>
#include <iostream>
#include <QtCore/QCoreApplication>
#include <QtCore/QObject>

class Object : public QObject
{
    Q_OBJECT

    public:
        explicit Object(QObject *parent = nullptr) : QObject(parent) {}

        void setData(int x)
        {
            emit dataChanged(x);
        }

    signals:
        void dataChanged(int x);
};

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    using namespace std;
    using namespace chrono;
    auto start_time = high_resolution_clock::now();
    //
    {
        auto a = Object(nullptr);
        uint64_t sum = 0;
        QObject::connect(&a, &Object::dataChanged, [&sum](int x) { sum += x; });

        for(size_t i = 0; i < 10'000; ++i)
            a.setData(i);
    }
    auto end_time = high_resolution_clock::now();
    auto elapsed_time = duration_cast<microseconds>(end_time - start_time).count();
    cout << elapsed_time;
    //
    return a.exec();
}

#include "main.moc"