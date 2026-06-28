from PIL import Image
img = Image.open("img/logo.png").convert("RGBA")
data = img.getdata()
new = []
for r, g, b, a in data:
    if r < 30 and g < 30 and b < 30:
        new.append((0, 0, 0, 0))
    else:
        new.append((r, g, b, a))
img.putdata(new)
img.save("img/logo_sem_fundo.png")
print("Fundo removido com sucesso!")
