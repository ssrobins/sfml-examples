from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#da30d52b2c5db13fc90a22140f704d67c7635319")

    def requirements(self):
        self.requires("box2d/2.3.1#d638756bb131680839b33b0897f4b3f04f2ba938")
        self.requires("sfml/2.5.1#92f62cbb247c38f0cfe47511c6e2e6462de92801")
