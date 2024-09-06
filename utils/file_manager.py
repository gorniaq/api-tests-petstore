def read_image_file(image_file_path):
    """
    Opens and reads an image file and returns the file content
    along with appropriate metadata for an API upload.
    :param image_file_path: The path to the image file.
    :return: A dictionary with file content and metadata.
    """
    with open(image_file_path, 'rb') as image_file:
        file_content = image_file.read()
    return {'file': ('image.jpg', file_content, 'image/jpeg')}
