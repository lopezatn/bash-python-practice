
filename = "app.log"

try:
  file = open(filename, "r")
except FileNotFoundError:
    print(f"Error: {filename} not found")
    exit(1)
    
count = 0
for line in file:
  if "ERROR" in line:
    count += 1
    print(line)

print(count)
