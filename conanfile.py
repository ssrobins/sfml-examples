from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires.add("cmake_utils/0.3.1#1cf9333e6fba1b7350ec8d4d06f737b54d163eef")

    def requirements(self):
        self.requires.add("box2d/2.3.1#722f09428568a828755cbac453888cce327681c7")
        self.requires.add("sfml/2.5.1#658a32038bba095fa6bd3c48165321e0c9d90569")
