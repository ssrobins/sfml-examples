cmake_minimum_required(VERSION 3.25)

list(APPEND CONAN_INSTALL_ARGS
    "--build=missing"
    "--conf=tools.system.package_manager:mode=install"
    "--conf=tools.system.package_manager:sudo=True"
    "--conf=tools.cmake.cmaketoolchain:generator=Ninja Multi-Config"
)

option(CONAN_UPDATE "Check for newer Conan packages" OFF)
if(CONAN_UPDATE)
    list(APPEND CONAN_INSTALL_ARGS "--update")
endif()

set(conan_provider_file "${CMAKE_BINARY_DIR}/conan_provider.cmake")
if(NOT EXISTS "${conan_provider_file}")
    message(STATUS "Downloading conan_provider.cmake")
    file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/develop2/conan_provider.cmake"
        "${conan_provider_file}"
        TLS_VERIFY ON)
endif()
set(CMAKE_PROJECT_TOP_LEVEL_INCLUDES "${conan_provider_file}")

project(SFMLExamples VERSION 0.1.0)

include(cmake/global_settings.cmake)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_OPTIMIZE_DEPENDENCIES true)

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET 10.13)
endif()

set(CMAKE_CONFIGURATION_TYPES "Debug;Release")

find_package(box2d REQUIRED)
find_package(SFML REQUIRED)

# Helper functions
include(cmake/add_executable_custom.cmake)
include(cmake/install_executable.cmake)
include(cmake/target_assets.cmake)

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
