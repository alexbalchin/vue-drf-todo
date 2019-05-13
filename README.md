# Vue-drf-todo
## Simple Todo App build with Django Rest Framework and Vue.js

### Project setup

#### Create a virtualenv (optional)
```
virtualenv venv
source venv/bin/activate
```
#### Install python dependencies
```
pip install -r vue_drf_todo/requirements.txt
```
#### Add SECRET_KEY
```
vue_drf_todo/settings.py
```
#### run Django migrations
```
cd vue_drf_todo
python manage.py migrate
```
#### Install Frontend dependencies
```
cd frontend
npm install
```

### Run the app
#### Start django server
```
cd vue_drf_todo
python manage.py runserver
```
#### Start frontend development server with hot reloading
```
cd frontend
npm run serve
```
