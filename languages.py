import os
import util
from subprocess import call


class Language():
    def __init__(self, title, names, folder_name):
        self.title = title
        self.names = names

    def getStyledName(self, n):
        # Camel case formatting is default
        return util.toCamelCase(n)

    def create(self, name, dir):
        pass  # Do nothing


class PythonLanguage(Language):
    def __init__(self):
        self.title = 'Python'
        self.names = ['python', 'py']
        self.folder_name = 'Python'

    def create(self, name, dir):
        f = open(os.path.join(dir, 'main.py'), 'w')
        f.write("# Insert code here :)")
        f.close()


class CLanguage(Language):
    def __init__(self):
        self.title = 'C'
        self.names = ['c']
        self.folder_name = 'C'

    def create(self, name, dir):
        srcdir = os.path.join(dir, 'src')
        os.mkdir(srcdir)
        incdir = os.path.join(dir, 'include')
        os.mkdir(incdir)
        builddir = os.path.join(dir, 'build')
        os.mkdir(builddir)

        f = open(os.path.join(srcdir, 'main.c'), 'w')
        f.write("#include <stdio.h>\n" +
                "\n" +
                "int main(int argc, char** argv)\n" +
                "{\n" +
                "   printf(\"Hello World.\\n\");\n" +
                "   return 0;\n" +
                "}")
        f.close()

        f = open(os.path.join(dir, 'CMakeLists.txt'), 'w')
        f.write("cmake_minimum_required (VERSION 2.6)\n" +
                "project ({})\n".format(name) +
                "\n" +
                "file(GLOB {}_SRC\n".format(name) +
                "    \"src/*.c\"\n" +
                ")\n" +
                "\n" +
                "include_directories(include)\n" +
                "\n" +
                "file(GLOB {}_INC\n".format(name) +
                "    \"include/*.h\"\n" +
                ")\n" +
                "\n" +
                'add_executable(' + name + ' ${' + name + '_SRC} ${' + name + '_INC})\n')
        f.close()

    def getStyledName(self, n):
        return util.toSnakeCase(n)


class LuaLanguage(Language):
    def __init__(self):
        self.title = 'Lua'
        self.names = ['lua']
        self.folder_name = 'Lua'

    def create(self, name, dir):
        f = open(os.path.join(dir, 'main.lua'), 'w')
        f.write("--Insert code here")
        f.close()


class JavaLanguage(Language):
    def __init__(self):
        self.title = 'Java'
        self.names = ['java']
        self.folder_name = 'Java'

    def create(self, name, dir):
        f = open(os.path.join(dir, "{}.java".format(name)), 'w')
        f.write(
            'public class {}'.format(name) + ' {\n'
            '\n' +
            '    public static void main(String[] args) {\n' +
            '        System.out.println("Hello World.");\n' +
            '    }\n' +
            '}\n'
        )
        f.close()


class RubyLanguage(Language):
    def __init__(self):
        self.title = 'Ruby'
        self.names = ['ruby']
        self.folder_name = 'Ruby'

    def create(self, name, dir):
        f = open(os.path.join(dir, "main.rb".format(name)), 'w')
        f.write(
            '#!/usr/bin/ruby -w\n' +
            '\n' +
            'puts "Hello World."\n'
        )
        f.close()

    def getStyledName(self, n):
        return util.toSnakeCase(n)


class NodeJSLanguage(Language):
    def __init__(self):
        self.title = 'NodeJS'
        self.names = ['nodejs', 'node']
        self.folder_name = 'NodeJS'

    def create(self, name, dir):
        f = open(os.path.join(dir, "main.js".format(name)), 'w')
        f.write(
            'console.log("Hello World");\n'
        )
        f.close()

        # Run 'npm init' in folder
        pdir = os.getcwd()  # Store previous directory

        os.chdir(dir)
        call(['npm', 'init'])

        os.chdir(pdir)  # Go back to previous directory

    def getStyledName(self, n):
        return util.toKebabCase(n)


all = [
    PythonLanguage(),
    CLanguage(),
    LuaLanguage(),
    JavaLanguage(),
    RubyLanguage(),
    NodeJSLanguage()
]


def get(name):
    for lang in all:
        if name.lower() in lang.names:
            return lang
    return None


def get_language_from_user():
    print(' -- Language Selection --')
    l = None
    while l == None:
        for lang in all:
            print(" * {} ({})".format(lang.title, ','.join(lang.names)))
        name = input(": ")
        l = get(name)

        if l == None:
            print("Invalid Language. Please enter a language from the list:\n")
    return l
