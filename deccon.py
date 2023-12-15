def dec(deci, base):
    if base == 2:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0','1']:
                raise ValueError ("invalid literal for dec() with base 2:", deci)
            sum_ += int(i)*2**(len(str(deci))-x)
            x += 1
        return sum_
    elif base == 8:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0','1', '2', '3', '4', '5','6', '7']:
                raise ValueError ("invalid literal for dec() with base 8:", deci)
            sum_ += int(i)*8**(len(str(deci))-x)
            x += 1
        return sum_
    elif base == 16:
        sum_ = 0
        x = 1
        for i in str(deci):
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7','8','9','A','B','C','D','E','F']:
                raise ValueError ("invalid literal for dec() with base 16:", deci)
            if i == 'A':
                i = 10
            if i == 'B':
                i = 11
            if i == 'C':
                i = 12
            if i == 'D':
                i = 13
            if i == 'E':
                i = 14
            if i == 'F':
                i = 15
            sum_ += int(i)*16**(len(deci)-x)
            x += 1
        return sum_
    else:
        raise ValueError ("invalid literal for dec() with base 2, 8, 16:", base)
