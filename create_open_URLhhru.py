'''Использовал для создания ссылки на страницу вакансии в hh.ru,
используя ее номер (id), полученый парсером.
После создания открываем в конкретном браузере Vivaldi.
'''

import pyperclip, webbrowser

vac_num = str(input("Введите номер (id) вакансии: \n"))
##vac_num = "37415007"  # test

# create needed page
page_url = r"https://hh.ru/vacancy/{}".format(vac_num)
pyperclip.copy(page_url)
print("Адрес вакансии скопирован в буфер: \n" + page_url)

# open our created page in needed broweser
vivaldi_path = r"C:\Program Files\Vivaldi\Application\vivaldi.exe" 
webbrowser.register("vivaldi", None, webbrowser.BackgroundBrowser(vivaldi_path))
webbrowser.get('vivaldi').open_new_tab(page_url)
