#filters
from PIL import Image

# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(load):
    global im
    im = Image.open(load)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im, name):
    im.save(name)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(filter):
    global im
    new_pix_val = []
    pix_val = list(filter.getdata())
    for i in range(len(pix_val)):
        if pix_val[i][0] + pix_val[i][1] + pix_val[i][2] < 182:
            new_pix_val.append([0, 51, 76])
        if 364 >= pix_val[i][0] + pix_val[i][1] + pix_val[i][2] >= 182:
            new_pix_val.append([217, 26, 33])
        if 546 >= pix_val[i][0] + pix_val[i][1] + pix_val[i][2] > 364:
            new_pix_val.append([252, 227, 166])
        if 546 < pix_val[i][0] + pix_val[i][1] + pix_val[i][2]:
            new_pix_val.append([252, 227, 166])
    newpixtuple = tuple(tuple(x) for x in new_pix_val)
    new_img = Image.new(im.mode, im.size)
    new_img.putdata(newpixtuple)
    new_img.show()
    return new_img

def main():
    im = load_img("Tokyo.jpg")
    newim = obamicon(im)
    save_img(newim, "Tokyobamicon.jpg")

if __name__ == '__main__':
    main()
