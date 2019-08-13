add_executable_custom(15_Volleyball)

target_sources(15_Volleyball PRIVATE
    main.cpp
)

target_include_directories(15_Volleyball PRIVATE
    .
)

target_link_libraries(15_Volleyball
    CONAN_PKG::box2d
    CONAN_PKG::sfml
)

install_executable(15_Volleyball)
