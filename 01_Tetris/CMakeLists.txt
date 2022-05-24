add_executable_custom(01_Tetris)

target_sources(01_Tetris PRIVATE
    main.cpp
)

target_assets(01_Tetris
    assets
)

target_link_libraries(01_Tetris
    sfml::sfml
)

install_executable(01_Tetris)
