from PIL import Image

def convert_to_black_and_white(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to black and white
    bw_image = image.convert("L")

    # Save the black and white image
    bw_image.save("bw_image.png")

    print("Image converted to black and white.")

# Provide the path to the input PNG image
image_path = "i.png"

# Convert the image to black and white
convert_to_black_and_white(image_path)