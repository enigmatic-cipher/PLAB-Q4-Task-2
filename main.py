"""
Given a string as input. Create a new string in which every occurrence of capital 'A' is doubled and small 'a' is tripled.
Input-> "Asana"
Output-> "AAsaaanaaa"
"""

st = "Asana"
ln = len(st)
strn = ""
for i in range(0,ln):
  ch = st[i]
  if (ch=="A"):
    strn = strn + ch + "A"
  elif (ch=="a"):
    strn = strn + ch + "aa"
  print(strn)