from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#77d5f06b9b20302a5410e41ed45e7bbea7de90a5")

    def requirements(self):
        self.requires("box2d/2.3.1#5818ed1c3a8557baaf3ac244553c4aaf1987458c")
        self.requires("sfml/2.5.1#9e7d536ae87aa4d222de81824ad84049aede3646")
