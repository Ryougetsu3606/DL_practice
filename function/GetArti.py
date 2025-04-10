import requests
import random
import re

def fetch_article():
    while True:
        ran1 = random.randint(0, 1)
        if ran1 == 0:
            ran = random.randint(129354, 129864)
            # 目标 URL
            url = f"http://www.zuowenv.com/zuowen/300zi/{ran}.html"
        else:
            ran = random.randint(132677, 133582)
            # 目标 URL
            url = f"http://www.zuowenv.com/zuowen/600zi/{ran}.html"

        try:
            # 发送 HTTP GET 请求
            response = requests.get(url)
            # 检查响应状态码
            if response.status_code == 200:
                # 手动设置编码为 utf-8
                response.encoding = 'utf-8'
                # 获取 HTML 文本
                html_text = response.text
        except Exception as e:
            continue

        # 使用正则表达式提取 <div class="contson"><p><strong> 和 </p><p><img> 之间的文本
        match = re.search(r'<strong>(.*?)</p><p><img', html_text, re.S)
        if match:
            article = match.group(1).strip()
            # 使用正则表达式删除所有字母和特殊符号
            article = re.sub(r'[a-zA-Z@#$%^&*(),./<>?;=:\'\"]', '', article)
            # 删除“作文{**}字”的模式
            article = re.sub(r'[作文\{\d+\}字]', '', article)
            article = re.sub(r'选自', '', article)
            return article

