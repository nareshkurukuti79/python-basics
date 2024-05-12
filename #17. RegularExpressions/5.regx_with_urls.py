###########################  Reg EXP with URL's ######################

import re

with open("urls.txt") as file:
    urls = file.read()

    pattern = r"http://([a-zA-Z]+)\."
    pattern = r"http?://([a-zA-Z]+)\."
    pattern = r"http?://([a-zA-Z]+)\.[a-zA-Z0-9-]+"
    pattern = r"http?://(www\.)?([a-zA-Z]+)\.([a-zA-Z0-9-]+)"

    matches_result = re.finditer(pattern, urls)

    for match in matches_result:
        print(match)
        print(match.group())
        print(match.group(2))
        print(match.group(1))
        print(match.group(3))
