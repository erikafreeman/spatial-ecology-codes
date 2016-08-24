#!/usr/bin/env python
from subprocess import Popen, call, check_output, STDOUT, PIPE

#### bash: ls -l
status = call('ls -l', shell=True)

status = call(['ls', '-l'])

#### bash: s=$(echo $USER)
s = check_output('echo $USER', shell=True).rstrip()
print s

# this does *not* work since "$USER" is substituted since shell is not used
s = check_output(['echo', '$USER']).rstrip()
print s

# to capture both stdout and stderr, set "stderr" option to "STDOUT"
s = check_output('echo $USER 1>&2', stderr=STDOUT, shell=True).rstrip()
print s

#### bash: ls | wc -l
p = Popen(['ls'], stdout=PIPE)
status = call(['wc', '-l'], stdin=p.stdout)
status = p.wait()

#### bash: ls | grep '\.sh$' wc -l
p1 = Popen(['ls'],                              stdout=PIPE)
p2 = Popen(['grep', '\\.py$'], stdin=p1.stdout, stdout=PIPE)
p3 = Popen(['wc', '-l'],       stdin=p2.stdout, stdout=PIPE)
s = p3.communicate()
print s
print s[0].strip()

#### bash: ls *.py
status = call('ls *.py', shell=True)

# this does *not* work since "*.py" is expanded by the shell, not "ls"
status = call(['ls', '*.py'])

# use glob module to expand "*.py"
import glob
status = call(['ls'] + glob.glob('*.py'))
