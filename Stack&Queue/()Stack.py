def validate_format(chars):
    lookup = {'{':'}','[':']','(':')'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    phrase = "[][]{}()"
    print(validate_format(phrase))

