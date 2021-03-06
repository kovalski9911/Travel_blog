import os
import secrets
from PIL import Image
from flask import current_app


def save_image_file(form_image_file, app_file_path, output_size=None):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image_file.filename)
    image_file_fn = random_hex + f_ext
    image_file_path = os.path.join(current_app.root_path, app_file_path, image_file_fn)
    
    if output_size != None:
        i = Image.open(form_image_file)
        i.thumbnail(output_size)
        i.save(image_file_path)
    else:
        form_image_file.save(image_file_path)  
         
    return image_file_fn