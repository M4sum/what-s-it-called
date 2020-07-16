from PIL import Image

filepath = "D:\\dontDelete\\myWork\\0009.jpg"
savepath = "D:\\dontDelete\\myWork\\what-s-it-called\\uploads\\0009.jpg"

image_file = Image.open(filepath)
if image_file:
    passed = False
    filename = image_file.filename
    # filepath = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(savepath)
    passed = True
print(passed)