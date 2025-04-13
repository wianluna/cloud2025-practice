1. Загрузить образ в Minikube
    ```
    docker build -t moviebucket-app .
    minikube start
    minikube image load moviebucket-app
    ```

2. Развёртывание в Kubernetes
    ```
    kubectl apply -f deployment.yaml
    ```

3. Доступ к приложению
    ```
    minikube service moviebucket-service
    ```

➕ Добавить фильм

    ```
    curl -X POST http://192.168.49.2:32356/add \
        -H "Content-Type: application/json" \
        -d '{"title": "Inception", "genre": "Sci-Fi"}'
    ```

✅ Отметить как просмотренный
    ```
    curl -X POST http://192.168.49.2:32356/mark_watched \
        -H "Content-Type: application/json" \
        -d '{"title": "Inception", "genre": "Sci-Fi", "rating": "5"}'
    ```

📄 Получить все фильмы

    ```
    curl http://192.168.49.2:32356/to_watch/Sci-Fi
    ```


    curl http://192.168.49.2:32356/random/Sci-Fi


