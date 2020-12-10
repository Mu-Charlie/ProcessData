import nibabel as nib
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy
import cv2
#提交报错 operands could not broadcast together with shapes(55,512,512)(104,512,512)
# 经过排查 697号文件存在问题，截取697号文件的后55张图片用于验证


'''
#==========================排查错误代码==========================


result_path="/data/mcl/MICCAI2020_Submission"
img_path="/data/mcl/COVID-19-Data/COVID-19-20/Validation"
sample_path="/data/mcl/SampleSubmission"
# data=nib.load(path)
# imgs=data.dataobj
reuslt_num_map={}
for file in os.listdir(result_path):
    if '.gz' in file:
        data=nib.load(os.path.join(result_path,file))
        imgs=data.dataobj
        # print(file[:3])
        reuslt_num_map[file[:3]]=imgs.shape
        # print(imgs.shape)
for file in os.listdir(img_path):
    if '.gz' in file:
        data=nib.load(os.path.join(img_path,file))
        imgs=data.dataobj
        if imgs.shape[-1]!=reuslt_num_map[file[18:21]][-1]:
            print(file)
            break
        print(imgs.shape,end=' ')
        print(reuslt_num_map[file[18:21]])
print(reuslt_num_map['697'])



# for file in os.listdir(sample_path):
#     if '.gz' in file:
#         data=nib.load(os.path.join(sample_path,file))
#         imgs=data.dataobj
#         print(imgs.shape,end=' ')
#         if(imgs.shape[-1]==55):
#             print(file)
#         print(reuslt_num_map[file[:3]])

'''
'''
#========================纠正错误================================
对于结果文件，将697号文件的结果截取其后55张作为结果
训练文件同样也截取后55张图片
'''
result_file="/data/mcl/MICCAI2020_Submission/697.nii.gz"
img_file="/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task013_COVID/imagesTs/COVID19_0697_0000.nii.gz"
data=nib.load(result_file)
imgs=data.get_data()
imgs=imgs[:,:,-55:]
affine=data.affine.copy()
hdr=data.header.copy()
new_nii=nib.Nifti1Image(imgs,affine,hdr)
nib.save(new_nii,"/data/mcl/MICCAI2020_Submission/697_2.nii.gz")

data=nib.load(img_file)
imgs=data.get_data()
imgs=imgs[:,:,-55:]
affine=data.affine.copy()
hdr=data.header.copy()
new_nii=nib.Nifti1Image(imgs,affine,hdr)
nib.save(new_nii,"/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task013_COVID/imagesTs/COVID19_0697_2_0000.nii.gz")
