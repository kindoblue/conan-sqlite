from conans.model.conan_file import ConanFile
from conans import CMake
import os

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "sqlite3/3.10.2@kindoblue/stable"

    def imports(self):
        self.copy("*.so", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake ../.. %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)
 
    def test(self):
        os.chdir("bin")
        self.run(".%stest " % os.sep)
