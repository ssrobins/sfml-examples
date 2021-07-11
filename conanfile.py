from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#77d5f06b9b20302a5410e41ed45e7bbea7de90a5")

    def requirements(self):
        self.requires("box2d/2.3.1#2640730b74de43c61ce2c6f209c570b2b05ceeec")
        self.requires("sfml/2.5.1#60a8805c66f3d2339b63a6b14c7203e564b36955")
