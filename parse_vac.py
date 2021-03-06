import requests

# перед тем, как задать параметры , сделать автоопределение количества страниц и вакансий
# на больших количсетвах  падает на ключе "items" - создает пустые записи?

# задаем параметры
url = 'https://api.hh.ru/vacancies'
text = "Python"  # text: language (job) # позже сделать выбор из списка
#text = "Java"
#text = 'C++'
#text = "1C"
number_of_pages = 10
per_page = 10    # кол-во на странице

# предварительный список (равный кол-ву страниц ?)
pre_res = []
for page in range(number_of_pages):
    
    par = {'text': text,'per_page': per_page, 'page':page}
    resp = requests.get(url, params = par)
    cle = resp.json()
    pre_res.append(cle)

# создадим один общий список
res_vac = []
for el in pre_res:            # el - dict
    for vac in el['items']:   # el['items'] - одна найденная страница? уточнить
        res_vac.append(vac)   # vac - one vacancy

# создадим список существующих ключей верхнего уровня
res_keys = []
for vac in res_vac:
    for k, v in vac.items():
        if k not in res_keys:
            res_keys.append(k)

# просто печатаем по тем ключам, которые хотим. Далее сделать вывод в табличное поле на форме
for v in res_vac:
    print(v['id'],v['schedule']['name'], v['name'],v['salary'] , sep = ' --')

# кол-во найденных вакансий
print("Got {} vacancies".format(len(res_vac)))



