s = input()
at = s.find("@")
ok = (
    s.count("@") == 1
    and at != 0
    and at != len(s) - 1
    and "." in s[at:]
)
print(ok)