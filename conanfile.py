from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#724fce6f13f84579d39b6983af6213c414d69e7b")

    def requirements(self):
        self.requires("box2d/2.3.1#3d99c11e29b7110200931e5dae2db29319df2724")
        self.requires("sfml/2.5.1#5e5815201dee40ece40752baa972b905e719a5ed")
