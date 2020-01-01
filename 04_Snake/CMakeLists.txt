add_executable_custom(04_Snake)

target_sources(04_Snake PRIVATE
    main.cpp
)

target_assets(04_Snake
    assets
)

target_link_libraries(04_Snake
    CONAN_PKG::sfml
)

install_executable(04_Snake)
