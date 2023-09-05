def reverse(text):

    s1 = ''
    for c in text:
        print("c is: " + c)

        s1 = c + s1  # appending chars in reverse order
        print("s1 is: " + s1)
    return s1
print(reverse("Sid!!!"))
