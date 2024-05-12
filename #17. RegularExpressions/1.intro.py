##################### Introduction of Regular Expressions ##########

import re

# Example1

test_string = "tan"

pattern = ".a."
result = re.match(pattern, test_string)

print(result)

# Example2
match_result = re.finditer("[abc]", "a")
match_result = re.finditer("[0-2]", "88 99 11 22 34 15 10")

for match in match_result:
    print(match)


# Example3 Period
match_result = re.finditer(".", "123")
match_result = re.finditer(".", "abc")
match_result = re.findall("..", "abcd")

for match in match_result:
    print(match)

# ^ - Caret

match_result = re.finditer("^a", "a")
match_result = re.finditer("^a", "abc")
match_result = re.finditer("^a", "bac")
match_result = re.finditer("^ab", "abc")
match_result = re.finditer("^a", "acb")

for match in match_result:
    print(match)

# $ - Dollar

match_result = re.finditer("a$", "a")
match_result = re.finditer("a$", ".formula")
match_result = re.finditer("a$", "cab")

for match in match_result:
    print(match)

# * - Star
match_result = re.finditer("ma*n", "mn")
match_result = re.finditer("ma*n", "man")
match_result = re.finditer("ma*n", "maaaaaan")
match_result = re.finditer("ma*n", "main")
match_result = re.finditer("ma*n", "woman")
match_result = re.finditer("ma*n", "testmain")

for match in match_result:
    print(match)

# + - Plus
match_result = re.finditer("ma+n", "mn")
match_result = re.finditer("ma+n", "man")
match_result = re.finditer("ma+n", "maaaaaan")
match_result = re.finditer("ma+n", "main")
match_result = re.finditer("ma+n", "woman")
match_result = re.finditer("ma+n", "testmain")

for match in match_result:
    print(match)

# ? - Question Mark
match_result = re.finditer("ma?n", "mn")
match_result = re.finditer("ma?n", "man")
match_result = re.finditer("ma?n", "maaaaaan")
match_result = re.finditer("ma?n", "main")
match_result = re.finditer("ma?n", "woman")
match_result = re.finditer("ma?n", "testmain")

for match in match_result:
    print(match)

# {} - Brackets

match_result = re.finditer("a{2, 4}", "abc dat aa ")
match_result = re.finditer("a{2, 4}", "abc daat")
match_result = re.finditer("a{2, 4}", "aabc daat")
match_result = re.finditer("a{2, 4}", "aabc daaat caaaat")
match_result = re.finditer("a{2, 4}", "aabc daat caaaat daaaaag")

for match in match_result:
    print(match)

# [] - Brackets

match_result = re.finditer("[0-9]{2, 4}", "abc 123 dat aa 45")
match_result = re.finditer("a{2, 4}", "abc daat")
match_result = re.finditer("a{2, 4}", "aabc daat")
match_result = re.finditer("a{2, 4}", "aabc daaat caaaat")
match_result = re.finditer("a{2, 4}", "aabc daat caaaat daaaaag")

for match in match_result:
    print(match)

# | Alternation

match_result = re.finditer("a|b", "adc")
match_result = re.finditer("z|c", "adc")
match_result = re.finditer("z|c", "zzc")
match_result = re.finditer("z|c|t", "zzctv")

for match in match_result:
    print(match)

# () - Group
match_result = re.finditer("(a|b|c)xz", "abc xz")
match_result = re.finditer("(a|b|c)xz", "abcxz")
match_result = re.finditer("(a|b|c)xz", "abxz")
match_result = re.finditer("(a|b|c)xz", "axz")
match_result = re.finditer("(a|b|c)xz", "axz cabxz")

for match in match_result:
    print(match)


# \ - Backslash

match_result = re.finditer("\^xz", "^xz")

for match in match_result:
    print(match)
