# -*- coding: utf-8 -*-
"""Chatbot1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJNB89umnOXYvZEOSxelISw6QQAV5gXE
"""

pip install openai -q

import openai
openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are powerful ChatGPT."},
    {"role": "user", "content": "I am Python, I want to master AI,NLP"},
    {"role": "assistant", "content": "Hello, Python. That's awesome! What do you want to know about AI?"},
    {"role": "user", "content": "What is NLP?"}
]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
          {"role": "system", "content": "You are powerful ChatGPT."},
          {"role": "user", "content": "I am Python, I want to master AI,NLP"},
          {"role": "assistant", "content": "Hello, Python. That's awesome! What do you want to know about AI?"},
         {"role": "user", "content": "What is NLP?"}
    ]
)

choices: [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "NLP stands for Natural Language Processing. It is a branch of AI that focuses on enabling machines to understand, interpret, and generate human language. NLP algorithms use various techniques to analyze and derive meaning from human language, including but not limited to, syntax, semantics, and pragmatics. Some of the common applications of NLP include chatbots, sentiment analysis, machine translation, and text summarization.",
        "role": "assistant"
      }
    }
  ]

def update_chat(messages, role, content):
  messages.append({"role": role, "content": content})
  return messages

def get_chatgpt_response(messages):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)
  return  response['choices'][0]['message']['content']

import pprint

messages=[
         {"role": "system", "content": "You are powerful ChatGPT."},
    {"role": "user", "content": "I am Python, I want to master AI,NLP"},
    {"role": "assistant", "content": "Hello, Python. That's awesome! What do you want to know about AI?"},
  ]

while True:
  pprint.pprint(messages)
  user_input = input()
  messages = update_chat(messages, "user", user_input)
  model_response = get_chatgpt_response(messages)
  messages = update_chat(messages, "assistant", model_response)