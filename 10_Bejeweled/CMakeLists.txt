add_executable_custom(10_Bejeweled)

target_sources(10_Bejeweled PRIVATE
    main.cpp
)

target_link_libraries(10_Bejeweled
    CONAN_PKG::sfml
)

install_executable(10_Bejeweled)
