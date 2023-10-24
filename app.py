from flask import Flask, render_template, request, send_file
from PIL import Image
import random
import os
from Convert_to_file import convert_to_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        alphabet_images = request.files.getlist('alphabet_images')
        text_file = request.files['text_file']

        user_uploads_dir = 'static/images/user_uploads'
        os.makedirs(user_uploads_dir, exist_ok=True)

        alphabet_image_files = []
        for alphabet_image in alphabet_images:
            filename = os.path.join(user_uploads_dir, alphabet_image.filename)
            alphabet_image.save(filename)
            alphabet_image_files.append(filename)

        text_filename = os.path.join(user_uploads_dir, 'text.txt')
        text_file.save(text_filename)

        final_image_filename = process_files(alphabet_image_files, text_filename, user_uploads_dir)

        return send_file(final_image_filename, as_attachment=True)

    return render_template('upload.html')

def process_files(alphabet_image_files, text_filename, user_uploads_dir):
    x_coordinate = 250
    y_coordinate = 300
    max_x_coordinate = 1748  # Maximum x-coordinate before starting a new line (A5 paper width)
    line_height = 66  # Height of each line
    space_width = 25  # Width of a space character

    landscape = Image.open("static/images/paper.png")
    landscape = landscape.resize((1748, 2480))  # Resize to A5 paper dimensions (portrait)

    with open(text_filename, 'r') as file_txt:
        words = file_txt.read().split()
        for word in words:
            word_width = len(word) * space_width  # Calculate width based on average character width
            if x_coordinate + word_width > max_x_coordinate:
                # Move to the next line on the same page
                y_coordinate += line_height
                x_coordinate = 250

            for char in word:
                if char == "," or char == ".":
                    y_coordinate += 6
                    x_coordinate -= 5
                    file_name = convert_to_file(char, user_uploads_dir)
                    transparent = Image.open(file_name)
                    transparent = transparent.resize((40, 40))  # Resize character images
                    landscape.paste(transparent, (x_coordinate, y_coordinate), mask=transparent)
                    y_coordinate -= 6
                    x_coordinate += 50  # Adjust horizontal spacing
                elif char == "'" or char == "\"":
                    y_coordinate -= 8
                    x_coordinate -= 2
                    file_name = convert_to_file(char, user_uploads_dir)
                    transparent = Image.open(file_name)
                    transparent = transparent.resize((40, 40))  # Resize character images
                    landscape.paste(transparent, (x_coordinate, y_coordinate), mask=transparent)
                    y_coordinate += 8
                    x_coordinate += 50  # Adjust horizontal spacing
                else:
                    file_name = convert_to_file(char, user_uploads_dir)
                    transparent = Image.open(file_name)
                    transparent = transparent.resize((40, 40))  # Resize character images
                    landscape.paste(transparent, (x_coordinate, y_coordinate), mask=transparent)

                    x_coordinate += 30  # Adjust horizontal spacing

            # Move to the next line after each word
            x_coordinate += space_width

    final_image_filename = "static/images/final_image.png"
    landscape.save(final_image_filename, 'PNG')
    return final_image_filename

if __name__ == '__main__':
    app.run(debug=True)
