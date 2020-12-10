import numpy as np
from PIL import Image
from ISR.models import RDN

img = Image.open('./test.jpg')
lr_img = np.array(img)
rdn=RDN(weights='psnr-small')

sr_img=rdn.predict(lr_img)
img=Image.fromarray(sr_img).show()
img.save('./recover.jpg')