add_executable_custom(14_Chess)

target_sources(14_Chess PRIVATE
    main.cpp
)

target_link_libraries(14_Chess
    CONAN_PKG::sfml
)

install_executable(14_Chess)
