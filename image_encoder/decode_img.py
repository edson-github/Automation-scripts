import base64


def decode():
    with open("base64_image.txt", "r") as f:
        base64_img = f.read()
    base64_img_bytes = base64_img.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)


if __name__ == '__main__':
    decode()
