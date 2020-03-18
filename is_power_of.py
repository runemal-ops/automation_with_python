def is_power_of(number, base):
    number = number/base
    if number == base:
        return True
    elif number > base:
        return is_power_of(number,base)
    else:
        return False

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False