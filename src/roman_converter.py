def decimal_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("Número fuera de rango (1-3999)")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syms[i]
            number -= val[i]
        i += 1
    return roman_num
