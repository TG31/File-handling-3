# Exercise 1
def read_line(filename, line_number):
    file = open(filename, "r")
    if line_number <= 0:
        file.close()
        return ""
    for i in range(line_number):
        line = file.readline()
        if line == "":
            file.close()
            return ""
    file.close()
    return line.rstrip("\n")

# Exercise 2
def reverse_lines(source, destination):
    file = open(source, "r")
    lines = file.readlines()
    file.close()
    file_1 = open(destination, "w")
    count = 0
    for i in range(len(lines) - 1, -1, -1):
        file_1.write(lines[i].strip() + "\n")
        count += 1
    file_1.close()
    return count

# Exercise 3
def merge_files(first, second, destination):
    file_1 = open(first, "r")
    lines_1 = file_1.readlines()
    file_1.close()
    file_2 = open(second, "r")
    lines_2 = file_2.readlines()
    file_2.close()
    file_3 = open(destination, "w")
    count = 0
    for line in lines_1:
        file_3.write(line.strip() + "\n")
        count += 1
    for line in lines_2:
        file_3.write(line.strip() + "\n")
        count += 1
    file_3.close()
    return count
    
# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == name:
            return int(parts[1])
    return -1

# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    found = False
    for i in range(len(lines)):
        parts = lines[i].strip().split(",")
        if parts[0] == name:
            lines[i] = parts[0] + "," + str(new_score) + "\n"
            found = True
            break
    if found == False:
        return False
    file = open(filename, "w")
    for line in lines:
        file.write(line)
    file.close()
    return True
