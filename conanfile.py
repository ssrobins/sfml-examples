from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#b92e3b563e31a4fe0e55849f3bfdb55eb7b06284")

    def requirements(self):
        self.requires("box2d/2.3.1#b586f22f2ab041a221c3767ac1f9312ea0f6f318")
        self.requires("sfml/2.5.1#1692035d8d7096e9c6c8a96dd3500d77b2c1595d")
