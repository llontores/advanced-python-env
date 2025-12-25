n = int(input())
valid_chars = "ABCEHKMOPTXY"

for _ in range(n):
    plate = input()
    if len(plate) != 6:
        print("No")
        continue
    
    digits = "0123456789"
    is_valid = True
    
    if plate[0] not in valid_chars: is_valid = False
    elif plate[1] not in digits or plate[2] not in digits or plate[3] not in digits: is_valid = False
    elif plate[4] not in valid_chars or plate[5] not in valid_chars: is_valid = False
    
    if is_valid: print("Yes")
    else: print("No")