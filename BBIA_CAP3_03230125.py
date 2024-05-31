################################
# Github Repo link
# https://github.com/yourusername/your-repo
# Your Name: Kinley Jigwang
# Your Section: A
# Your Student ID Number: 03230125
################################
# REFERENCES
#https://www.geeksforgeeks.org/python-string-isdigit-method/
#https://www.w3schools.com/python/ref_file_readlines.asp
################################
# SOLUTION
# Your Solution Score:  488366
################################

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_sum(file_name):
    lines = read_input(file_name)
    total_sum = 0

    for line in lines:
        first_digit = ''
        last_digit = ''
        left = 0
        right = len(line) - 1

        while left < len(line):
            if line[left].isdigit():
                first_digit = line[left]
                break
            left += 1
        
        while right >= 0:
            if line[right].isdigit():
                last_digit = line[right]
                break
            right -= 1

        if first_digit and last_digit:
            number = int(first_digit + last_digit)
            total_sum += number

    return total_sum

def print_solution(file_name):
    total_sum = calculate_sum(file_name)
    print(f"The total sum from the given input file {file_name} is {total_sum}")

if __name__ == "__main__":
    file_name = '125.txt'
    print_solution(file_name)