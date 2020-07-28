import os

root_path = './utils'
'''
遍历文件夹及其子文件夹中的文件，并存储在一个列表中
输入文件夹路径、空文件列表[]
返回 文件列表Filelist,包含文件名（完整路径）
'''

def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        # # 若只是要返回文件名，使用这个
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            get_filelist(newDir, Filelist)
    return Filelist
 
if __name__ =='__main__' :
    filepath_list = get_filelist(root_path, [])
 
 