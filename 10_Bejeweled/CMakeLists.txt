add_executable_custom(10_Bejeweled)

target_sources(10_Bejeweled PRIVATE
    main.cpp
)

target_assets(10_Bejeweled
    assets
)

target_link_libraries(10_Bejeweled
    sfml::sfml
)

install_executable(10_Bejeweled)
