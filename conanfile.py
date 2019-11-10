"""Conan recipe package for libsolace
"""
from conans import ConanFile, CMake, tools


class LibsolaceConan(ConanFile):
    name = "libsolace"
    version = "0.3.7"
    license = "Apache-2.0"
    author = "Ivan Ryabov <abbyssoul@gmail.com>"
    url = "https://github.com/abbyssoul/conan-%s.git" % name
    homepage = "https://github.com/abbyssoul/%s" % name
    description = "High performance components for mission critical applications"
    topics = ("HPC", "High reliability", "P10", "solace", "performance", "c++", "conan")
    
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
#        git = tools.Git()
#        git.clone(self.homepage)
        self.run("git clone --branch v{} --depth 1 --recurse-submodules {}".format(self.version, self.homepage))

    def _configure_cmake(self):
        cmake = CMake(self, parallel=True)
        #cmake.definitions["PKG_CONFIG"] = "OFF"
        #cmake.definitions["SOLACE_GTEST_SUPPORT"] = "OFF"
        #cmake.configure(source_folder=self._source_subfolder)
        cmake.configure(source_folder=self.name)
        return cmake
    
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        # cmake.test(target="test_solace") Don't waste time building tests

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy(pattern="LICENSE", dst="licenses", src=self.name)
        
        #self.copy("*.hpp", dst="include", src="include")
        #self.copy("*.lib", dst="lib", keep_path=False)
        #self.copy("*.dll", dst="bin", keep_path=False)
        #self.copy("*.dylib*", dst="lib", keep_path=False)
        #self.copy("*.so", dst="lib", keep_path=False)
        #self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["solace"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("m")

