# from urllib.parse import urlparse
# import os

# def extract_domain(url):
#     parsed_url = urlparse(url)
#     return parsed_url.netloc

# # Danh sách các liên kết
# links = [
#     "https://doanhnghiep2020.gso.gov.vn/Login.aspx D19T00024:654321",
#     "https://www.uef.edu.vn/tththv/dang-nhap 205220921:Bichhoa2002",
#     "https://mobilelegends.vn raffyramos552:calderolang12",
#     "https://thongkedoanhnghiep.gso.gov.vn/Login.aspx 194600379820:4600379820"
# ]

# # Tạo một từ điển để lưu trữ các liên kết theo tên miền
# domain_links = {}

# for link in links:
#     domain = extract_domain(link)
#     if domain not in domain_links:
#         domain_links[domain] = []
#     domain_links[domain].append(link)

# # In ra các liên kết cho mỗi trang web
# for domain, links in domain_links.items():
#     print(f"Các liên kết trên trang web '{domain}':")
#     for link in links:
#         print(link)
#     print()


# if not os.path.exists('main_directory'):
#     os.mkdir('main_directory')



import re

def extract_urls(text):
    # Biểu thức chính quy để tìm kiếm các địa chỉ web
    url_pattern = r'(https?://\S+)'
    
    # Tìm kiếm các địa chỉ web trong văn bản
    urls = re.findall(url_pattern, text)
    
    return urls

# Dòng văn bản chứa địa chỉ web và văn bản khác
text = "http://lcms.ulis.vnu.edu.vn/sso/authenticate 20040750@vnu.edu.vn:laithanhbinh148"

# Lấy ra các địa chỉ web từ dòng văn bản
urls = extract_urls(text)

# In ra các địa chỉ web
print("Các địa chỉ web trong văn bản:")
for url in urls:
    print(url)
