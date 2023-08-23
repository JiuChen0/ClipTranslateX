import pyperclip
import pandas as pd
import requests
from googletrans import Translator

# Google翻译初始化
google_translator = Translator()

# DeepL API参数
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"
API_KEY = "YOUR_DEEPL_API_KEY"
USER_AGENT = "YourApp/1.2.3"

# 定义翻译函数
def google_translate(text, target_language="zh-cn"):
    return google_translator.translate(text, dest=target_language).text

def deepl_translate(text, target_language="ZH"):
    headers = {
        "Authorization": f"DeepL-Auth-Key {API_KEY}",
        "User-Agent": USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = f"text={text}&target_lang={target_language}"
    response = requests.post(DEEPL_API_URL, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()['translations'][0]['text']

def translate_text(text, api_choice):
    if api_choice == "google":
        return google_translate(text)
    elif api_choice == "deepl":
        return deepl_translate(text)
    else:
        raise ValueError("Invalid API choice.")
