#load modules
from PIL import Image
from PIL.ExifTags import TAGS
from prettytable import PrettyTable

image_filename = "./canon_hdr_NO.jpg"

#initialiting prettytable object
table = PrettyTable()

#setting table feilds name
table.field_names = ["MetaTags", "Values"]

#load image
my_image = Image.open(image_filename)

#get EXIF standared Data of the image
img_exif_data = my_image.getexif()

for id  in img_exif_data:
    tag_name = TAGS.get(id, id)
    data = img_exif_data.get(id)
    
    #if data in bytes
    if isinstance(data, bytes):
        data = data.decode()

    table.add_row([tag_name, data])

print(table)