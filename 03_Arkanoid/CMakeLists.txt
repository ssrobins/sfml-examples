add_executable_custom(03_Arkanoid)

target_sources(03_Arkanoid PRIVATE
    main.cpp
)

target_assets(03_Arkanoid
    assets
)

target_link_libraries(03_Arkanoid
    sfml::sfml
)

install_executable(03_Arkanoid)
