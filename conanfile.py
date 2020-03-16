from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#d093c585be2418d6a664babbec39e71d6b5cd11d")

    def requirements(self):
        self.requires("box2d/2.3.1#9fd12e5cf8e69edd2f7e09f9418fee94e8cba1e3")
        self.requires("sfml/2.5.1#4b78df7e663f416c531bc5ee5e3cfd92a555c1f6")
