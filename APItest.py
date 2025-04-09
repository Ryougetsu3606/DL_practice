from zhipuai import ZhipuAI
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
url = "https://i.pixiv.re/c/540x540_70/img-master/img/2025/04/06/20/07/16/129027603_p0_master1200.jpg" # 替换为您要请求的图片URL
client = ZhipuAI(api_key="ff7e9e8b16474c0497784cf39b97089a.5I8fXNIiIQo3Ro14") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4v-plus-0111",
    stream=False,
    temperature=0.9,
    messages=[
        {
            "role": "user",
            "content": [
            {
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    }
                },
                {
                    "type": "text",
                    "text": "请描述图片中人物的特征。注意：特征之间用空格分隔，特征之间不要用逗号或其他符号分隔。"
                },
                {
                    "type": "text",
                    "text": "这个角色的名字是什么？注意：请你仅仅回答角色的名字，不要添加其他任何内容。重复，不要添加其他内容"
                }
            ]
        }
    ]
)

# 输出结果
print(response.choices[0].message.content)
# 请求url中的图片并打印
image_response = requests.get(url)
if image_response.status_code == 200:
    # Display the image using matplotlib
    image = Image.open(BytesIO(image_response.content))
    plt.imshow(image)
    plt.axis('off')  # Turn off axis
    plt.show()
else:
    print(f"Failed to fetch the image. Status code: {image_response.status_code}")