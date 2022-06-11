cmake_minimum_required(VERSION 3.21)

project(SFMLExamples VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(APPLE)
    string(REGEX MATCH "[0-9]+\.[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
elseif(MSVC)
    string(REGEX MATCH "[0-9]+\.[0-9]" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    string(REPLACE "." "" compiler_version ${compiler_version})
else()
    string(REGEX MATCH "[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang" AND ${compiler_version} LESS 8)
        string(REGEX MATCH "[0-9]+\.[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    endif()
endif()

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET 10.9)
    set(conan_args os.version=${CMAKE_OSX_DEPLOYMENT_TARGET};compiler=apple-clang;compiler.libcxx=libc++;compiler.version=${compiler_version};compiler.cppstd=${CMAKE_CXX_STANDARD})
elseif(UNIX)
    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        set(compiler clang)
    elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        set(compiler gcc)
    else()
        message("Unhandled compiler, ${CMAKE_CXX_COMPILER_ID}, Conan install command may fail")
    endif()
    set(conan_args os=Linux;arch=${CMAKE_SYSTEM_PROCESSOR};compiler=${compiler};compiler.version=${compiler_version};compiler.libcxx=libstdc++11;compiler.cppstd=${CMAKE_CXX_STANDARD})
    set(conan_profile_host ${CMAKE_SOURCE_DIR}/profiles/linux)
elseif(MSVC)
    set(conan_args arch=x86;compiler=msvc;compiler.version=${compiler_version};compiler.runtime=static;compiler.cppstd=${CMAKE_CXX_STANDARD})
else()
    message("Unhandled platform, Conan install command may fail")
endif()

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD
        "https://raw.githubusercontent.com/conan-io/cmake-conan/0.18.1/conan.cmake"
        "${CMAKE_BINARY_DIR}/conan.cmake"
        TLS_VERIFY ON)
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

option(CONAN_BUILD_MISSING_PKGS "Build missing Conan packages" ON)
if(CONAN_BUILD_MISSING_PKGS)
    set(conan_build_option missing)
endif()

conan_add_remote(NAME artifactory-ssrobins
    INDEX 0
    URL https://ssrobins.jfrog.io/artifactory/api/conan/conan
    VERIFY_SSL True)

set(CMAKE_CONFIGURATION_TYPES "Debug;Release")
foreach(TYPE ${CMAKE_CONFIGURATION_TYPES})
    conan_cmake_install(PATH_OR_REFERENCE ${CMAKE_SOURCE_DIR}
        BUILD ${conan_build_option}
        UPDATE
        SETTINGS ${conan_args};build_type=${TYPE}
        PROFILE_HOST ${conan_profile_host})
endforeach()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})
set(CMAKE_FIND_ROOT_PATH ${CMAKE_BINARY_DIR})

find_package(box2d REQUIRED)
find_package(cmake_utils REQUIRED)
find_package(sfml REQUIRED)

include(${cmake_utils_PACKAGE_FOLDER_RELEASE}/global_settings.cmake)

# Helper functions
include(${cmake_utils_PACKAGE_FOLDER_RELEASE}/add_executable_custom.cmake)
include(${cmake_utils_PACKAGE_FOLDER_RELEASE}/install_executable.cmake)
include(${cmake_utils_PACKAGE_FOLDER_RELEASE}/target_assets.cmake)

# From 16 games in C++/SFML YouTube tutorial:
# https://www.youtube.com/user/FamTrinli/playlists

add_subdirectory(01_Tetris)
add_subdirectory(02_Doodle_Jump)
add_subdirectory(03_Arkanoid)
add_subdirectory(04_Snake)
add_subdirectory(05_Minesweeper)
add_subdirectory(06_Fifteen-Puzzle)
add_subdirectory(07_Racing_Top_Down)
add_subdirectory(08_Outrun)
add_subdirectory(09_Xonix)
add_subdirectory(10_Bejeweled)
add_subdirectory(11_NetWalk_Pipe_Puzzle)
add_subdirectory(12_Mahjong_Solitaire)
add_subdirectory(13_Tron)
if(WIN32)
    add_subdirectory(14_Chess)
endif()
add_subdirectory(15_Volleyball)
add_subdirectory(16_Asteroids)

set(CPACK_ARCHIVE_COMPONENT_INSTALL ON)
set(CPACK_PACKAGE_FILE_NAME ${CMAKE_PROJECT_NAME})
include(CPack)
