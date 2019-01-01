#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Conan recipe package for libsolace
"""
from conans import ConanFile, CMake, tools


class SolaceConan(ConanFile):
    name = "solace"
    libname = "lib%s" % name
    version = "0.1"
    license = "Apache-2.0"
    author = "Ivan Ryabov <abbyssoul@gmail.com>"
    url = "https://github.com/abbyssoul/conan-%s" % libname
    homepage = "https://github.com/abbyssoul/%s" % libname
    description = "High performance components for mission critical applications"
    topics = ("HPC", "P10", "solace", "performance", "c++", "conan")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    src_url = "https://github.com/abbyssoul/%s" % libname

    def source(self):
#        git = tools.Git()
#        git.clone(self.src_url)
        self.run("git clone --depth 1 --recurse-submodules {}".format(self.src_url))
        self.run("cd %s" % self.libname)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.libname)
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="libsolace/include", keep_path=True)
        self.copy("*solace.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]

