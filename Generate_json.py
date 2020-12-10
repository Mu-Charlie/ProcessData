import json
import os
info={}
info["name"]="COVID19MICCAI"
info["description"]="MICCAI2020 COVID-19 Lesion Segmentation"
info["reference"]="MICCAI 2020"
info["licence"]="unknown"
info["release"]="1.2 25/11/2020"
info["tensorImageSize"]="3D"
info["modality"]={"0":"CT"}
info["labels"]={
    "0":"background",
    "1":"Lesion"
}
info["numTraining"]=200
info["numTest"]=0
info["training"]=[]
trdata_path="/data/mcl/nnUnet/nnUNet_raw/Task07_COVID/imagesTr"
trlabel_path="/data/mcl/nnUnet/nnUNet_raw/Task07_COVID/labelsTr"
for file in os.listdir(trdata_path):
    img_path=os.path.join(trdata_path,file)
    label_path=os.path.join(trlabel_path, file)
    info["training"].append({"image":img_path,"label":label_path})
info["test"]=[]
print("=============================================================")
print("=============================================================")
print("=============================================================")

# for file in os.listdir(trlabel_path):
#     print(file)
file_name="dataset.json"
with open(file_name,'w') as file_obj:
    file_obj.write(json.dumps(info,ensure_ascii=False,indent=4,separators=(',',':')))


