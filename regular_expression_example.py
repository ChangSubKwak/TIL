# 정규표현식 탐색의 특징
# 1. 매칭되는 패턴이 소비되지 않는다.(검색조건이나, 검색결과에는 포함되지 않음)
# 2. 4가지 방법이 존재한다. (전방/후방 - 긍정/부정)

import re

# 1. 전방긍정 탐색 (Positive Lookahead)
# - 패턴의 뒤에 탐색 패턴이 존재하는지 찾음

print("[Positive Lookahead]")

text = "foobar foobaz"
pattern = r'foo(?=bar)'
matches = re.findall(pattern, text)
print(matches)  # ['foo']

pattern = re.compile(r'foo(?=bar)')
matches = pattern.search(text)
print(matches.start(), matches.end())


# 2. 전방부정 탐색 (Negative Lookahead)
# - 패턴의 뒤에 탐색 패턴이 존재 안 하는 것을 찾음

print("[Negative Lookahead]")
pattern = r'foo(?!bar)'
matches = re.findall(pattern, text)
print(matches)  # ['foo']

pattern = re.compile(r'foo(?!bar)')
matches = pattern.search(text)
print(matches.start(), matches.end())


# 3. 후방긍정 탐색 (Positive Lookbehind)
# - 패턴의 앞에 탐색 패턴이 존재하는지 찾음

print("[Positive Lookbehind]")

text = "foobar foobaz"
pattern = r'(?<=foo)bar'
matches = re.findall(pattern, text)
print(matches)  # ['bar']

pattern = re.compile(r'(?<=foo)bar')
matches = pattern.search(text)
print(matches.start(), matches.end())


# 4. 후방부정 탐색 (Negative Lookbehind)
# - 패턴의 앞에 탐색 패턴이 존재 안 하는 것을 찾음

print("[Negative Lookbehind]")

text = "foobar fozbaz"
pattern = r'(?<!foo)baz'
matches = re.findall(pattern, text)
print(matches)  # ['baz']

pattern = re.compile(r'(?<!foo)baz')
matches = pattern.search(text)
print(matches.start(), matches.end())



