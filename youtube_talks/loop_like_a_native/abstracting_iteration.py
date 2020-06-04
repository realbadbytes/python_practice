# text file can have blank lines or commented lines, want to ignore both
f = open("my_config.ini")
for line in f:
    line = line.strip()
    if line.startswith('#')
        continue
    if not line:
        continue
    do_something(line)

# a much better approach
# 1, f is an iterable
# strongly note: this means it can be tested with lists of strings, 
# since strings are also iterable
def interesting_lines(f):
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line

with open("my_config.ini") as f:
    for line in interesting_lines(f):
        do_something(line)

with open("my_other.dat") as f2:
    for line in interesting_lines(f2):
        do_something_else(line)

# abstracted iteration is more testable and applicable than just a file parser

