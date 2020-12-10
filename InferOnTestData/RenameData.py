import os
import json
'''
将测试集数据重命名为模型能够推理的名称格式
建立一个map 映射实际名字与更改后名字的关系
将其存为json文件
{
“new_name1":"origin_name1",
“new_name2":"origin_name2",
“new_name3":"origin_name3",
“new_name4":"origin_name4",
“new_name5":"origin_name5",
...

“new_nameN":"origin_nameN"
}
'''
def rename_test_to_standard(path):
    #将原始文件名更改成模型能够推理的文件名格式 并将其映射关系记录到json文件中
    info={}
    i=1
    for file in os.listdir(path):
        new_file_name = "COVID19_"+"000"+str(i)
        i+=1
        new_file_name = new_file_name+ '_0000.nii.gz'
        info[new_file_name]=file
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))
    file_name = "newTestAndOldTestName.json"
    print(info)
    with open(file_name, 'w') as file_obj:
        file_obj.write(json.dumps(info, ensure_ascii=False, indent=4, separators=(',', ':')))

def rename_infer_to_origin(path):
    #将文件更改回原始文件
    info={}
    with open("newTestAndOldTestName.json") as f:
        info=json.load(f)
    # print("============================================")
    # print("                功能没有做测试                 ")
    # print("============================================")
    assert 0==1,"\n============================================\n            功能没有做测试,请先做测试            \n============================================\n"
    for file in os.listdir(path):
        new_file_name = info[file]
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))



if __name__=='__main__':
    # data_root='/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task007_COVID/COVIDtest'
    data_root='/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task007_COVID/COVIDinf'
    # rename_test_to_standard(data_root)
    rename_infer_to_origin(data_root)

