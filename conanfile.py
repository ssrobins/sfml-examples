from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("box2d/2.3.1#a0215989fbf5f43230376a078b276eaa8b3d4474")
        self.requires.add("sfml/2.5.1#820f9ee26eecf951975a053826974787eab9ac82")
