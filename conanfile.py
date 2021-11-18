from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/2.0.1#bc87acc9a67867fb20e22e3c51eb4c070a9f9758")

    def requirements(self):
        self.requires("box2d/2.3.1#8d35fff9bc17cf629dd8fab8babc2a3f7cdc3228")
        self.requires("sfml/2.5.1#f57c2ff1310d9691428e0149cdd1c4ed7768a739")
