import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    for _ in [".jpg", ".jpeg", ".png"]:
        if sys.argv[1].endswith(_) and sys.argv[2].endswith(_):
            break
        elif sys.argv[1].endswith(_) or sys.argv[2].endswith(_):
            sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")
    try:
        base_image = Image.open(sys.argv[1]).convert('RGBA')
        shirt = Image.open("shirt.png").convert('RGBA')
        #shirt = shirt.resize(base_image.size)
        base_image = ImageOps.fit(base_image, shirt.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        base_image.paste(shirt, shirt)
        base_image = base_image.convert('RGB')
        base_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

else:
    sys.exit("Too many command-line arguments")
