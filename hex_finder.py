from PIL import Image

def get_pixel_hex(image_path, x, y):
    # Open the image file
    img = Image.open(image_path)

    # Get the RGB value of the pixel at (x, y)
    pixel = img.getpixel((x, y))

    # Convert RGB to Hex
    hex_color = '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])

    return hex_color

# Example usage: Get the hex color of the pixel at (x, y) in the image
image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
x, y = 100, 150  # Replace with your desired pixel coordinates
hex_code = get_pixel_hex(image_path, x, y)
print(f"The hex code at ({x}, {y}) in the image is: {hex_code}")
