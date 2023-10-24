from PIL import Image
import random
import os

def convert_to_file(letter, user_uploads_dir):
    random_number = random.randint(1, 3)
    is_upper = letter.isupper()

    if letter == " ":
        file_name = os.path.join(user_uploads_dir, "space.png")
    elif letter == "'":
        file_name = os.path.join(user_uploads_dir, "single_apostrophe.png")
    elif letter == "\"":
        file_name = os.path.join(user_uploads_dir, "double_apostrophe.png")
    elif letter == ".":
        file_name = os.path.join(user_uploads_dir, "period.png")
    elif letter == ",":
        file_name = os.path.join(user_uploads_dir, "comma.png")
    elif letter == ";":
        file_name = os.path.join(user_uploads_dir, "semicolon.png")
    elif letter == ":":
        file_name = os.path.join(user_uploads_dir, "colon.png")
    elif letter == "-":
        file_name = os.path.join(user_uploads_dir, "dash.png")
    elif letter == "(":
        file_name = os.path.join(user_uploads_dir, "open_bracket.png")
    elif letter == ")":
        file_name = os.path.join(user_uploads_dir, "closed_bracket.png")
    elif letter == "1":
        file_name = os.path.join(user_uploads_dir, "one.png")
    elif letter == "2":
        file_name = os.path.join(user_uploads_dir, "two.png")
    elif letter == "3":
        file_name = os.path.join(user_uploads_dir, "three.png")
    elif letter == "4":
        file_name = os.path.join(user_uploads_dir, "four.png")
    elif letter == "5":
        file_name = os.path.join(user_uploads_dir, "five.png")
    elif letter == "6":
        file_name = os.path.join(user_uploads_dir, "six.png")
    elif letter == "7":
        file_name = os.path.join(user_uploads_dir, "seven.png")
    elif letter == "8":
        file_name = os.path.join(user_uploads_dir, "eight.png")
    elif letter == "9":
        file_name = os.path.join(user_uploads_dir, "nine.png")
    elif letter == "0":
        file_name = os.path.join(user_uploads_dir, "zero.png")
    elif is_upper == False:
        file_name = os.path.join(user_uploads_dir, f"lower_{letter}{random_number}.png")
    elif is_upper:
        file_name = os.path.join(user_uploads_dir, f"upper_{letter}{random_number}.png")
    elif is_upper == False:
        file_name = os.path.join(user_uploads_dir, f"lower_{letter}{random_number}.png")
    
    img = Image.open(file_name)
    rgba = img.convert('RGBA')
    datas = rgba.getdata()

    newData = []

    for item in datas:
        if item[0] > 220:
            newData.append((10, 240, 120, 1))
        else:
            newData.append(item)

    rgba.putdata(newData)

    new_file_name = file_name
    rgba.save(new_file_name, 'PNG')

    return file_name
