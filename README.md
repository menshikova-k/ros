Тестовое задание (запустить и описать то, что делает код, переписать в виде ROS нод со входом через REST).
Этот проект - система логирования с использованием REST API. 
При запуске программ в командной строке выводятся логи (
INFO:     Started server process [7] (процессы были запущенны)
INFO:     Started server process [8]
INFO:     Waiting for application startup. (сервер ожидает завершения процесса)
INFO:     Waiting for application startup.
INFO:     Application startup complete. (приложение успешно отработало)
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit) (указаны порты, по которым приложение доступно)
INFO:     Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit) ), 
которые выводятся при запуске серверного процесса с помощью Uvicorn.

Обновленный код содержит две ноды "logger_node" и "listener_node" с возможностью получения данных через REST API.
