# PyHoloWorld
Basic Hello World app for Holochain ported to Python

Please see original code at https://github.com/holochain/HoloWorld

To compile this Python code for Holochain, you will need to install Transcrypt
and Paver.

https://www.transcrypt.org/

https://pythonhosted.org/Paver/

Before building anything you also need to run 'npm install' in order to obtain
additional required Javascript libraries.

After that just run 'make' and it should build.

Then 'hcdev test' and 'hcdev web' should work without any problem.
