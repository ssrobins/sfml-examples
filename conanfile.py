from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#30236679ffe9804515e8c092a744560a72ffb55a")

    def requirements(self):
        self.requires("box2d/2.3.1#3e39d20dd892c780cd11e7195b9198a6744ed997")
        self.requires("sfml/2.5.1#420eac2b0101a98c69a577569f9d3a509e2d05e1")
