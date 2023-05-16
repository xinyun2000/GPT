"""
作者：Xinyun
日期：2023年05月15日
学习使用api并且使用GPT3和GPT3.5进行两个简单的示例
"""

import openai
import os
# 使用os库读取环境变量
openai_api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key:",openai_api_key)

# 创建一个GPT-3的请求
def GPT3():
    response = openai.Completion.create(
        model="text-davinci-003",#表示GPT3.5的模型
        prompt = "Please provide some tips for beginner Python programmer",#最核心的概念prompt
        temperature=0.7,#控制生成内容的随机性。较低的值将使生成内容更有趣和多样，较高的值将使生成内容更加一致和可预测。
        max_tokens=50,#控制生成内容的长度。您可以根据需要设置此参数，以获得适当长度的文本。
        frequency_penalty=0,
        presence_penalty=0
    )
    #输出GPT-3的回答
    print(response.choices[0].text.strip())

def GPTnewest():#使用GPT3.5进行
    messages=[{'role':'system','content':'你是一个乐于助人的诗人'}]#通过系统角色给助手设定一个人设，相当于之前的prompt？
    messages.append({'role':'user','content':'作一首诗，要有风，要有花，要有雪，要有月'})#用户向gpt3.5提出第一个问题
    #openai.chatcompletion即调用接口
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    #在messages中加入assistant的第一个问题的回答部分
    messages.append({
        'role':response.choices[0]['message']['role'],
        'content':response.choices[0]['message']['content']
    })
    #在messages中加入用户提出第二个问题
    messages.append({'role':'user','content':'好诗！好诗！'})
    #调用api接口
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    # 在messages中加入assistant的第二个问题的回答部分
    messages.append({
        'role': response['choices'][0]['message']['role'],
        'content': response['choices'][0]['message']['content']
    })
    print(messages)


if __name__ == "__main__":
    GPTnewest()