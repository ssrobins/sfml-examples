from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("cmake_utils/0.3.1#a1d53d179d9736ff032b5f5de3e4c3e2eebcb1f0")

    def requirements(self):
        self.requires("box2d/2.3.1#c9ad941f2cc9b02c162942cc6af9859e6397ed05")
        self.requires("sfml/2.5.1#68c0f11697a80f04e14b505cfba7610b028b9d9f")
