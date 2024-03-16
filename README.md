# Технологии виртуализации (Kubernetes)

#### Установка необходимого программного обеспечения

##### Docker

Для создания контейнеров понадобится Docker, который также можно установить с официального сайта: https://www.docker.com/

##### Minikube

Установка minikube с официального сайта: https://kubernetes.io/ru/docs/tasks/tools/install-minikube/

![Установка minikube](/res/1.png)

При возникновении ошибки `Unable to resolve the current Docker CLI context "default": context "default"`, нужно воспользоваться командой `docker context use default`

![Unable to resolve the current Docker CLI context "default": context "default"](/res/2.png)

##### Kubectl

Установить kubectl можно по инструкции: https://kubernetes.io/ru/docs/tasks/tools/install-kubectl/#установка-kubectl-в-linux

В моем случае, я заменил файл `kubectl.exe`, установленный Docker-ом (путь к нему можно узнать из переменной среды `PATH` в Windows), файлом `kubectl.exe`, скаченном из инструкции

В настройках Docker необходимо включить Kubernetes

![](/res/5.png)


##### Kubernetes Dashboard

Kubernetes Dashboard - удобный инструкмент для получения сведений о состоянии кластера Kubernetes и базового управления им

Инструкция по установке (настройке) Dashboard UI: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

Dashboard настраивается для запущенного контейнера minikube

![](/res/6.png)
В [этой](https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md) инструкции описано - что необходимо сделать для получениия доступа к Dashboard UI. Необходимо применить манифест `ui-access.yml`, находящийся в корне проекта при помощи команды `kubectl apply -f .\ui-access.yml`

![](/res/7.png)

Затем при помощи команды `kubectl -n kubernetes-dashboard create token admin-user` извлечь т.н. барьерный токен для ранее созданного (при помощи `ui-access.yml`) сервисного аккаунта

Далее - выполнить команду `kubectl proxy`, перейти по ссылке Dashboard `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/` и ввести ранее полученный токен

![](/res/8.png)

#### Запуск

Запуск Minikube производится при помощи команды `minikube start --driver=docker`

![Запуск Minikube](/res/3.png)

Как итог этого шага - запущен контейнер minikube в Docker
![](/res/4.png)

Команда логина в docker hub: `docker login -u selvnv` (использовать Access Token из Docker Hub)

Сборка образа выполняется командой: `docker build -t selvnv/vtech:1.0 .`

Загрузка образа в docker hub: `docker push selvnv/vtech:1.0`

Можно стянуть этот образ: `selvnv/vtech:1.0`

После чего применить манифест Deployment-а: `kubectl apply -f deployment.yml`

Затем манифест Service-а (для доступа к приложению в контейнерах): `kubectl apply -f service.yml`

Для того, чтобы обращаться к приложениям, сначала нужно узнать ip-адрес: `minikube ip`

И приписать к нему порт Service:
![](/res/10.png)