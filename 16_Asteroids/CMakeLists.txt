add_executable_custom(16_Asteroids)

target_sources(16_Asteroids PRIVATE
    main.cpp
)

target_assets(16_Asteroids
    assets
)

target_link_libraries(16_Asteroids
    CONAN_PKG::sfml
)

install_executable(16_Asteroids)
