from PIL import Image
import os
mark = Image.open(r"C:\Users\Darkonno\Pictures\програ\вотер_знак\вотр знак в1.png")
neim = os.listdir('изображение')
i = 0
for naum_fofto in neim:
    i += 1
    fofto = Image.open(os.path.join('изображение', naum_fofto))
    x, y = fofto.size
    hard = x - 397
    shir = y - 200
    position = (hard, shir)
    fofto.paste(mark, position, mask=mark)
    fofto.save(os.path.join('гот', f"{i}.jpg" ))
print("Complite   9")