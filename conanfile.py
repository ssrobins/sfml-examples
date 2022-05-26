from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        self.build_requires("cmake_utils/9.0.1#7f745054c87ea0007a89813a4d2c30c4c95e24b2")

    def requirements(self):
        self.requires("box2d/2.3.1#7be42ea3ee83f5e3d80d9b9513e11f15092e4f47")
        self.requires("sfml/2.5.1#1230d76d351f88b81dc25050e6e76f1a7e5d356c")
