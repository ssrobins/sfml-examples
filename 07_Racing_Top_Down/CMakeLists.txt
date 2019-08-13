add_executable_custom(07_Racing_Top_Down)

target_sources(07_Racing_Top_Down PRIVATE
    main.cpp
)

target_link_libraries(07_Racing_Top_Down
    CONAN_PKG::sfml
)

install_executable(07_Racing_Top_Down)
