from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("box2d/2.3.1#f374feb3c060e091bdaf0a0005dd64c28ed04c67")
        self.requires("cmake_utils/10.0.1#f374feb3c060e091bdaf0a0005dd64c28ed04c67")
        self.requires("sfml/2.5.1#f374feb3c060e091bdaf0a0005dd64c28ed04c67")
