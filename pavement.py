# This is meant to be a generic Python builder for Holochain apps therefore
# it has option to include full runtime which is not needed for PyHoloWorld
# demonstration app DNA itself.

from paver.easy import *

@task
@cmdopts([
    ('runtime', 'r', 'Include Transcrypt runtime in app DNA'),
])
def build(options):
    sh('transcrypt -n ui/*.py')
    sh('transcrypt -n -p .none dna/*/*.py')

    print('Modifying javascript for otto.')
    runtime = libraries = []
    if hasattr(options, 'runtime') and options.runtime:
        libraries = path('node_modules/string.prototype.startswith/startswith.js').lines()

    for dir in path('dna').dirs():
        for modfile in path(dir + '/__javascript__').files('*.mod.js'):
            jsfile = path(modfile.relpath()[:-7] + '.js')
            if hasattr(options, 'runtime') and options.runtime and not runtime:
                # Construct javascript runtime for otto
                runtime = libraries[:]
                runtime.append('\n// Transcrypt runtime code for otto: no bytearray support')
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

            modlines = []
            for line in modfile.lines()[2:]:
                if line[3] == '_': break
                modlines.append(line[2:])

            jsfile.write_lines(runtime + modlines)

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
