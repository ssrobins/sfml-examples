add_executable_custom(09_Xonix)

target_sources(09_Xonix PRIVATE
    main.cpp
)

target_assets(09_Xonix
    assets
)

target_link_libraries(09_Xonix
    sfml::sfml
)

install_executable(09_Xonix)
