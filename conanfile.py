from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires.add("cmake_utils/0.3.1#1cf9333e6fba1b7350ec8d4d06f737b54d163eef")

    def requirements(self):
        self.requires.add("box2d/2.3.1#18cbe3ca36efde484001aeca05edfa62cdc0bcfd")
        self.requires.add("sfml/2.5.1#63650f391c1574648fbf72b307fa9d35caf869b4")
