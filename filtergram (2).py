#filtergram
import filters

def main():
    filename = input("FILENAME: ")
    newfname = input("SAVE AS: ")
    im = filters.load_img(filename)
    newim = filters.obamicon(im)
    filters.save_img(newim, newfname)

if __name__ == '__main__':
    main()
