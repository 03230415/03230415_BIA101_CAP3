################################
# Github Repo link: https://github.com/03230415/03230415_BIA101_CAP3
# Your Name: Yangchen Om
# Your Section: BBIB
# Your Student ID Number: 03230415
################################
# REFERENCES
# https://www.youtube.com/watch?v=ypOlyre4PrI
################################
# SOLUTION
# Your Solution Score: 484217
################################

def calculate_total(input_file):
    total = 0
    with open(input_file, 'r') as file:
        for line in file:
            i = 0  # Left pointer
            j = len(line) - 1  # Right pointer
            first_digit = None
            last_digit = None
            
            # Move left pointer to the first digit
            while i < len(line) and not line[i].isdigit():
                i += 1
            
            # Move right pointer to the last digit
            while j >= 0 and not line[j].isdigit():
                j -= 1
            
            if i < j:  # Ensure valid positions for both pointers
                first_digit = int(line[i])
                last_digit = int(line[j])
                
            if first_digit is not None and last_digit is not None:
                 number = int(str(first_digit) + str(last_digit))
                 total += number
    return total

def main():
    input_file = "415.txt"  
    result = calculate_total(input_file)
    print("Total sum of numbers: ", result)

if __name__ == "__main__":
    main()
