from PIL import Image
import os
mark = Image.open(r"C:\Users\Darkonno\Pictures\програ\вотер_знак\вотр знак в1.png") # открывает воденой знак
neim = os.listdir('изображение') # делает список имен в папке
i = 0
for naum_fofto in neim: # переберает имена вытаскивая по одному из списка
    i += 1
    fofto = Image.open(os.path.join('изображение', naum_fofto)) # открывает фото в папке по имени которому вытащили из списка
    x, y = fofto.size # вычисление размера пикселей на основной фотографии
    hard = x - 397
    shir = y - 200
    position = (hard, shir)
    fofto.paste(mark, position, mask=mark) # на осоновную фоогорафию вставляетм воденой знак по кординатам и mask=mark сохраняет альфоканал
    fofto.save(os.path.join('гот', f"{i}.jpg" ))
print("Complite   8")