from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("box2d/2.3.1#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
        self.requires("cmake_utils/9.0.1#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
        self.requires("sfml/2.5.1#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
