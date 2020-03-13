from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#bddead915084dbfac2b4114574fae5ae8545e540")

    def requirements(self):
        self.requires("box2d/2.3.1#9699e70bd278099f8da60ae508796a598ce159dd")
        self.requires("sfml/2.5.1#b0d57764841bf37146f6d7c4ed3f2a18ae85ccc7")
