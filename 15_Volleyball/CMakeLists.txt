add_executable_custom(15_Volleyball)

target_sources(15_Volleyball PRIVATE
    main.cpp
)

target_assets(15_Volleyball
    assets
)

target_include_directories(15_Volleyball PRIVATE
    .
)

target_link_libraries(15_Volleyball
    box2d::box2d
    sfml::sfml
)

install_executable(15_Volleyball)
