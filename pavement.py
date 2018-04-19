from paver.easy import *

@task
def build():
    sh('transcrypt -n ui/*.py')
    sh('transcrypt -n -p .none dna/*/*.py')

    print('Modifying javascript for otto.')
    startswith = path('node_modules/string.prototype.startswith/startswith.js').lines()
    runtime = None

    for dir in path('dna').dirs():
        for modfile in path(dir + '/__javascript__').files('*.mod.js'):
            modlines = []
            for line in modfile.lines()[2:]:
                if line[3] == '_': break
                modlines.append(line[2:])

            jsfile = path(modfile.relpath()[:-7] + '.js')
            if not runtime: # Construct javascript runtime for otto
                runtime = startswith[:] # required library
                runtime.append("\n// Transcrypt runtime code for otto: no bytearray support")
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

            jsfile.write_lines(runtime + modlines)

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
