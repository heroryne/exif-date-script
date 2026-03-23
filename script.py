from pathlib import Path
from datetime import datetime
import piexif


folder = Path(input("Enter folder path: ").strip('"'))
# Loop through all .jpg files in the folder
for file in folder.glob("*.jpg"):
    print(file.stem)
    date = datetime.strptime(file.stem, "%y%m%d_%H%M%S")
    print (date)
    exif_dict = piexif.load(str(file))
    print(exif_dict)
# Writing the same date to all three date fields in the EXIF data

    exif_date = date.strftime("%Y:%m:%d %H:%M:%S").encode()
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = exif_date
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = exif_date
    exif_dict["0th"][piexif.ImageIFD.DateTime] = exif_date
    print (exif_dict["Exif"])
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, str(file))
#     print(f"Updated EXIF date for {file.name}")