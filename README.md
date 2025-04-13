# MovieBucket
MovieBucket — приложение для управления списком фильмов. Оно позволяет:
* Добавлять фильмы в список "к просмотру" по жанрам.

* Отмечать фильмы как просмотренные с рейтингом.

* Получать все фильмы по жанру или случайный фильм из списка.

## Установка и запуск MovieBucket в Minikube

### 1. **Загрузить образ в Minikube**

```bash
docker build -t moviebucket-app .
minikube start --driver=docker                      
minikube image load moviebucket-app
```

### 2. **Развертывание приложения**
```bash
kubectl apply -f deployment.yaml
```

### 3. **Доступ к приложению**

```bash
minikube service moviebucket-service
```

---

## Примеры использования

### **Добавить фильм**

```bash
curl -X POST http://<minikube-ip>:<port>/add \
     -H "Content-Type: application/json" \
     -d '{"title": "Inception", "genre": "Sci-Fi"}'
```

### **Отметить как просмотренный**

```bash
curl -X POST http://<minikube-ip>:<port>/mark_watched \
     -H "Content-Type: application/json" \
     -d '{"title": "Inception", "genre": "Sci-Fi", "rating": "10"}'
```

### **Получить все фильмы по жанру**

```bash
curl http://<minikube-ip>:<port>/to_watch/Sci-Fi
```

### **Получить случайный фильм по жанру**

```bash
curl http://<minikube-ip>:<port>/random/Sci-Fi
```
