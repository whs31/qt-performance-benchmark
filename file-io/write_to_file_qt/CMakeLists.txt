cmake_minimum_required(VERSION 3.25)
project(write_to_file)

set(CMAKE_CXX_FLAGS_RELEASE "-O3")

find_package(QT NAMES Qt6 Qt5 COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core)

add_executable(${PROJECT_NAME} main.c++)
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME "out.out")
target_link_libraries(${PROJECT_NAME} Qt${QT_VERSION_MAJOR}::Core)