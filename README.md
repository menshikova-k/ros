Тестовое задание (запустить и описать то, что делает код, переписать в виде ROS нод со входом через REST).
Этот проект - система логирования с использованием REST API. 
При запуске программ в командной строке выводятся логи ( <br>
INFO:     Started server process [7] (процессы были запущенны) <br>
INFO:     Started server process [8] <br>
INFO:     Waiting for application startup. (сервер ожидает завершения процесса) <br>
INFO:     Waiting for application startup. <br>
INFO:     Application startup complete. (приложение успешно отработало) <br>
INFO:     Application startup complete. <br>
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit) (указаны порты, по которым приложение доступно) <br>
INFO:     Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit) ), <br>
которые выводятся при запуске серверного процесса с помощью Uvicorn. <br>

Обновленный код содержит две ноды "logger_node" и "listener_node" с возможностью получения данных через REST API.
