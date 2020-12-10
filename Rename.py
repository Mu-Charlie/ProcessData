import os
import numpy as np
import pandas as pd


def rename_test(path):
    for file in os.listdir(path):
        new_file_name = file.replace("volume-covid19-A-", "COVID19_")
        new_file_name = new_file_name[:12] + '_0000.nii.gz'
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
def rename_train(path):
    for file in os.listdir(path):
        new_file_name = file.replace("volume-covid19-A-", "COVID19_")
        new_file_name = new_file_name[:12] + '.nii.gz'
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
def rename_to_standard_infer(ori_path,path):#需要从原始数据集路径中将原始文件名读出
    # "/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task013_COVID/inferTs"
    # ori_path = "/data/mcl/COVID-19-Data/COVID-19-20/Validation"
    ori_file_map={}
    for file in os.listdir(ori_path):#读出所有原始文件名，截取出需要用的部分
        new_file_name=file.replace("volume-covid19-A-","")
        new_file_name = new_file_name.replace("_ct", "")
        ori_file_map[new_file_name[:4]]=new_file_name[1:]
    for file in os.listdir(path):
        if '.gz' in file:
            new_file_name=ori_file_map[file[8:12]]
            os.rename(os.path.join(path,file),os.path.join(path,new_file_name))

if __name__=='__main__':
    print("Rename.py main")
    # img_path = '/data/mcl/nnUnet/nnUNet_raw/Task13_COVID/imagesTr/'
    # label_path = '/data/mcl/nnUnet/nnUNet_raw/Task13_COVID/labelsTr'
    # rename_train(img_path)
    # rename_train(label_path)

    # 新数据
    # img_path = '/data/mcl/nnUnet/nnUNet_raw/Task07_COVID/imagesTr/'
    # label_path = '/data/mcl/nnUnet/nnUNet_raw/Task07_COVID/labelsTr'
    # rename_train(img_path)
    # rename_train(label_path)
    # 重命名新数据的验证集
    # img_path = '/data/mcl/nnUnet/nnUNet_raw/Task07_COVID/imagesTs'
    # rename_test(img_path)

    # for file in os.listdir(img_path):
    #     new_file_name=file.replace("volume-covid19-A-","COVID19_")
    #     new_file_name=new_file_name[:12]+'.nii.gz'
    #     os.rename(os.path.join(img_path,file),os.path.join(img_path,new_file_name))

    #
    # for file in os.listdir(label_path):
    #     new_file_name = file.replace("volume-covid19-A-", "COVID19_")
    #     new_file_name = new_file_name[:12] + '.nii.gz'
    #     os.rename(os.path.join(label_path,file),os.path.join(label_path,new_file_name))
