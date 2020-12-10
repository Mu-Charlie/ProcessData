# -*- coding: utf8 -*-
import nibabel as nib
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy
import cv2
'''
CT图像的nii文件，其中的图片为二值图片


'''




def save_nii_img(dir,file,save_img_dir):
    # 图片保存路径 保存文件夹+病人代号
    print("deal with "+os.path.join(dir,file))
    if (os.path.exists(save_img_dir) == False):
        os.mkdir(save_img_dir)
    save_dir = os.path.join(save_img_dir, file.split(".")[0].split('_')[0])
    if os.path.exists(save_dir) == False:
        os.mkdir(save_dir)
    data=nib.load(os.path.join(dir,file))
    imgs=data.dataobj
    # print(imgs.shape)

    # 循环保存图片至之前创建的路径中
    if "seg" in file:
        imgs=numpy.array(imgs)*255
    for i in range(imgs.shape[-1]):
        # print(os.path.join(save_img_dir,file.split(".")[0]))
        # print(os.path.join(save_dir,str(i+1)+".png"))
        # print(i)
        img = Image.fromarray(imgs[:, :,i])
        img=img.convert('L')
        img.save(os.path.join(save_dir,str(i+1)+".png"))

def dir_nii_to_img(root,save_root):
    #eg: save_root: ./data/Train
    if (os.path.exists(save_root) == False):
        os.mkdir(save_root)

    for dir, path, files in os.walk(root):
        # print(dir)
        # print(path)
        # print(files)
        for file in files:
            if 'gz' in file:
                if "seg" in file:
                    save_nii_img(dir,file,save_root+"/label")
                else:
                    save_nii_img(dir,file,save_root+"/img")
def nii_to_img(root,save_root):
    #数据集根目录下有 Train和Validation目录 分别建立相应的图片数据集
    # eg:save_root:./data
    if(os.path.exists(save_root)==False):
        os.mkdir(save_root)
    for root_dir,dirs,files in os.walk(root):
        for i in dirs:
            dir_nii_to_img(os.path.join(root_dir,i),os.path.join(save_root,i))


# img_arr=nib.load("volume-covid19-A-0003.nii")
# print(type(img_arr))
# data=img_arr.get_data()
# print(data)
# print(data[:,:,0].shape)
# plt.imshow(data[:,:,0],cmap='gray')
# plt.show()



# save_nii_img("C:\\Work\\BisheData\\COVID-19-20\\Train\\","volume-covid19-A-0003_seg.nii.gz",".\\data")
nii_to_img("/data/mcl/COVID-19-Data/COVID-19-20","/data/mcl/COVID-19-Data/Challenge_data")
# img=Image.open('C:\\Work\\BiShe\\ProcessData\\data\\volume-covid19-A-0003_ct\\1.png')
# print(img.size)
# img.show()
# print(numpy.array(img)[200:300,200:300])

#矢状位 冠状位
# print(img_arr.dataobj)
# plt.imshow(data[:,390,:],cmap='gray')
# plt.show()
# plt.imshow(data[290,:,:],cmap='gray')
# plt.show()
