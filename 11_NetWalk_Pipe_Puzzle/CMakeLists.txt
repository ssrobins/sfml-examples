add_executable_custom(11_NetWalk_Pipe_Puzzle)

target_sources(11_NetWalk_Pipe_Puzzle PRIVATE
    main.cpp
)

target_link_libraries(11_NetWalk_Pipe_Puzzle
    CONAN_PKG::sfml
)

install_executable(11_NetWalk_Pipe_Puzzle)
