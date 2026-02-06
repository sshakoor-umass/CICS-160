def password_checker(password):
    chars = [x for x in password]
    if len(chars) < 8:
        return False
    elif not chars[0] == chars[0].upper() and not chars[1] == chars[1].upper() and not chars[0] != chars[1]:
        return False
    else:
        total = 0
        for c in chars:
            if not c.isalnum():
                return False
            if c.isdigit():
                total += int(c)
        return total % 2 == 0