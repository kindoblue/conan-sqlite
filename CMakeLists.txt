project(sqlite3)
cmake_minimum_required(VERSION 2.8)
include(../conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

if(BUILD_SHARED_LIBS)
    set(LIB_MODE STATIC)
    message(STATUS "[sse] Building static library")
else(BUILD_SHARED_LIBS)
    set(LIB_MODE SHARED)
    message(STATUS "[sse] Building shared library")
endif(BUILD_SHARED_LIBS)

add_library(sqlite3 ${LIB_MODE} sqlite3.c)
