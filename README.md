# Обрезка ссылок с помощью Битли

[Скрипт для создания укороченных ссылок и подсчёта количества переходов поссылке]

### Как установить

1. Python3 должен быть уже установлен. 
2. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей
3. ```pip install -r requirements.txt```
   API ключ для входа берется тут [Bitly.com] (https://app.bitly.com/Bo35bTdm3qT/home).
     а. Регистрация на сайте
     b. Создание access token
4. Создайте файл 'bitly_token.env' и запишите туда ваш ключ 'BITLY_TOKEN=*ваш ключ*' 
5. Сохраните файл в том же репозитории что и файл main.py
6. Запустите скрипт

### Как запустить

1. Используя консоль запустите скрипт через команду: ```python *название_файла* *URL*```
прим. ```*PS C:\Users\User\Desktop\project 3\project-3> python main.py https://bit.ly/3vhW4DB*```
2. Если не получается запустить через команду попробуйте открыть проделать путь до корневой папки репозитория со всеми файлами либо откройте её в вашем текстовоме редакторе, для пользователей Visual Studio Code достаточно открыть папку репозитория в explorer.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).