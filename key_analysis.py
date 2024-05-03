import openai

import requests

import json

import nltk

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords



api_key = 'openai_api_key'


# Функция для извлечения ключевых слов
def extract_keywords(text):  
    # Удаляем стоп-слова (например, артикли, предлоги и местоимения)  
    stop_words = set(stopwords.words('english'))  
    words = word_tokenize(text)  
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]  
  
    # Обращаемся к новому API OpenAI для чатов  
    response = requests.post(  
        'chat_completions_link',  
        headers={'Authorization': f'Bearer {api_key}'},  
        json={  
            'model': 'gpt-3.5-turbo',  # Пример использования актуальной модели для чата  
            'messages': [{  
                'role': 'system',  
                'content': 'Extract 5  keywords from the following text without numbering:'  
            }, {  
                'role': 'user',  
                'content': text  
            }]  
        }  
    )  
  
    # Проверяем статус ответа  
    if response.status_code == 200:  
        # Пытаемся извлечь ключевые слова  
        try:  
            response_data = json.loads(response.text)  
            # Убедитесь, что получаете ответ в правильном формате  
            if 'choices' in response_data and len(response_data['choices']) > 0:  
                # Получаем текст первого ответа  
                answer = response_data['choices'][0]['message']['content']  
                keywords = answer.split(', ')  # Пример разделения строк, может потребоваться настройка  
                return keywords  
        except KeyError:  
            print("Ошибка: Проблема с извлечением данных из ответа API.")  
            print("Ответ API:", response.text)  
            return []  
    else:  
        print("Ошибка запроса к API. Код статуса:", response.status_code)  
        print("Ответ API:", response.text)  
        return []  
  
