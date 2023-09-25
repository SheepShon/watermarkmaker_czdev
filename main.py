from PIL import Image , ImageDraw, ImageFont, ImageFilter
import os.path
import json
from colorama import Fore, Back, Style
from colorama import init
sfile = open("settings.json")
data = json.load(sfile)
sfile.close()

TRANSPARENT = data['transparent']
AIWKF = data['asp_img_with_kf'] * 1.76
AIHKF = data['asp_img_height_kf'] * 3.4
AIIKF = data['asp_img_indent_kf'] * 17.14

os.system("cls")
print(Style.BRIGHT + Fore.BLUE + "czDevelopment "+ Fore.WHITE + "| Watermark maker |" + Fore.YELLOW + " Version 0.5" + Fore.WHITE + "\n")

def getpos(pos, im_width, im_height, wm_width, wm_height, indent):
    match pos:
        case "lu":
            xpos = indent
            ypos = indent
        case "ru":
            xpos = im_width-indent-wm_width
            ypos = indent
        case "ld":
            xpos = indent
            ypos = im_height-indent-wm_height
        case "rd":
            xpos = im_width-indent-wm_width
            ypos = im_height-indent-wm_height
        case "cc":
            xtiw = int(im_width/2)
            xtww = int(wm_width/2)
            xpos =  xtiw-xtww

            ytiw = int(im_height/2)
            ytww = int(wm_height/2)
            ypos = ytiw-ytww

        case "cu":
            xtiw = int(im_width/2)
            xtww = int(wm_width/2)
            xpos =  xtiw-xtww

            ypos = indent

        case "cd":
            xtiw = int(im_width/2)
            xtww = int(wm_width/2)
            xpos =  xtiw-xtww

            ypos = im_height-indent-wm_height

        case "lc":
            xpos = indent

            ytiw = int(im_height/2)
            ytww = int(wm_height/2)
            ypos = ytiw-ytww

        case "rc":
            xpos = im_width-indent-wm_width

            ytiw = int(im_height/2)
            ytww = int(wm_height/2)
            ypos = ytiw-ytww

            
    return xpos, ypos

print(Fore.YELLOW +"Режимы работы:"+ Fore.WHITE +"\n1 - Один файл, выбор логотипа и расположения\n2 - Массив файлов, один логотип и расположение для всех одинаковое\n3 - Массив файлов, выбор логотипа и расположения для каждого отдельно\n")
mode = input(Fore.CYAN +"Режим работы: "+ Fore.WHITE)

if mode == "1":

    file_name = input(Fore.CYAN +"Название файла [be.jpeg]: "+ Fore.WHITE)
    watermark = input(Fore.CYAN +"Watermark [pm/ym]: "+ Fore.WHITE)

    im = Image.open("ref/"+file_name)
    im_width, im_height = im.size

    if watermark == "pm":
        wm = Image.open("dist/pm.png").convert('RGBA')

        asp_img_with = im_width/AIWKF
        asp_img_height = asp_img_with/AIHKF
        indent = im_width/AIIKF

        wm = wm.resize((int(asp_img_with), int(asp_img_height)))
    elif watermark == "ym":
        wm = Image.open("dist/ym.png").convert('RGBA')

        asp_img_with = im_width/AIWKF
        asp_img_height = asp_img_with/AIHKF
        indent = im_width/AIIKF

        wm = wm.resize((int(asp_img_with), int(asp_img_height)))

    wm.putalpha(TRANSPARENT)
    wm_width, wm_height = wm.size

    pos = input(Fore.CYAN +"Расположение [cc/lu/ru/cu/ld/rd/cd/lc/rc]\n(c - центр | r - право | l - лево | u - верх | d - низ): "+ Fore.WHITE)
    xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height, int(indent))

    im.paste(wm, (xpos,ypos),wm)

    im.save("out/"+file_name)

    print(Fore.GREEN +'\nУспешно! Watermark добавлен на оригинальное изображение. Новое изображение сохранено под именем\n\n'+ Fore.YELLOW + 'wm-'+file_name)
    print(Fore.WHITE+"\nНажмите любую клавишу для закрытия консоли..")
    print(Style.NORMAL + Fore.BLACK+"")

elif mode == "2":

    watermark = input(Fore.CYAN +"Watermark [pm/ym]: "+ Fore.WHITE)
    pos = input(Fore.CYAN +"Расположение [cc/lu/ru/cu/ld/rd/cd/lc/rc]\n(c - центр | r - право | l - лево | u - верх | d - низ): "+ Fore.WHITE)

    files = os.listdir("ref")

    saved_files = []

    for image in files:
        im = Image.open("ref/"+image)
        im_width, im_height = im.size

        if watermark == "pm":
            wm = Image.open("dist/pm.png").convert('RGBA')

            asp_img_with = im_width/AIWKF
            asp_img_height = asp_img_with/AIHKF
            indent = im_width/AIIKF

            wm = wm.resize((int(asp_img_with), int(asp_img_height)))

        elif watermark == "ym":
            wm = Image.open("dist/ym.png").convert('RGBA')

            asp_img_with = im_width/AIWKF
            asp_img_height = asp_img_with/AIHKF
            indent = im_width/AIIKF

            wm = wm.resize((int(asp_img_with), int(asp_img_height)))

        wm.putalpha(TRANSPARENT)
        wm_width, wm_height = wm.size

        xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height, int(indent))
        im.paste(wm, (xpos,ypos),wm)
        im.save("out/"+image)
        saved_files.append("wm-"+image)

    print(Fore.GREEN +'\nУспешно! Watermark добавлен на массив изображений.\nСписок обработнных файлов:\n'+ Fore.YELLOW)
    for i in saved_files:
        print(i)

    print(Fore.WHITE+"\nНажмите любую клавишу для закрытия консоли..")
    print(Style.NORMAL + Fore.BLACK+"")

elif mode == "3":

    files = os.listdir("ref")

    saved_files = []

    for image in files:
        im = Image.open("ref/"+image)
        im_width, im_height = im.size
        print("\nПосле ознакомления с изображением, нажмите Enter в консоли.")
        im.show()
        watermark = input(Fore.CYAN +"Watermark [pm/ym]: "+ Fore.WHITE)
        
        if watermark == "pm":
            wm = Image.open("dist/pm.png").convert('RGBA')

            asp_img_with = im_width/AIWKF
            asp_img_height = asp_img_with/AIHKF
            indent = im_width/AIIKF

            wm = wm.resize((int(asp_img_with), int(asp_img_height)))
        elif watermark == "ym":
            wm = Image.open("dist/ym.png").convert('RGBA')

            asp_img_with = im_width/AIWKF
            asp_img_height = asp_img_with/AIHKF
            indent = im_width/AIIKF

            wm = wm.resize((int(asp_img_with), int(asp_img_height)))

        wm.putalpha(TRANSPARENT)
        wm_width, wm_height = wm.size

        pos = input(Fore.CYAN +"Расположение [cc/lu/ru/cu/ld/rd/cd/lc/rc]\n(c - центр | r - право | l - лево | u - верх | d - низ): "+ Fore.WHITE)

        xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height, int(indent))
        im.paste(wm, (xpos,ypos),wm)
        im.save("out/"+image)
        saved_files.append("wm-"+image)

    print(Fore.GREEN +'\nУспешно! Watermark добавлен на массив изображений.\nСписок обработнных файлов:\n'+ Fore.YELLOW)
    for i in saved_files:
        print(i)

    print(Fore.WHITE+"\nНажмите любую клавишу для закрытия консоли..")
    print(Style.NORMAL + Fore.BLACK+"")
