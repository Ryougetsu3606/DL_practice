from zhipuai import ZhipuAI
import requests

def article_evaluation(file_content, api, standard):
    """
    评估文章的函数，先输入文章内容，生成评语，再根据评语生成评分。
    :param file_content: 文章内容
    :return: 评估结果
    """
    if standard == "easing":
        comment_prompt = "你好，请为以下的作文文本生成一段评语。文本内容：{}\n注意：评语应在50到100字之间。评语应包括且仅仅包括：简要分析作文，并评价该作文水平如何。而无需给出其他任何内容。".format(file_content)
    else:
        comment_prompt = "你好，请为以下的作文文本生成一段评语。文本内容：{}\n注意：评语应遵循高考作文评分标准，具体如下：1.先评价立意，分为“立意深刻、独到/立意完整/立意简单，缺乏内涵/毫无立意”四档；2.再评价文笔，分为“文笔优美/良好/一般/很差”四档；3.最后评价字数，分为“200字以上/100-200字/50-100字/不足50字”四档，这里需要严格统计字数。而无需给出其他任何内容。".format(file_content)

    try:
        client = ZhipuAI(api_key=api)  # 填写您自己的APIKey
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
                            "text": comment_prompt
                        }
                    ]
                }
            ]
        )

        # 输出结果
        comment = response.choices[0].message.content
        if standard == "easing":
            eval_prompt = "你好，请你根据以下评语，生成一个评分。评语内容：{}\n注意：评分应在0到100之间。你应该仅仅输出一个数字作为评分，不能输出其他任何内容。".format(comment)
        else:
            eval_prompt = "你好，请你根据以下评语，生成一个评分。评语内容：{}\n注意：评分应遵循高考作文评分标准，具体如下：1.先评价立意，分为“立意深刻、独到/立意完整/立意简单，缺乏内涵/毫无立意”四档；2.再评价文笔，分为“文笔优美/良好/一般/很差”四档；3.最后评价字数，分为“200字以上/100-200字/50-100字/不足50字”四档。评语已经分好了档次，每一个点从高到低可以得30/20/10/5分，请你分析评语中给出的档次，计算总分。你应该仅仅输出一个数字作为评分，不能输出其他任何内容。".format(comment)
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
                            "text": eval_prompt
                        }
                    ]
                }
            ]
        )
        score = response.choices[0].message.content
        return comment, score

    except Exception as e:
        return f"发生错误", "N/A"
