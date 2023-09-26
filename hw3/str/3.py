"""def string_both_ends(str):
  if len(str) < 3:
    return ''

  return str[0:2] + str[-2:]"""

str  = str(input())
try:
  print(str[0:2] + str[-2:])
except:
  if len(str) < 3:
    print(" ")