from PIL import Image, ImageOps

def invert_black_and_white(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to black and white
    bw_image = image.convert("L")

    # Invert the black and white colors
    inverted_image = ImageOps.invert(bw_image)

    # Save the inverted image
    inverted_image.save("inverted_image.png")

    print("Image colors inverted.")

# Provide the path to the input PNG image
image_path = "invert.JPG"

# Invert the black and white colors in the image
invert_black_and_white(image_path)