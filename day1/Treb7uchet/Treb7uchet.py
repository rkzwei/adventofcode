



def CalibrationTool (line):
    first_digit = None
    last_digit = None
    # After initializing vars, loop through the line to find first and last digits, last being reversed.
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break
        # Check if both digits were found
    if first_digit is not None and last_digit is not None:
        # Combine the digits to form a two-digit number
        calibration_value = first_digit * 10 + last_digit
        return calibration_value
    else:
        # If no valid digits were found, return a default value (e.g., 0)
        return 0


def sum_calibrated_values(txtfile):
    
    with open(txtfile, 'r') as file:
        calibration_doc = file.read()

    lines = calibration_doc.split('\n')

    total_sum = 0

    for line in lines:
        if line:
            calibration_value = CalibrationTool(line)
            total_sum += calibration_value
    return total_sum

txtfile = "C:\\Users\\Admin\\Documents\\code\\advent2023\\day1\\Treb7uchet\\input.txt"


result = sum_calibrated_values(txtfile)

print("Sum is: ", result)