add_executable_custom(02_Doodle_Jump)

target_sources(02_Doodle_Jump PRIVATE
    main.cpp
)

target_assets(02_Doodle_Jump
    assets
)

target_link_libraries(02_Doodle_Jump
    sfml::sfml
)

install_executable(02_Doodle_Jump)
