from PIL import Image


def create_dummy_image(file_path):
    # Create a simple 100x100 white image
    img = Image.new('RGB', (100, 100), color='white')
    img.save(file_path)

# Specify the path where you want to save the dummy image
create_dummy_image('path/to/dummy_image.jpg')
