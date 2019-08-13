add_executable_custom(12_Mahjong_Solitaire)

target_sources(12_Mahjong_Solitaire PRIVATE
    main.cpp
)

target_link_libraries(12_Mahjong_Solitaire
    CONAN_PKG::sfml
)

install_executable(12_Mahjong_Solitaire)
