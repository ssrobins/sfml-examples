set(target_name 15_Volleyball)

add_executable_custom(${target_name})

target_sources(${target_name} PRIVATE
    main.cpp
)

target_include_directories(${target_name} PRIVATE
    .
)

target_link_libraries(${target_name}
    CONAN_PKG::box2d
    CONAN_PKG::sfml
)

install_executable(${target_name})
