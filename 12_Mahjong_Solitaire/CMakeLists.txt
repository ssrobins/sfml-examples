add_executable_custom(12_Mahjong_Solitaire)

target_sources(12_Mahjong_Solitaire PRIVATE
    main.cpp
)

target_assets(12_Mahjong_Solitaire
    assets
)

target_link_libraries(12_Mahjong_Solitaire
    sfml::sfml
)

install_executable(12_Mahjong_Solitaire)
