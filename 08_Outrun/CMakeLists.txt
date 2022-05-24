add_executable_custom(08_Outrun)

target_sources(08_Outrun PRIVATE
    main.cpp
)

target_assets(08_Outrun
    assets
)

target_link_libraries(08_Outrun
    sfml::sfml
)

install_executable(08_Outrun)
