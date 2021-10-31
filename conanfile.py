from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#2e2e0de4635e8c3a83655a207c63ad34ba1dadd7")

    def requirements(self):
        self.requires("box2d/2.3.1#c9e861a6615050fb060773f070123f48c8417033")
        self.requires("sfml/2.5.1#ada4c4c4ec7dfab4aed45311e4487aab625aca38")
