from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#e474aafdec36cf92d97e781b844f390f3170f29f")

    def requirements(self):
        self.requires("box2d/2.3.1#2d87b135821108cab9473d63a7b67ad0b925bca3")
        self.requires("sfml/2.5.1#088b79f2ab521b0cf6cf5d745b862147b265b2d5")
