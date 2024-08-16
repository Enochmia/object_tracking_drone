from PIL import Image as aimg
import os
import matplotlib.pyplot as plt
import glob

newsize=(640,640)

dst_dir = 'path'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('path')
dir2 = "path"
i=0

for f in files:
    img = aimg.open(f)
    img_resize = img.resize(newsize)
    img_resize = img_resize.rotate(270)
    img_resize.save(os.path.join(dir2, f'yj_({i})'+'.jpg'))
    print(f'{i} finished')
    i+=1
