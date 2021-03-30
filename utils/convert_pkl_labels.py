import pickle
import os
# from tqdm import tqdm
with open("/home/niranjan/Projects/interactive_monet/igibson_far_cam/igibson_far_cam_train/dataset_dicts.pkl","rb") as f:
    data_list = pickle.load(f)
label_path = "/home/niranjan/Projects/interactive_monet/igibson_far_cam/igibson_far_cam_train/labels"
print(len(data_list))
for data in data_list:
    # print(data["file_name"])
    with open(os.path.join(label_path, data["file_name"][:-4].split("/")[-1])+".txt", "w") as f:
        
        for annotation in data["annotations"]:
            bbox = list(annotation["bbox"])
            bbox[0] = bbox[0]+bbox[2]/2
            bbox[1] = bbox[1]+bbox[3]/2
            print(str(annotation["category_id"])+" "+str(bbox[0]/256)+" "+ str(bbox[1]/256)+" "+str(bbox[2]/256)+" "+str(bbox[3]/256), file=f)
            # print(annotation["category_id"],bbox[0]/256, bbox[1]/256, bbox[2]/256, bbox[3]/256)
    # break