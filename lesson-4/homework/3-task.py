txt = input("Enter string: ")
ind = 0
ans = ""
st = 0
used_chars = "AOIUEaoiue"
while ind < len(txt):
    ind += 2
    if ind >= len(txt):
        ans += txt[st : ind + 1]
        break
    if txt[ind] in used_chars:
        ind += 1
        continue
    else:
        ans += txt[st : ind + 1]
        if ind == len(txt) - 1:
            break
        ans += "_"
        used_chars += txt[ind]
        st = ind + 1
        ind += 2
print(ans)
