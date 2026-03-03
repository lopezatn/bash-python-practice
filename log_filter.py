import sys

if len(sys.argv) < 3:
    print("Missing one or more arguments")
    exit(1)

filename = sys.argv[1]
keyword = sys.argv[2]

with open(filename) as f:
    for line in f:
        if keyword in line:
            print(line.strip())

