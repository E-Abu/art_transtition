import requests
import colorgram

picture_addr = '../data/art36181394.jpg'
url = "http://img3.artron.net/auction/old/art8233/d/art82330060.jpg"

lineart_addr = '../data/2fe743fbb2fb43165cad916a21a4462308f7d3fe.jpg'

def pull_picture(url, picture_addr):
    img_data = requests.get(url).content
    with open(picture_addr,'wb') as handler:
        handler.write(img_data)

#pull_picture(url,picture_addr)



'''
关于颜色提取的
colorgram
'''
def color_extract(picture_addr,number_of_colors):

    color_ex = colorgram.extract(picture_addr, number_of_colors)

    colors = []
    color_proportion =[]
    for color in color_ex:
        colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
        color_proportion.append(color.proportion)

    return colors, color_proportion

number_of_colors = 50
colors,color_proportion = color_extract(picture_addr,number_of_colors)

number_of_colors = len(colors)
print (colors[0])


'''
auto coloring
'''
import cv2 as cv
import numpy as np
import random

def color_proportion():
    return

def fill_color_demo(lineart_addr, colors):
    """
    漫水填充：会改变图像
    """
    image = cv.imread(lineart_addr)
    #print(type(image))


    # 复制图片
    copyImg = image.copy()
    # 获取图片的高和宽
    h, w = image.shape[:2]
    print(h,w)


    # 创建一个h+2,w+2的遮罩层，
    # 这里需要注意，OpenCV的默认规定，
    # 遮罩层的shape必须是h+2，w+2并且必须是单通道8位，具体原因我也不是很清楚。
    mask = np.zeros([h + 2, w + 2], np.uint8)

    # 这里执行漫水填充，参数代表：
    # copyImg：要填充的图片
    # mask：遮罩层
    # (30,30)：开始填充的位置（开始的种子点）
    # (0,255,255)：填充的值，这里填充成黄色
    # (100,100,100)：开始的种子点与整个图像的像素值的最大的负差值
    # (50,50,50)：开始的种子点与整个图像的像素值的最大的正差值
    # cv.FLOODFILL_FIXED_RANGE：处理图像的方法，一般处理彩色图象用这个方法
    i = 0
    counter =0
    while i < number_of_colors and counter < 500:
        r_x, r_y = (random.randint(0, h-1), random.randint(0, w-1))
        print (r_x, r_y,i,colors[i])
        seed_color = image[r_x, r_y]
        print (seed_color)
        if seed_color.tolist() == [255, 255, 255]:
            try:
                cv.floodFill(copyImg, mask, (r_x, r_y), colors[i], (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
                i += 1
            except Exception as e: print(e)
        counter += 1
    #cv.imshow("fill color", copyImg)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    cv.imwrite('../data/预览.jpg', copyImg)

fill_color_demo(lineart_addr,colors)

