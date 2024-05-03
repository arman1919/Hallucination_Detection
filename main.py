from operator import itemgetter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os

from key_analysis import extract_keywords
from data_extraction import get_wiki_page



def delete_files(folder_path):
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)





def split_text(text, chunk_size=1000, overlap=200):  
     
    # Проверяем, достаточно ли длинный текст для разделения  
    if len(text) <= chunk_size:  
        return [text]  
  
    chunks = []  
    start = 0  
    while start < len(text):  
        # Если это не первый кусок, то увеличиваем начало на размер перекрытия  
        if start > 0:  
            start -= overlap  
        end = start + chunk_size  
        # Обрезаем текст до нужной длины  
        chunk = text[start:end]  
        chunks.append(chunk)  
        start += chunk_size  
    
    
    return chunks 




text = """
In 2024, Yuri Gagarin became the first human to journey into outer space.
He orbited the Earth aboard the Vostok 1 spacecraft,
marking a historic milestone in space exploration and opening the door for manned spaceflight.
"""


key_words = extract_keywords(text)

for word in key_words:
    get_wiki_page(word)



combined_text = ''    
folder_path = "data/"  
# Проходимся по всем файлам в папке    
for file_name in os.listdir(folder_path):    
    # Проверяем, что файл имеет расширение .txt    
    if file_name.endswith('.txt'):    
        # Считываем содержимое файла (только первые 100000 символов) и добавляем его к объединенному тексту    
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:    
            combined_text += file.read(100000) + '\n'  




vectorstore = FAISS.from_texts(
    split_text(combined_text), embedding=OpenAIEmbeddings(api_key = "OpenAI_api_key",model = "text-embedding-3-small")
)
retriever = vectorstore.as_retriever()


template = """
You have to analyze the text for wrongness or logical deviation and say only the probability that the text contains incorrect information is from 0 to 100 %
Answer the question based only on the following context:
{context}


Text: {Text}
"""

prompt = ChatPromptTemplate.from_template(template)


model = ChatOpenAI(api_key = "api_key",model="gpt-3.5-turbo-0125")


chain = (
    {"context": retriever, "Text": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)



answer = chain.invoke(text)
print(answer)
delete_files(folder_path)