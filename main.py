#project by: codevuive
#coder: Tuấn Lê
import os
from urllib.parse import urlparse
import re

# xử lý đọc file (đọc từng dòng một theo cấu trúc của file login)
def read_file_login(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


#xử lý lọc file lọc lấy các trường có .vn
def filter_file(key_word, file_path):
    with open('filter_login.txt', 'a', encoding='utf-8') as file:
        for line in read_file_login(file_path):
            if key_word in line:
                file.write(line)
                file.write('\n')

#Lọc lấy địa chỉ web
def extract_urls(text):
    # Biểu thức chính quy để tìm kiếm các địa chỉ web
    url_pattern = r'(https?://\S+)'
    
    # Tìm kiếm các địa chỉ web trong văn bản
    urls = re.findall(url_pattern, text)
    
    return urls



if __name__ == "__main__":
    
    with open('filter_login.txt', 'w', encoding='utf-8') as file:
        file.write('')

    key_words = ['.vn']
    file_path = input('Nhap duong dan file: ')
    for key in key_words:
        filter_file(key, file_path)
        
    #xử lý lọc các đường dần cùng một trang
    #rút tên miền 
    #tạo thư mục chính lưu tên miền
    if not os.path.exists('main_directory'):
        os.mkdir('main_directory')

    #đọc file và xử lý tên miền
    with open('filter_login.txt','r', encoding='utf-8') as file:
        for line in file:
            tmp = extract_urls(line.strip())
            if tmp != []:
                domain = urlparse(tmp[0]).netloc
            #thư mục con 
            sub_directory = os.path.join('main_directory', domain)
            new_sub_directory = sub_directory.replace(':', '_')
            #Kiểm tra sự tồn tại
            if not os.path.exists(new_sub_directory):
                os.mkdir(new_sub_directory)

            file_name = os.path.basename(sub_directory) + '.txt'
            file_path = os.path.join(new_sub_directory,file_name)
            with open(file_path, 'a', encoding='utf-8') as domain_file:
                domain_file.write(line)
                
