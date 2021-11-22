from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/3.0.0#4e7b4d9bfca394477325cdfc8eacce8b1c82583e")

    def requirements(self):
        self.requires("box2d/2.3.1#c578e6a30b02cb10d4195b7d1d8798a47d604f37")
        self.requires("sfml/2.5.1#69412c151d6eef5d35cea61894bb72b4da33d29c")
