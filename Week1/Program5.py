size_hardisk=int(input("Enter the size of hardisk in GB: "))
if(size_hardisk<=0):
    print("Invalid Data Entered")
else:
    n_bytes=1024**3*size_hardisk
    print("The no of bytes in the hardisk is ",n_bytes)
    size_img=float(input("Enter the size of image in MB: "))
    if(size_img<=0):
        print("Invalid Data Entered")
    else:
        n_bytes_img=1024**2*size_img
        n_imgs=n_bytes//n_bytes_img
        print("The number of images the hardisk can hold is ",n_imgs)

