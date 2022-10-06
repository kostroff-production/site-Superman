# Superman
### О приложении
Приложение «Superman» является динамическим сайтом, посвященному герою DC Superman.<br> 
К сайту подключено администрирование через установку прав доступа для пользователей.<br>
Администратор сайта может создавать, обновлять и удалять посты, так же 
отвечать в разделе FAQ. 
### Установка.
Предварительно установив все зависимости
и Docker, загрузите приложение на свой сервер через гит.<br> 
`git clone https://github.com/kostroff-production/site-Superman.git`<br> 
Активируем файл `entrypoint.sh` из директории с файлом.<br> 
`chmod +x ./entrypoint.sh`<br>
Сделайте сборку контейнера из директории с Docker файлом.<br>
`docker build .`<br>
Далее собираем docker-compose.<br>
`docker-compose up -d –build`
После приложение должно быть доступно, если все зависимости были установлены корректно.<br>
## Разделы сайта
### Стартовая страница
Стартовая страница выполнена в минималистичном стиле.<br>
Основная кнопка на странице - это кнопка “Promo”, при нажатии на которую запускается ролик о 
Superman.<br>
![start_page](screenshots/start_page.jpg)
### Раздел Историй
В разделе собраны известные статьи и истории о герое, выполненные в виде слайдов, которые можно открыть и почитать.
<br>
<br>
![history](screenshots/history.jpg)
<br>
<br>
![history_mobile](screenshots/history_mobile.png)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![history_mobile_detail](screenshots/history_mobile_detail.jpg)
### Раздел Фильмографии.
В раздел добавлены несколько сериалов и фильмов о Superman с их кратким описание и кнопкой просмотра.<br>
При нажатии на кнопку просмотра пользователь будет перенаправлен на сайт Кинопоиска.
<br>
<br>
![movies](screenshots/movies.jpg)
<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![movies_mobile](screenshots/movies_mobile.jpg)
### Раздел Ответов на вопросы.
В разделе FAQ пользователи через специализированную форму могут задавать свои вопросы о сайте и вносить предложения.<br>
Администратор сайта в последующем отвечает на вопросы пользователей, просмотреть ответ можно нажав на вопрос.
<br>
<br>
![faq](screenshots/faq.jpg)
