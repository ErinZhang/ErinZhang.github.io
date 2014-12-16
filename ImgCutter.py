# -*- coding: utf-8 -*-
from PIL import Image
import os
import math

# In Windows, the path of generated link contains '\', which cannot be recognized by Firefox
area = 120 * 120
# area = 240 * 240
rootDir2 = r"C:\Users\xujiah\Documents\GitHub\ErinZhang.github.io\works"
template = r"<a class='highslide' href='%s' onclick='return hs.expand(this)'><img src='%s' alt='%s'/></a>"

htmlfile = open('generated.html', 'w')

for root, dirs, files in os.walk(unicode(rootDir2, 'utf-8'), topdown=False):
    for rawname in files:
        fullname = os.path.join(root, rawname)
        filename, ext = rawname.split('.')
        # print filename
        # print ext
        thumbname = os.path.join(root, filename + "_thumb." + ext)
        print thumbname
        img = Image.open(fullname)
        zoom = math.sqrt(img.size[0] * img.size[1] / area)
        # print zoom
        img = img.resize((int(img.size[0] / zoom),
                          int(img.size[1] / zoom)), Image.ANTIALIAS)
        img.save(thumbname)
        htmlfile.write(unicode(template % (fullname, thumbname, filename)).encode('utf-8'))
        # break

htmlfile.close()