from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires.add("cmake_utils/0.1.0#89a9bc6923fea4dabf19de6aa6b7ddcf8667b2ee")

    def requirements(self):
        self.requires.add("box2d/2.3.1#18cbe3ca36efde484001aeca05edfa62cdc0bcfd")
        self.requires.add("sfml/2.5.1#63650f391c1574648fbf72b307fa9d35caf869b4")
