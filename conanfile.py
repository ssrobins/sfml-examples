from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#09e87aa7b71951c0c77bbf861baaaa53c3d55830")

    def requirements(self):
        self.requires("box2d/2.3.1#93687d2584f85a3e93c809130ccfd96338317c48")
        self.requires("sfml/2.5.1#c901ae398dce47f27ff68f0177831d64e3c894a1")
