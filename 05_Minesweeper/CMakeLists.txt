add_executable_custom(05_Minesweeper)

target_sources(05_Minesweeper PRIVATE
    main.cpp
)

target_link_libraries(05_Minesweeper
    CONAN_PKG::sfml
)

install_executable(05_Minesweeper)
