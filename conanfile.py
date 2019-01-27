from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("box2d/2.3.1@stever/stable")
        self.requires.add("sfml/2.5.1@stever/stable")
