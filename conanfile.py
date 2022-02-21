from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/6.1.0#9ced9bcfd95178b35d2ec5955b725a5652dbda26")

    def requirements(self):
        self.requires("box2d/2.3.1#c5ab311eb0ab814da6173d00ced8dc187229a3e0")
        self.requires("sfml/2.5.1#7d6d90d08596afbb245ef8cc27809fea69851193")
