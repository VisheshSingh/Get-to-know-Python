import urllib.request

url = input('Enter the url to download the image: ')
file_name = input('Enter the file name to save as: ')

def download_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

download_jpg(url, 'images/', file_name)