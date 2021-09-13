import re

def remove_vol(string):
    clean_str = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    a = list(clean_str)
    without_empty_strings = [string for string in a if string != " "]
    return sorted(without_empty_strings)


print(remove_vol('virker det her lort'))