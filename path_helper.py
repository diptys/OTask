import os

def list_check_file_or_folder_exist(file_list):
    exist_file_or_folders=[]
    non_exist_file_or_folders=[]
    for file_path in file_list:
        if(os.path.exists(file_path.rstrip())):
            exist_file_or_folders.append(file_path.rstrip())
        else:
            non_exist_file_or_folders.append(file_path.rstrip())
    return non_exist_file_or_folders

def file_check_file_or_folder_exist(input_file_name,output_file_name):
    with open(input_file_name) as f:
        file_list = list(f)    
    non_exist_file_or_folders_list=list_check_file_or_folder_exist(file_list)
    
    with open(output_file_name, 'w') as f:
        for item in non_exist_file_or_folders_list:
            f.write("%s\n" % item)

def main():
    with open('images_to_be_copied.txt') as f:
        file_list = list(f)    
    ls=list_check_file_or_folder_exist(file_list)
    print(ls)

    file_check_file_or_folder_exist("images_to_be_copied.txt","non_exist_file_or_folders.txt")
    

if __name__ == "__main__":
	main()