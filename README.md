# Clouds_Virtualization_CMC_course
Приложение в рамках практического задания по курсу "Облачные вычисления и виртуализация информационных ресурсов"

# Описание
Приложение представляет собой Flask-клиент, посредством которого идёт общение с Redis БД (оба развертываются в докер-контейнерах)

Семанитика приложения - взаимодействие с условной базой данных музыкальных групп.
Поддерживаются два запроса:
* по адресу /albums - внесение в БД сведений об альбомах, выпущенных заданной музыкальной группой. Ожидается json файл с полями 'band' и 'album'.
     
    *Пример*: curl -X POST \<url\>/albums \
     -H "Content-Type: application/json" \
     -d '{"band": "Pantera", "album": "Vulgar Display of Power"}' 
* По адресу /albums/<band> - получение альбомов указанной группы по данным БД

    *Пример*: curl \<url\>/albums/Pantera 

# Запуск 

```
minikube start 
eval $(minikube docker-env)
docker build -t flask-app ./app
docker build -t redis ./redis
kubectl apply -f k8s_cfg.yaml
```

# Получение url
```
minikube service flask-app --url
```

Также можно сделать проброс портов и получить доступ к БД через localhost:
```
kubectl port-forward service/flask-app 5000:5000
```
