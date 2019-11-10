from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires.add("cmake_utils/0.1.0#89a9bc6923fea4dabf19de6aa6b7ddcf8667b2ee")

    def requirements(self):
        self.requires.add("box2d/2.3.1#dc184ca0366ec14bd0e85f8b21b1e32f46a570d4")
        self.requires.add("sfml/2.5.1#ce4fde128151ffee338a5de73c6fff1e9f0d2d1f")
