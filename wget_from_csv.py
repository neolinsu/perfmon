import csv
import os
import wget

    
def download_file(url, dir_path, file_path):
    folder = os.path.exists(dir_path)
    if not folder:
        print(f'create floder: {dir_path}')
        os.makedirs(dir_path)
    ifile = os.path.exists(file_path)
    if not ifile:
        print(f'download: {url} to {file_path}')
        wget.download(url, file_path)


with open('01.org.perfmon.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        url = row[0]
        metas = url.split('/')
        dir_path = './' + '/'.join(metas[4:-1])
        file_path = './' + '/'.join(metas[4:])
        print(f"{dir_path}:{file_path}")
        download_file(url, dir_path, file_path)
