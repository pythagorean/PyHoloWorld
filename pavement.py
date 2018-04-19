from paver.easy import *

@task
def build():
    sh('transcrypt -n ui/*.py')
    sh('transcrypt -n -p .none dna/*/*.py')
    print('Modifying javascript for otto.')
    startswith = path('node_modules/string.prototype.startswith/startswith.js').lines()
    for dir in path('dna').dirs():
        for infile in path(dir + '/__javascript__').files('*.mod.js'):
            inlines = []
            for line in infile.lines()[2:]:
                if line[3] == '_': break
                inlines.append(line[2:])
            runtime = startswith
            runtime.append("\n// Transcrypt runtime code for otto: no bytearray support")
            jsfile = path(infile.relpath()[:-7] + '.js')
            strip = False
            for line in jsfile.lines()[3:]:
                if line[1:2] == '(': break
                if line[4:22] == "function bytearray":
                    strip = True
                if strip and line[4:16] == "function str":
                    strip = False
                if not strip:
                    runtime.append(line)
            runtime.append('\n// Transcrypted Python module for otto')
            jsfile.write_lines(runtime + inlines)

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
