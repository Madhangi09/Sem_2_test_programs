def is_pangram(s):
    if len(s)!=26:
        return False
    alpha=set("abcdefghijklmnopqrstuvwxyz")
    string_set=set(s)
    return string_set==alpha
input_str=input("Enter a string (lower case only):").strip()
if is_pangram(input_str):
    print ("The input is Pangram")
else:
    print ("The input is not a Pangram")
