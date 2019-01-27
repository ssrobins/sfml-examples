set(target_name 16_Asteroids)

add_executable_custom(${target_name})

target_sources(${target_name} PRIVATE
    main.cpp
)

target_link_libraries(${target_name}
    CONAN_PKG::sfml
)

install_executable(${target_name})
