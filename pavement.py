# This is meant to be a generic Python builder for Holochain apps therefore
# it has option to include full runtime which is not needed for PyHoloWorld
# demonstration app DNA itself.

from paver.easy import *

@task
@cmdopts([
    ('runtime', 'r', 'Include Transcrypt runtime in app DNA'),
])
def build(options):
    functions = [
        '// Holochain functions for Transcrypted Python module',
        'var hc_property = property;',
        'var hc_get      = get;',
        'var hc_update   = update;',
        'var hc_commit   = commit;',
        ''
    ]
    runtime = polyfill = []
    if hasattr(options, 'runtime') and options.runtime:
        polyfill = ['// Using babel polyfill libraries for otto']
        polyfill += path('node_modules/babel-polyfill/dist/polyfill.js').lines()

    for dir in path('dna').dirs():
        for pyfile in dir.files('*.py'):
            sh('transcrypt -n -p .none ' + pyfile.relpath())
            jsfile = dir + '/__javascript__/' + pyfile.namebase + '.js'
            modfile = path(jsfile.relpath()[:-3] + '.mod.js')
            if hasattr(options, 'runtime') and options.runtime and not runtime:
                # Construct javascript runtime for otto
                runtime = polyfill[:]
                runtime.append('\n// Transcrypt runtime code for otto')
                for line in jsfile.lines()[3:]:
                    if line[1:2] == '(': break
                    runtime.append(line)
                runtime.append('\n// Transcrypted Python module for otto')

            modlines = []
            for line in modfile.lines()[2:]:
                if line[3:4] == '_': break
                modlines.append(line[2:])

            jsfile.write_lines(functions + runtime + modlines)

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
