from paver.easy import *

@task
def build():
    sh('transcrypt -n ui/*.py')
    sh('transcrypt -n -p .none dna/*/*.py')
    runtime = path('python-runtime.js').lines()
    for dir in path('dna').dirs():
        for infile in path(dir + '/__javascript__').files('*.mod.js'):
            inlines = []
            for line in infile.lines()[2:]:
                if line[3] == '_': break
                inlines.append(line[2:])
            outfile = path(infile.relpath()[:-7] + '.js')
            outfile.write_lines(runtime + ['\n'] + inlines)

@task
def clean():
    sh('for x in `find . -name "__javascript__"`; do rm -rf $x; done')
