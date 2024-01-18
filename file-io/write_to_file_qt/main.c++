#include <QtCore/QDataStream>
#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <iostream>

using std::cout;
using std::endl;

int main(int argc, char *argv[])
{
    cout << "[Qt ] Starting 1'000'000 writes to file" << endl;
    QFile file("test.junk");
    file.open(QIODevice::WriteOnly | QIODevice::Truncate);
    QDataStream stream(&file);
    stream.setByteOrder(QDataStream::LittleEndian);

    uint64_t data = 0x0123456789abcdef;
    for(size_t i = 0; i < 1'000'000; ++i)
        stream << data;
    file.close();
    cout << "[Qt ] Done!" << endl;

    cout << "[Qt ] Cleaning up..." << endl;
    const auto res = QFile::remove("test.junk");
    if(not res)
       cout << "[Qt ] Failed to remove file!" << endl;
    else
       cout << "[Qt ] Done!" << endl;
    return 0;
}