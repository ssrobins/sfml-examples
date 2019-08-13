add_executable_custom(08_Outrun)

target_sources(08_Outrun PRIVATE
    main.cpp
)

target_link_libraries(08_Outrun
    CONAN_PKG::sfml
)

install_executable(08_Outrun)
