import wikipediaapi  # Импортируем библиотеку  
 
 
# Создаем объект Wiki, указывая язык и пользовательский агент  
wiki_wiki = wikipediaapi.Wikipedia(  
    language='en',  # Указываем язык  
    user_agent='my_cool_application/1.0'  # Указываем пользовательский агент  
)  
  
excluded_sections = ["See also", "References", "Further reading", "External links"]  
  
def print_sections(sections, level=0, file=None):  
    for s in sections:  
        # Печатаем секцию, если она не в списке исключений  
        if s.title not in excluded_sections:  
            print("%s: %s" % ("*" * (level + 1), s.title), file=file)  
            print(s.text, file=file)  # Печатаем текст секции  
        # Всегда вызываем print_sections для вложенных секций, даже если текущая секция в списке исключений  
        print_sections(s.sections, level + 1, file=file)  
  
def get_wiki_page(title):  
    # Получаем страницу по названию  
    page = wiki_wiki.page(title)  
  
    # Проверяем, существует ли страница  
    if not page.exists():  
        print("Страница не найдена")  
        return  None
  
    # Открываем файл для записи  
    with open(f"data/{title.replace(' ', '_')}.txt", "w", encoding='utf-8') as file:  
        print("Заголовок статьи:", page.title, file=file)  
        print(page.text, file=file)  # Печатаем основной текст статьи  
        print_sections(page.sections, file=file)  # Печатаем секции  
  
    return f"data/{title.replace(' ', '_')}.txt" 



