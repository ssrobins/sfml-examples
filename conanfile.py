from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        self.build_requires("cmake_utils/9.0.1#7f745054c87ea0007a89813a4d2c30c4c95e24b2")

    def requirements(self):
        self.requires("box2d/2.3.1#449fcf50a8576d57f1541acd4ce71298039ba282")
        self.requires("sfml/2.5.1#0e0eec0ebbdd0304915592e218ca25b2f48c7cff")
