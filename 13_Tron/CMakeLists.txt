add_executable_custom(13_Tron)

target_sources(13_Tron PRIVATE
    main.cpp
)

target_assets(13_Tron
    assets
)

target_link_libraries(13_Tron
    sfml::sfml
)

install_executable(13_Tron)
