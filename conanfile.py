from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#77d5f06b9b20302a5410e41ed45e7bbea7de90a5")

    def requirements(self):
        self.requires("box2d/2.3.1#00a7a8fbcd0665f2e547aab9d6acdaf73aafe0fd")
        self.requires("sfml/2.5.1#14616b0363a0677811713e413226212e46e44bf0")
