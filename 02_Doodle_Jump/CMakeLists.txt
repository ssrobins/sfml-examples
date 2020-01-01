add_executable_custom(02_Doodle_Jump)

target_sources(02_Doodle_Jump PRIVATE
    main.cpp
)

target_assets(02_Doodle_Jump
    assets
)

target_link_libraries(02_Doodle_Jump
    CONAN_PKG::sfml
)

install_executable(02_Doodle_Jump)
