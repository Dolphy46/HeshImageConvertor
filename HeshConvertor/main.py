from PIL import Image
from pathlib import Path
from pygost.gost34112012 import GOST34112012


test_data = b'Data/Image/naruto.png'

path = Path(test_data).stem

print(path)
print(test_data)

img = Image.open(test_data)
m = GOST34112012(digest_size=256)
m.update(test_data)

hesh = m.hexdigest()
print(hesh)


img.save(f'Data/OutputData/PNM/{path}.pnm')

with open(f'Data/OutputData/hesh_{path}.txt', "w") as output:
    output.write(str(hesh))
