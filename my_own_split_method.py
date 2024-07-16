# strng = " abc "
# strng = "To be or not to be, that is the question"
strng = "   "
strng += " "
s = ''
ls = []
for i in range(len(strng)):

    s += strng[i]
    if s.isspace():
        pass
    else:
        if strng[i] == " ":
            ls.append(s.strip())
            s = ""
print(ls)
