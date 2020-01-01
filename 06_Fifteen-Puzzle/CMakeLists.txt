add_executable_custom(06_Fifteen-Puzzle)

target_sources(06_Fifteen-Puzzle PRIVATE
    main.cpp
)

target_assets(06_Fifteen-Puzzle
    assets
)

target_link_libraries(06_Fifteen-Puzzle
    CONAN_PKG::sfml
)

install_executable(06_Fifteen-Puzzle)
