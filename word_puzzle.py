from PIL import Image

matrix = Image.open("word_matrix.png")
mask = Image.open("masks.png")

matrix = matrix.resize((6464, 4864))
mask = mask.resize((6464, 4864))

mask.putalpha(300)

matrix.paste(im=mask,box=(0,0),mask=mask)
matrix.show()
matrix.save("see_through.png")
