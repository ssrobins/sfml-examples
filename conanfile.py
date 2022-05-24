from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package_multi"

    def build_requirements(self):
        self.build_requires("cmake_utils/8.0.0#b0932588b4ccd8ac8db4fed90295f7480ac0b37f")

    def requirements(self):
        self.requires("box2d/2.3.1#7be42ea3ee83f5e3d80d9b9513e11f15092e4f47")
        self.requires("sfml/2.5.1#1230d76d351f88b81dc25050e6e76f1a7e5d356c")
