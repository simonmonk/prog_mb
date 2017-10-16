
def pluralize(s):
    if s.endswith("s"):
        return s
    elif s. endswith("y"):
        return s[:-1] + "ies"
    else:
        return s + "s"