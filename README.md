1. Загрузить образ в Minikube
    ```
    docker build -t moviebucket-app .
    minikube start
    minikube image load moviebucket-app
    ```

2. Развёртывание в Kubernetes
    ```
    kubectl apply -f k8s_config.yml
    ```

3. Доступ к приложению
    ```
    minikube service moviebucket-service
    ```

➕ Добавить фильм

    ```
    curl -X POST http://127.0.0.1:50344/add \
        -H "Content-Type: application/json" \
        -d '{"title": "Dune", "genre": "Sci-Fi", "status": "to_watch"}'
    ```

✅ Отметить как просмотренный
   
    ```
    curl -X POST http://127.0.0.1:50344/rate \
        -H "Content-Type: application/json" \
        -d '{"title": "Dune", "rating": 9}'
    ```

📄 Получить все фильмы

    ```
    curl http://127.0.0.1:50344/list
    ```