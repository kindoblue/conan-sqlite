from conans import ConanFile
import os, shutil
from conans.tools import download, unzip, check_sha256
from conans import CMake

class SQLite3Conan(ConanFile):
    name = "sqlite3"
    version = "3.10.2"
    license = "Public domain"
    description = "SQLite library"
    settings = "os", "compiler", "arch", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    url="https://github.com/kindoblue/conan-sqlite.git"
    exports = ["CMakeLists.txt"]
    ZIP_FOLDER_NAME = "sqlite-amalgamation-3100200"

    def source(self):
        zip_name = "sqlite-amalgamation-3100200.zip"
        download("http://www.sqlite.org/2016/%s" % zip_name, zip_name)
        check_sha256(zip_name, "b68adfb8cfd0ba5712e0ed8346929538ceb9125d6de4d15049db56201ac794f6")
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.ZIP_FOLDER_NAME)
        cmake = CMake(self.settings)
        
        self.run("mkdir _build")
        self.run('cd _build && cmake ../%s %s' % (self.ZIP_FOLDER_NAME, cmake.command_line))
        self.run("cd _build && cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", "include", "%s" % (self.ZIP_FOLDER_NAME), keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.so", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.pdb", dst="lib", src="_build", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['sqlite3']
        if not self.settings.os == "Windows":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")
