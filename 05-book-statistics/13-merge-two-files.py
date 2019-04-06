from PIL import Image

base = Image.open("text_description.png")
word_cloud = Image.open("word_cloud.png")
base.paste(word_cloud, (300, 40))
base.show()
