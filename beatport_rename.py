import os
import re
directory = "C:\\Users\\Valued Customer\\Downloads\\beatport_tracks\\"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if re.fullmatch(r'\d{8}', filename.split("_")[0]):
        ind = filename.index('_')
        new_name = filename[ind+1:]
        print(new_name)
        os.rename(directory+filename, directory+new_name)
        # os.rename(filename, new_name)
        # print(os.path.join(directory, filename))
        continue
    else:
        continue