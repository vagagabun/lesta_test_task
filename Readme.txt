Требования для запуска: 
-- Docker
-- Docker-compose


Первое задание:
docker build -t flask-app .
docker run -p 5000:5000 -d flask-app
Проверка работоспособности: curl http://localhost:5000/ping

Второе задание:
docker-compose up --build --detach
Проверка работоспособности: curl http://localhost:5000/count

Удаление и остановка контейнеров:

Первое задание: Посмотреть ID с помощью команды docker ps, а затем остановить его
c помощью docker kill. Затем удалить данный контейнер с помощью docker rm, далее удалить
его образ с помощью docker rmi. Глянуть ID образа можно с помощью docker images.

Второе задание: Для остановки всех сервисов выполните команду docker-compose down. Если необходимо
удалить созданный образ Flask-приложения, выполните команду docker rmi.
