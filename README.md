# PyHoloWorld
Basic Hello World app for Holochain ported to Python

Please see original code at https://github.com/holochain/HoloWorld

To compile this Python code for Holochain, you will need to install Transcrypt
and Paver.

https://www.transcrypt.org/

https://pythonhosted.org/Paver/

After that just run 'make' and it should build.

Then 'hcdev test' and 'hcdev web' should work without any problem.

If you wish to modify the app DNA in a way that requires inclusion of the
Python runtime, modify Makefile accordingly to build with 'paver -q build -r'
and run 'npm install' or 'yarn' to obtain needed libraries.
