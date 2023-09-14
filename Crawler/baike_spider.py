import requests
from bs4 import BeautifulSoup

# 定义目标URL
url = "https://www.zgbk.com/ecph/subject?SiteID=1&ID=197963"

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含字条信息的HTML元素，这可能需要根据具体网页结构来调整
    # 以下是一个示例，你需要根据实际情况修改选择器
    zitiao_elements = soup.select(".some-selector")

    # 循环遍历找到的字条信息元素
    for zitiao_element in zitiao_elements:
        # 提取字条信息并打印
        zitiao_info = zitiao_element.text.strip()
        print(zitiao_info)
else:
    print("请求失败，状态码：" + str(response.status_code))