#! /usr/bin/python

import subprocess

MAILMAN_HOME = "/usr/lib/mailman/bin/"

def execute(cmd):
    cmd = MAILMAN_HOME + cmd
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    outs = out.splitlines()
    return outs


# get list names
outs = execute("list_lists")
lists = []
for line in outs[1:]:
    words = line.split()
    lists.append(words[0])


for list in lists:
    print list
    members = execute("list_members " + list)
    for member in members:
        print member
    print
