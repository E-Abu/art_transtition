import requests
import colorgram

def pull_picture(url):
    img_data = requests.get(url).content
    with open('picture.jpg','wb') as handler:
        handler.write(img_data)

url = "http://img3.artron.net/auction/old/art8233/d/art82330060.jpg"
pull_picture(url)



'''
下面的内容是关于颜色提取的
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('sweet_pic.jpg', 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s
'''


