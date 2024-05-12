############################ Reg EXP with Dates ####################

import re

with open("dates.txt") as file:
    # print(file)
    print(file.read())
    print(type(file.read()))
    dates = file.read()

    matches_result = re.finditer(r"\d\d.\d\d.\d\d\d\d", dates)
    matches_result = re.finditer(r"\d{2}.\d{2}.\d{4}", dates)
    matches_result = re.finditer(r"\d{2}/\d{2}/\d{4}", dates)
    matches_result = re.finditer(r"\d{2}.\d{2}.\d{4}", dates)
    matches_result = re.finditer(r"\d{2}-\d{2}-\d{4}", dates)
    matches_result = re.finditer(r"\d{2}[-/]\d{2}[-/]\d{4}", dates)

    for match in matches_result:
        print(match)
