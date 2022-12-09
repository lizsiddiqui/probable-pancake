import os
import shutil
source = 'C:/Users/lizsi/Downloads'
destination = 'C:/Users/lizsi/OneDrive/Desktop/The_Folder'

list_of_files = os.listdir (source)
for file_name in list_of_files: 
    name, ext = os.path.splitext (file_name)

    if ext == '':
        continue

    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + 'The_Documents'
        path3 = destination + '/' + 'The_Documents' + '/' + file_name

        print ('Path 1:', path1)
        print ('Path 3:', path3)

        if os.path.exists (path2):
            print ('Moving' + file_name + '...')
            shutil.move (path1, path3)

        else:
            os.makedirs (path2)
            print ('Moving ' + file_name + '...')
            shutil.move (path1, path3)