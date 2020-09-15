# this is a script that run in terminal
# it run test.py according to the range that has been set
# text.py will be run and show the output

import subprocess

for i in range(0, 5):
    subprocess.check_call(['python', 'test.py'])