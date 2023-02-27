import sys

def sum_digits(text):
    digits = []
    current_digit = ''
    for char in text:
        if char.isdigit():
            current_digit += char
        elif current_digit:
            digits.append(int(current_digit))
            current_digit = ''
    if current_digit:
        digits.append(int(current_digit))
    return sum(digits)

def main():
    is_on = True
    total_sum = 0
    for line in sys.stdin:
        line = line.strip()
        if line.lower() == 'off':
            is_on = False
        elif line.lower() == 'on':
            is_on = True
        elif '=' in line:
            if is_on:
                result = sum_digits(line)
                total_sum += result
                print(total_sum)
        elif is_on:
            result = sum_digits(line)
            total_sum += result

if __name__ == '__main__':
    main()
