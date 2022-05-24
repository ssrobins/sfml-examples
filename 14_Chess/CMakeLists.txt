add_executable_custom(14_Chess)

target_sources(14_Chess PRIVATE
    main.cpp
)

target_assets(14_Chess
    assets
)

target_link_libraries(14_Chess
    sfml::sfml
)

install_executable(14_Chess)
