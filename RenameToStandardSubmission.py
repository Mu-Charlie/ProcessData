import os
import Rename
# path="/data/mcl/nnUnet/nnUNet_raw/nnUNet_raw_data/Task013_COVID/inferTs"
path="/data/mcl/MICCAISbumission/Submission2"
ori_path = "/data/mcl/COVID-19-Data/COVID-19-20/Validation"
Rename.rename_to_standard_infer(ori_path,path)
