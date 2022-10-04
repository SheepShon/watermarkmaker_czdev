from PIL import Image , ImageDraw, ImageFont, ImageFilter
import os.path
from colorama import Fore, Back, Style
from colorama import init

TRANSPARENT = 120
VERSION = "5.0"

os.system("cls")
print(Style.BRIGHT + Fore.BLUE + "czDevelopment "+ Fore.WHITE + "| Watermark maker |" + Fore.YELLOW + " Version " + VERSION + Fore.WHITE + "\n")

def getpos(pos, im_width, im_height, wm_width, wm_height):
    match pos:
        case "lu":
            xpos = 50
            ypos = 50
        case "ru":
            xpos = im_width-50-wm_width
            ypos = 50
        case "ld":
            xpos = 50
            ypos = im_height-50-wm_height
        case "rd":
            xpos = im_width-50-wm_width
            ypos = im_height-50-wm_height
    return xpos, ypos

print(Fore.YELLOW +"Режимы работы:"+ Fore.WHITE +"\n1 - Один файл, выбор логотипа и расположения\n2 - Массив файлов, один логотип и расположение для всех одинаковое\n3 - Массив файлов, выбор логотипа и расположения для каждого отдельно\n")
mode = input(Fore.CYAN +"Режим работы: "+ Fore.WHITE)

if mode == "1":

    file_name = input(Fore.CYAN +"Название файла [be.jpeg]: "+ Fore.WHITE)
    watermark = input(Fore.CYAN +"Watermark [pm/ym]: "+ Fore.WHITE)
    if watermark == "pm":
        wm = Image.open("dist/pm.png").convert('RGBA')
        wm = wm.resize((500, 160))
    elif watermark == "ym":
        wm = Image.open("dist/ym.png").convert('RGBA')
        wm = wm.resize((500, 150))

    wm.putalpha(TRANSPARENT)
    wm_width, wm_height = wm.size

    im = Image.open("ref/"+file_name)
    im_width, im_height = im.size

    pos = input(Fore.CYAN +"Расположение [lu/ru/ld/rd]: "+ Fore.WHITE)
    xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height)

    im.paste(wm, (xpos,ypos),wm)

    im.save("out/wm-"+file_name)

    print(Fore.GREEN +'\nУспешно! Watermark добавлен на оригинальное изображение. Новое изображение сохранено под именем\n\n'+ Fore.YELLOW + 'wm-'+file_name)
    print(Fore.WHITE+"\nНажмите любую клавишу для закрытия консоли..")
    print(Style.NORMAL + Fore.BLACK+"")

elif mode == "2":

    watermark = input(Fore.CYAN +"Watermark [pm/ym]: "+ Fore.WHITE)
    if watermark == "pm":
        wm = Image.open("dist/pm.png").convert('RGBA')
        wm = wm.resize((500, 160))
    elif watermark == "ym":
        wm = Image.open("dist/ym.png").convert('RGBA')
        wm = wm.resize((500, 150))

    wm.putalpha(TRANSPARENT)
    wm_width, wm_height = wm.size

    pos = input(Fore.CYAN +"Расположение [lu/ru/ld/rd]: "+ Fore.WHITE)

    files = os.listdir("ref")

    saved_files = []

    for image in files:
        im = Image.open("ref/"+image)
        im_width, im_height = im.size
        xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height)
        im.paste(wm, (xpos,ypos),wm)
        im.save("out/wm-"+image)
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
            wm = wm.resize((500, 160))
        elif watermark == "ym":
            wm = Image.open("dist/ym.png").convert('RGBA')
            wm = wm.resize((500, 150))

        wm.putalpha(TRANSPARENT)
        wm_width, wm_height = wm.size
        

        pos = input(Fore.CYAN +"Расположение [lu/ru/ld/rd]: "+ Fore.WHITE)

        xpos,ypos = getpos(pos, im_width, im_height, wm_width, wm_height)
        im.paste(wm, (xpos,ypos),wm)
        im.save("out/wm-"+image)
        saved_files.append("wm-"+image)

    print(Fore.GREEN +'\nУспешно! Watermark добавлен на массив изображений.\nСписок обработнных файлов:\n'+ Fore.YELLOW)
    for i in saved_files:
        print(i)

    print(Fore.WHITE+"\nНажмите любую клавишу для закрытия консоли..")
    print(Style.NORMAL + Fore.BLACK+"")
