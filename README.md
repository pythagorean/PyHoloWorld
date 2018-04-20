# PyHoloWorld
Basic Hello World app for Holochain ported to Python

Please see original code at https://github.com/holochain/HoloWorld

To compile this Python code for Holochain, you will first need to install
[Transcrypt](https://www.transcrypt.org) and [Paver](https://pythonhosted.org/Paver).

    pip install transcrypt
    pip install paver

After that just run 'make' and it should build.

Then 'hcdev test' and 'hcdev web' should work without any problem.

If you wish to modify the app DNA in a way that requires inclusion of the
Python runtime, modify Makefile accordingly to build with 'paver -q build -r'
and run 'npm install' or 'yarn' to obtain needed libraries.
