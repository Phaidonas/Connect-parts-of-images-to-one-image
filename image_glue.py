from PIL import Image
import glob
image_list = []
total_width=25000
total_height=25000
rows_number=10
columns_number=10;

row=0

img = Image.new('RGB', (total_width, total_height))
for filename in glob.glob('./image_both/*.tiff'):
    im=Image.open(filename)
    image_list.append(im)
print(len(image_list))

count=0
x_offset = 0
y_offset = 0
for im in image_list:
    count += 1
    img.paste(im, (x_offset, y_offset))
    print("X_off {}, Y_off {}".format(x_offset,y_offset))
    # print("Y_off {}".format(y_offset))

    if (count % 10 == 0):
        y_offset += int(total_height/columns_number)
        x_offset=0
        print("new row")
    else:
        x_offset += int(total_width/rows_number)

img.save('full.tiff')

