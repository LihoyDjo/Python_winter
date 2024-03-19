from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height), (255, 0, 0))
draw = ImageDraw.Draw(img)

draw.line((0, 0, width, height), fill=(255, 255, 255), width=2)
draw.line((0, height, width, 0), fill=(255, 255, 255), width=2)

draw.rounded_rectangle((width // 2, height // 2, width, height), radius=20, fill=(0, 0, 0), outline=None, width=1)

draw.rectangle(((width // 4, height // 4), (width // 4 * 3, height // 4 * 3)), '#cc99ff')

draw.pieslice((0, 0, width // 5, height // 5), 45, 30, fill=(0, 170, 0), outline=(0, 0, 0), width=1)

# draw.chord((0, 0, width // 5, height // 5), 55, 30, fill=(200, 100, 0), outline=None, width=1)
draw.arc((0, 0, width // 5, height // 5), 180, 270, fill='#ffff00', width=10)

draw.ellipse((width * 0.2, height * 0.2, width * 0.8, height * 0.8), fill='#000000')

img.save('red_image.jpg')
