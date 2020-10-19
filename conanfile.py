from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#cc144db607f04d12c0b18303a7c7d37386ce0783")

    def requirements(self):
        self.requires("box2d/2.3.1#e259c69dc653c346b70350d21113a2adaad72079")
        self.requires("sfml/2.5.1#cd092e0ab5f37bceb1601ea5021068a84afd934c")
