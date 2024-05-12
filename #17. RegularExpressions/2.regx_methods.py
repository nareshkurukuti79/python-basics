############################## Regx Methods ########################

import re

# \d [0-9]

# findall()

string = "hello 12 hi 65 123 howdy 784 907"
pattern = "\d+"

result = re.findall(pattern, string)
print(result)

# split()
string = "hello 12 hi 65 123 howdy 784 907"
pattern = "\d+"

result = re.split(pattern, string)
print(result)


# sub()
string = "abc 12 \
    de 23 \n f45 621"

pattern = "\s+"
print(re.findall(pattern, string))

replace = ""
new_string = re.sub(pattern, replace, string)
print(new_string)

# search()
string = "python is fun"
pattern = "\Apython"

match_result1 = re.search(pattern, string)
print(match_result1)


# match.group()

string = "12345 67, 789 1122"
pattern = "(\d{3}) (\d{2})"

match = re.search(pattern, string)

if match:
    print(match.group())

    print(match.start())
    print(match.end())
    print(match.span())
else:
    print("Match not found")

# r - raw string

pattern_one = "\tBook"
pattern_two = r"\tBook"
print(pattern_one)
print(pattern_two)


# Special Sequences Part - 1

# \d - [0-9]
string = "12 3.4 5 67.8 90"
pattern = r"\d"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \D - [a-zA-Z_]

string = "12 3.4 5 67.8 90 # Hi There < ? _"
pattern = r"\D"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \s - (space, tab, " ", "\t", "\n")
string = "12 3.4 5 67.8 90 # Hi There \t \n < ? _"
pattern = r"\s"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)


# \S - [a-zA-Z0-9_]
string = "12 3.4 5 67.8 90 # Hi There \t \n NARESH < ? _"
pattern = r"\S"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \w - [a-zA-Z0-9_]
string = "12 3.4 5 67.8 90 # Hi There \t \n NARESH < ? _"
pattern = r"\w"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \W - not [a-zA-Z0-9_]
string = "12 3.4 5 67.8 90 # Hi There \t \n NARESH < ? _"
pattern = r"\W"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \b
# case 1 - At the beginning
string = "possible 12 3.4 5 67.8 90 # Hi There \t \n NARESH < ? _ > ^ impossible"
pattern = r"\bpossible"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# case 1 - At the end
string = "12 3.4 5 67.8 90 # Hi There impossible \t \n NARESH < ? _ > ^ impossible"
pattern = r"possible\b"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# \B
# case 1 - Not At the beginning
string = "possible 12 3.4 5 67.8 90 # Hi There \t \n NARESH < ? _ > ^ impossible"
pattern = r"\Bpossible"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)

# case 1 - Not At the end
string = "12 3.4 5 67.8 90 # Hi There impossible \t \n NARESH < ? _ > ^ impossible"
pattern = r"possible\B"
match_result = re.finditer(pattern, string)

for match in match_result:
    print(match)
