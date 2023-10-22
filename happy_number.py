ticket_number = input()

digits = [int(digit) for digit in ticket_number]

if sum(digits[:3]) == sum(digits[3:]):
    print("Этот билет счастливый!")
else:
    print("Этот билет не счастливый.")
