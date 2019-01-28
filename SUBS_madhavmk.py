def run(s,t):
    sub_index = []
    begin = t[0]
    l = len(t)
    for i in range(len(s)):
        if s[i] == begin:
            if t == s[i:i+l]:
                sub_index.append(i+1)
    print (*sub_index)