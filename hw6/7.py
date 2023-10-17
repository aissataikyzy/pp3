import re

credit_card_pattern = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'

def has_consecutive_repeats(card_number):
    for i in range(len(card_number) - 3):
        if card_number[i] == card_number[i + 1] == card_number[i + 2] == card_number[i + 3]:
            return True
    return False

n = int(input())

for _ in range(n):
    card_number = input().strip()
    
    card_number = card_number.replace("-", "")
    
    if re.match(credit_card_pattern, card_number) and not has_consecutive_repeats(card_number):
        print("Valid")
    else:
        print("Invalid")
