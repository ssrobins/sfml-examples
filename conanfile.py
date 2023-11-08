from conan import ConanFile

required_conan_version = ">=2.0.4"

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"
    default_options = {
        "sfml/*:audio": False,
        "sfml/*:graphics": True,
        "sfml/*:network": False,
        "sfml/*:window": True,
    }

    def requirements(self):
        self.requires("box2d/2.3.1")
        self.requires("sfml/2.6.1")
