add_executable_custom(01_Tetris)

target_sources(01_Tetris PRIVATE
    main.cpp
)

target_link_libraries(01_Tetris
    CONAN_PKG::sfml
)

install_executable(01_Tetris)
