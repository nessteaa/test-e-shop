Необходимые шаги для инсталляции:
pip install -r requirements.txt

Команды для запуска сервиса:
python3 -m venv myvenv
source mevenv/bin/activate
export FLASK_ENV=development
python3 app.py

Тестовый сценарий:

Заполнение БД тестовыми данными:
mongoimport --db shop --collection Products shop_script.json

1. Создать новый товар:

curl -X POST -H "Content-Type: application/json" -d '{"name": "iPhone X", "description": "Phone", "parameters": {"manufacturer": "Apple", "country": "China", "storage": 128, "mpix": 8}}' localhost:5000/add/

2. Получить список названий товаров с возможностью фильтрации по:

а) названию

curl -X GET localhost:5000/search_name/

curl -X POST -H "Content-Type: application/json" -d '{"name": "iPhone X"}' localhost:5000/search_name/

б) выбранному параметру и его значению

curl -X GET localhost:5000/search_parametr/

curl -X POST -H "Content-Type: application/json" -d '{"parameters": {"screen": 6.1}}' localhost:5000/search_parametr/

