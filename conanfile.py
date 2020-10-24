from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#cc144db607f04d12c0b18303a7c7d37386ce0783")

    def requirements(self):
        self.requires("box2d/2.3.1#e86e6c95a7193c4654700665f93ea446969c711f")
        self.requires("sfml/2.5.1#53b19f48090b9597c7b7bf76ae29e8e80df924e7")
