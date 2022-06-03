from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        self.build_requires("cmake_utils/9.0.1#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")

    def requirements(self):
        self.requires("box2d/2.3.1#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")
        self.requires("sfml/2.5.1#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")
