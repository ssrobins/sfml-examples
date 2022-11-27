from conan import ConanFile

required_conan_version = ">=2.0.0-beta1"

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("box2d/2.3.1@ssrobins")
        self.requires("cmake_utils/12.0.1@ssrobins")
        self.requires("sfml/2.5.1@ssrobins")
