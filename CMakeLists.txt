cmake_minimum_required(VERSION 3.13.0)

project(Rectangles)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

include(cmake/global_settings.cmake)

# Helper functions
include(cmake/add_executable_custom.cmake)
include(cmake/install_executable.cmake)

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

include(CPack)
