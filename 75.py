f_input = open('75_input.txt', 'r', encoding="utf-8")
f_output = open('75_output.txt', 'w', encoding="utf-8")

a = f_input.read()
result = ""
is_first_letter = True
is_was_whitespase = False
for letter in a:
    if letter == " ":
        is_first_letter = True
        if not is_was_whitespase:
            result += " "
            is_was_whitespase = True
    else:
        is_was_whitespase = False
        if is_first_letter:
            result+=letter
            is_first_letter = False
        else:
            result += letter.lower()
f_output.write(result)
f_output.close()
f_input.close()
