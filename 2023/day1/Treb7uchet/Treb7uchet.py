import re
def extract_first_and_last(number):
    # Convert the number to a string to handle multi-digit numbers
    num_str = str(number)

    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    return first_digit, last_digit

def reconstruct_number(first_digit, last_digit):
    # Combine the digits to form a new number
    new_number = first_digit * 10 + last_digit
    return new_number if new_number != 10 else 0

def word_to_digit(word):
    word_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return word_dict.get(word, 0)

def CalibrationTool (line):

    pattern = re.compile(r'(\d+|one|two|three|four|five|six|seven|eight|nine)')

    # Find all matches in the line
    matches = pattern.findall(line)
    print("Matches: ", matches)

    # Convert words to digits
    digit_values = [word_to_digit(match) if not match.isdigit() else int(match) for match in matches]
    print("Individual values: ", digit_values)
    # Combine the digits to form a multi-digit number
    calibration_value = int(''.join(map(str, digit_values)))

    # Extract the first and last digits
    first_digit, last_digit = extract_first_and_last(calibration_value)

    # Reconstruct the number using the first and last digits
    calibration_value = reconstruct_number(first_digit, last_digit)
    
    print("Value = ", calibration_value)
    return calibration_value





    # original for first part below:
    # first_digit = None
    # last_digit = None
    # # After initializing vars, loop through the line to find first and last digits, last being reversed.
    # for char in line:
    #     if char.isdigit():
    #         first_digit = int(char)
    #         break

    # for char in reversed(line):
    #     if char.isdigit():
    #         last_digit = int(char)
    #         break
    #     # Check if both digits were found
    # if first_digit is not None and last_digit is not None:
    #     # Combine the digits to form a two-digit number
    #     calibration_value = first_digit * 10 + last_digit
    #     return calibration_value
    # else:
    #     # If no valid digits were found, return a default value (e.g., 0)
    #     return 0


def sum_calibrated_values(txtfile):
    
    with open(txtfile, 'r') as file:
        calibration_doc = file.read()

    lines = calibration_doc.split('\n')

    total_sum = 0

    for line in lines:
        if line:
            calibration_value = CalibrationTool(line)
            total_sum += calibration_value
    return total_sum - 10

txtfile = "C:\\Users\\Admin\\Documents\\code\\advent2023\\day1\\Treb7uchet\\input.txt"


result = sum_calibrated_values(txtfile)

print("Sum is: ", result)