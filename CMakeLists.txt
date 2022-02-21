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
    set(conan_args -s os.version=${CMAKE_OSX_DEPLOYMENT_TARGET} -s compiler.version=${compiler_version} -s compiler.cppstd=${CMAKE_CXX_STANDARD})
elseif(UNIX)
    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        set(compiler clang)
    elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        set(compiler gcc)
    else()
        message("Unhandled compiler, ${CMAKE_CXX_COMPILER_ID}, Conan install command may fail")
    endif()
    set(conan_args -s compiler=${compiler} -s compiler.version=${compiler_version} -s compiler.libcxx=libstdc++11 -s compiler.cppstd=${CMAKE_CXX_STANDARD})
elseif(MSVC)
    set(conan_args -s arch=x86 -s compiler=msvc -s compiler.version=${compiler_version} -s compiler.runtime=static -s compiler.cppstd=${CMAKE_CXX_STANDARD})
else()
    message("Unhandled platform, Conan install command may fail")
endif()

option(CONAN_BUILD_MISSING_PKGS "Build missing Conan packages" ON)
if(CONAN_BUILD_MISSING_PKGS)
    set(conan_build_option --build=missing)
endif()

execute_process(
    COMMAND conan remote add artifactory-ssrobins https://ssrobins.jfrog.io/artifactory/api/conan/conan --insert --force
    COMMAND conan install --install-folder ${CMAKE_BINARY_DIR} --update ${CMAKE_SOURCE_DIR} ${conan_build_option} ${conan_args}
    RESULT_VARIABLE conan_result
)
if(conan_result)
    message(FATAL_ERROR "Conan error")
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

include(${CONAN_CMAKE_UTILS_ROOT}/global_settings.cmake)

# Helper functions
include(${CONAN_CMAKE_UTILS_ROOT}/add_executable_custom.cmake)
include(${CONAN_CMAKE_UTILS_ROOT}/install_executable.cmake)
include(${CONAN_CMAKE_UTILS_ROOT}/target_assets.cmake)

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
