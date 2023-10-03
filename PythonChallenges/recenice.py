ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def to_string(i):
  if i >= 100:
    return ones[i // 100] + "hundred" + to_string(i % 100)
  if i <= 10:
    return ones[i]
  if i > 10 and i < 20:
    return teens[i - 10]
  return tens[i // 10] + ones[i % 10] or ""
  
d = {}

for i in range(1, 1000):
  string = to_string(i)
  key = i - len(string)
  if key not in d:
    d[key] = []
  d[key].append(string)

n = int(input())
words = []
replace_index = 0
sum_character = 0
for i in range(n):
  word = input()
  words.append(word)
  if word == "$":
    replace_index = i
  else:
    sum_character += len(word)
words[replace_index] = d[sum_character][0]
print(" ".join(words))