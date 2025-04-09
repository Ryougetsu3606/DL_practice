from zhipuai import ZhipuAI
import requests
import os
with open('test.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()
client = ZhipuAI(api_key="ff7e9e8b16474c0497784cf39b97089a.5I8fXNIiIQo3Ro14") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-flash",
    stream=False,
    temperature=0.01,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "你好，请为以下的作文文本生成一段评语。文本内容：{}\n注意：评语应在50到100字之间。评语应包括且仅仅包括：简要分析作文，并评价该作文水平如何。而无需给出其他任何内容。".format(file_content)
                }
            ]
        }
    ]
)

# 输出结果
comment = response.choices[0].message.content
print(comment)

response = client.chat.completions.create(
    model="glm-4-flash",
    stream=False,
    temperature=0.01,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "你好，请你根据以下评语，生成一个评分。评语内容：{}\n注意：评分应在0到100之间。你应该仅仅输出一个数字作为评分，不能输出其他任何内容。".format(comment)
                }
            ]
        }
    ]
)
score = response.choices[0].message.content
print("评分：{}".format(score))
