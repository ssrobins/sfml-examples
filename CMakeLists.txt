cmake_minimum_required(VERSION 3.25)

project(SFMLExamples VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_OPTIMIZE_DEPENDENCIES true)

if(APPLE)
    string(REGEX MATCH "[0-9]+\.[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
elseif(MSVC)
    string(REGEX MATCH "([0-9]+\.[0-9])([0-9])" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    string(REPLACE "." "" compiler_version ${CMAKE_MATCH_1})
    set(compiler_update ${CMAKE_MATCH_2})
else()
    string(REGEX MATCH "[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang" AND ${compiler_version} LESS 8)
        string(REGEX MATCH "[0-9]+\.[0-9]+" compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    endif()
endif()

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET 10.9)
    if(CMAKE_SYSTEM_PROCESSOR STREQUAL "arm64")
        set(conan_arch "armv8")
    else()
        set(conan_arch ${CMAKE_SYSTEM_PROCESSOR})
    endif()
    set(conan_args -s os=Macos -s arch=${conan_arch} -s os.version=${CMAKE_OSX_DEPLOYMENT_TARGET} -s compiler=apple-clang -s compiler.libcxx=libc++ -s compiler.version=${compiler_version} -s compiler.cppstd=${CMAKE_CXX_STANDARD})
elseif(UNIX)
    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        set(compiler clang)
    elseif(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        set(compiler gcc)
    else()
        message("Unhandled compiler, ${CMAKE_CXX_COMPILER_ID}, Conan install command may fail")
    endif()
    set(conan_args -s os=Linux -s arch=${CMAKE_SYSTEM_PROCESSOR} -s compiler=${compiler} -s compiler.version=${compiler_version} -s compiler.libcxx=libstdc++11 -s compiler.cppstd=${CMAKE_CXX_STANDARD})
elseif(MSVC)
    set(conan_args -s os=Windows -s arch=x86 -s compiler=msvc -s compiler.version=${compiler_version} -s compiler.update=${compiler_update} -s compiler.runtime=static -s compiler.cppstd=${CMAKE_CXX_STANDARD})
else()
    message("Unhandled platform, Conan install command may fail")
endif()

execute_process(
    COMMAND conan --version
    COMMAND_ECHO STDOUT
    ERROR_QUIET
    OUTPUT_VARIABLE conan_output
    RESULT_VARIABLE conan_result
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
if(conan_result)
    message(FATAL_ERROR "Conan not found, is it installed?")
elseif(conan_output MATCHES 1.)
    message(FATAL_ERROR "Conan 1.x found, you must install Conan 2.x.")
endif()

option(CONAN_BUILD_MISSING_PKGS "Build missing Conan packages" ON)
if(CONAN_BUILD_MISSING_PKGS)
    set(conan_build_option --build=missing)
endif()

set(conan_remote_name artifactory-ssrobins)
set(conan_remote_url https://ssrobins.jfrog.io/artifactory/api/conan/conan)
execute_process(
    COMMAND conan remote update ${conan_remote_name} --url ${conan_remote_url}
    COMMAND_ECHO STDOUT
    ERROR_QUIET
    RESULT_VARIABLE conan_result
)
if(conan_result)
    execute_process(
        COMMAND conan remote add ${conan_remote_name} ${conan_remote_url}
        COMMAND_ECHO STDOUT
        RESULT_VARIABLE conan_result
    )
    if(conan_result)
        message(FATAL_ERROR "Conan error")
    endif()
endif()

set(CMAKE_CONFIGURATION_TYPES "Debug;Release")
foreach(TYPE ${CMAKE_CONFIGURATION_TYPES})
    execute_process(
        COMMAND conan install --output-folder ${CMAKE_BINARY_DIR} --remote ${conan_remote_name} ${CMAKE_SOURCE_DIR} ${conan_build_option} ${conan_args} -s build_type=${TYPE} --profile:host ${CMAKE_SOURCE_DIR}/profile.jinja
        COMMAND_ECHO STDOUT
        RESULT_VARIABLE conan_result
    )
    if(conan_result)
        message(FATAL_ERROR "Conan error")
    endif()
endforeach()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG TRUE)
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
