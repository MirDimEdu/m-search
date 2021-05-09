# m-search
Микросервис поиска по постами и эвентам


# Установка
1) Создать и активировать venv.
2) Установить все зависимости из requirements.txt.
3) Установить docker.

# Запуск
Сначала необходимо запустить mongodb, для этого в корне проекта нужно выполнить

    docker compose up --build -d mongodb

Остановить монгу можно через 

    docker compose stop

Сбросить состояние базы 

    docker compose stop && docker compose rm

Имя базы/пароль можно изменить в файле scripts/mongo-init.js

Запуск самого приложения для разработки:

    uvicorn search:app

# Конфигурация
В файле config.yaml необходимо указать параметры подключения к mongodb
и имена коллекций в которых нужно хранить данные

`mongodb_post_collection` - коллекция для постов.
`mongodb_event_collection` - коллекция для эвентов.