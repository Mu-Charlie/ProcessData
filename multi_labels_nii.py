import nibabel as nib
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy


# acknowledge:
# deal with kaggle data which includes 2D & 3D data
# 3D data:
# in folder: rp_im(the CT image,nii files),rp_lung_msk(lung mask,nii files),rp_msk(labels,nii mask)

# 2D data:
# int files: "tr_im.nii.gz"(the train data),"tr_mask.nii.gz"(the label),"val_im.nii.gz"(validation data)

# ps:this data includes 3 classes so...
#ground-glass (mask value =1), consolidation (=2) and pleural effusion(胸腔积液) (=3)
# consolidation:In pneumonia, the lungs are consolidated because the alveoli are filled with exudate 肺炎时，因肺泡内充满渗出液而使肺实变

# after deal format
# 3D:
# |--img
#     |--folder1
#     |--folder2
#     ...
# |--label1
#     |--folder1
#     |--folder2
#     ...
# |--label2
#     |--folder1
#     |--folder2
#     ...
# |--label3
#     |--folder1
#     |--folder2
#     ...

# 2D:
# |--img
#     |--file1
#     |--file2
#     ...
# |--label1
#     |--file1
#     |--file2
#     ...
# |--label2
#     |--file1
#     |--file2
#     ...
# |--label3
#     |--file1
#     |--file2
#     ...


def save_nii_img(dir, file, save_dir):
    # 图片保存路径 保存文件夹+病人代号
    print("deal with " + os.path.join(dir, file))
    if os.path.exists(save_dir) == False:
        os.mkdir(save_dir)
    data = nib.load(os.path.join(dir, file))
    imgs = data.dataobj
    # print(imgs.shape)

    # 循环保存图片至之前创建的路径中
    if True:
        imgs = numpy.array(imgs)
    for i in range(imgs.shape[-1]):
        # print(os.path.join(save_img_dir,file.split(".")[0]))
        # print(os.path.join(save_dir,str(i+1)+".png"))
        # print(i)
        if "msk" in dir:
            if "lung" in dir:
                img = Image.fromarray(imgs[:,:,i]*255).convert('L')
                save_path = os.path.join(save_dir, "lung-label")
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, file.split('.')[0])
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, str(i + 1) + ".png")
                img.save(save_path)
            else:
                img1 = numpy.zeros_like(imgs[:, :, i])
                img1[numpy.where(imgs[:, :, i] == 1)] = 255
                img2 = numpy.zeros_like(imgs[:, :, i])
                img2[numpy.where(imgs[:, :, i] == 2)] = 255
                img3 = numpy.zeros_like(imgs[:, :, i])
                img3[numpy.where(imgs[:, :, i] == 3)] = 255

                img1 = Image.fromarray(img1).convert('L')
                save_path = os.path.join(save_dir, "ground-glass-label")
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, file.split('.')[0])
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, str(i + 1) + ".png")
                # print(save_path)
                img1.save(save_path)

                img2 = Image.fromarray(img2).convert('L')
                save_path = os.path.join(save_dir, "consolidation-label")
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, file.split('.')[0])
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, str(i + 1) + ".png")
                img2.save(save_path)

                img3 = Image.fromarray(img3).convert('L')
                save_path = os.path.join(save_dir, "pleural-effusion-label")
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, file.split('.')[0])
                if os.path.exists(save_path) == False:
                    os.mkdir(save_path)
                save_path = os.path.join(save_path, str(i + 1) + ".png")
                img3.save(save_path)
        else:
            img = Image.fromarray(imgs[:, :, i])
            img = img.convert('L')
            save_path = os.path.join(save_dir, file.split('.')[0])
            if os.path.exists(save_path) == False:
                os.mkdir(save_path)
            img.save(os.path.join(save_path, str(i + 1) + ".png"))

def dir_nii_to_img(root,save_root):
    for dir, path, files in os.walk(root):
        for file in files:
            if "msk" in dir:
                save_nii_img(dir,file,save_root)
            else:
                save_nii_img(dir,file,os.path.join(save_root,'img'))


def nii_to_img_3d(root,save_root):
    # if (os.path.exists(save_root) == False):
    #     os.mkdir(save_root)
    if os.path.exists(save_root)==False:
        temp_root=save_root
        path_list=[]
        while os.path.exists(temp_root)==False:
            path_list.append(temp_root)
            temp_root=os.path.abspath(os.path.join(temp_root,".."))
        while len(path_list)!=0:
            paths=path_list.pop()
            os.mkdir(paths)
    for root_dir, dirs, files in os.walk(root):
        for i in dirs:
            dir_nii_to_img(os.path.join(root_dir, i), save_root)


def save_nii_img2d(root,file,save_root):
    if os.path.exists(save_root)==False:
        os.mkdir(save_root)
    print("deal with " + os.path.join(root, file))
    data = nib.load(os.path.join(root, file))
    imgs = data.dataobj
    if "im" in file:
        save_root=os.path.join(save_root,"img")
        if os.path.exists(save_root) == False:
            os.mkdir(save_root)
        for i in range(imgs.shape[-1]):
            img = Image.fromarray(imgs[:, :, i])
            img = img.convert('L')
            save_path = os.path.join(save_root, str(i + 1) + ".png")
            print(save_path)
            img.save(save_path)
    else:
        save_root1=os.path.join(save_root,"ground-glass-label")
        if os.path.exists(save_root1) == False:
            os.mkdir(save_root1)
        save_root2 = os.path.join(save_root, "consolidation-label")
        if os.path.exists(save_root2) == False:
            os.mkdir(save_root2)
        save_root3 = os.path.join(save_root, "pleural-effusion-label")
        if os.path.exists(save_root3) == False:
            os.mkdir(save_root3)
        for i in range(imgs.shape[-1]):
            img1 = numpy.zeros_like(imgs[:, :, i])
            img1[numpy.where(imgs[:, :, i] == 1)] = 255
            img2 = numpy.zeros_like(imgs[:, :, i])
            img2[numpy.where(imgs[:, :, i] == 2)] = 255
            img3 = numpy.zeros_like(imgs[:, :, i])
            img3[numpy.where(imgs[:, :, i] == 3)] = 255

            img1 = Image.fromarray(img1).convert('L')
            save_path = os.path.join(save_root1, str(i + 1) + ".png")
            print(save_path)
            img1.save(save_path)
            img2 = Image.fromarray(img2).convert('L')
            save_path = os.path.join(save_root2, str(i + 1) + ".png")
            print(save_path)
            img2.save(save_path)

            img3 = Image.fromarray(img3).convert('L')
            save_path = os.path.join(save_root3, str(i + 1) + ".png")
            print(save_path)

            img3.save(save_path)


def nii_to_img_2d(root,save_root):
    print(save_root)
    print(os.path.exists(save_root))
    if os.path.exists(save_root)==False:
        print("create..")
        temp_root=save_root
        path_list=[]
        while os.path.exists(temp_root)==False:
            path_list.append(temp_root)
            temp_root=os.path.abspath(os.path.join(temp_root,".."))
        while len(path_list)!=0:
            paths=path_list.pop()
            print("mkdir:"+paths)
            os.mkdir(paths)
    for root_dir,dirs,files in os.walk(root):
        for file in files:
            if "tr" in file:
                save_nii_img2d(root_dir,file,os.path.join(save_root,"Train"))
            else:
                save_nii_img2d(root_dir,file,os.path.join(save_root,"Validation"))



nii_to_img_2d("/data/mcl/COVID-19-Data/kaggle_nii_data/kaggle_2dseg_data","/data/mcl/COVID-19-Data/kaggle_data/2dData")

nii_to_img_3d("/data/mcl/COVID-19-Data/kaggle_nii_data/kaggle_seg_data","/data/mcl/COVID-19-Data/kaggle_data/3dData")
