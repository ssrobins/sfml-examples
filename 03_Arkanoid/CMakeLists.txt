add_executable_custom(03_Arkanoid)

target_sources(03_Arkanoid PRIVATE
    main.cpp
)

target_link_libraries(03_Arkanoid
    CONAN_PKG::sfml
)

install_executable(03_Arkanoid)
