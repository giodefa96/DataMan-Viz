def pulisci(num):
    re_comp1 = re.compile("^(\d+)\-+(\d*)")
    m = re_comp1.search(num)
    if m:
        a = (int(m.group(1)) + int(m.group(2))) / 2
        return int(a)
    else:
        return int(num)
    return int(num)
