from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        self.build_requires("cmake_utils/9.0.1#7f745054c87ea0007a89813a4d2c30c4c95e24b2")

    def requirements(self):
        self.requires("box2d/2.3.1#246411ef22a5bd9a9526f74068e6f6acba420f72")
        self.requires("sfml/2.5.1#d75c42001d70f0cd03a0a967f7a69951d5672787")
