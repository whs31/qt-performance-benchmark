#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <filesystem>

using namespace std;

auto main() -> int
{
    cout << "[C++] Starting 1'000'000 writes to file" << endl;
    ofstream stream("test.junk", std::ios::binary | std::ios::trunc);
    uint64_t data = 0x0123456789abcdef;
    for(size_t i = 0; i < 1'000'000; ++i)
        stream.write(reinterpret_cast<char*>(&data), sizeof(uint64_t));

    stream.close();
    cout << "[C++] Done!" << endl;

    cout << "[C++] Cleaning up..." << endl;
    const auto res = filesystem::remove(filesystem::path("test.junk"));
    if(not res)
       cerr << "[C++] Failed to remove file!" << endl;
    else
       cout << "[C++] Done!" << endl;
    return 0;
}