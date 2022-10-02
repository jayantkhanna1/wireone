# WireOne Project

This project was created as an assignment for wireone organization

## Installation : 

```
python -m venv ve
./ve/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Create DBP
Post on following endpoint to create a DBP

```
http://127.0.0.1:8000/new_DBP
```

Make sure to add following form data 

```
distance: <INTEGER VALUE (in Km)>
price : <INTEGER VALUE (in Rs)>
```

### Create TMF
Post on following endpoint to create a TMF

```
http://127.0.0.1:8000/new_TMF
```

Make sure to add following form data 

```
time: <INTEGER VALUE (in hours)>
factor : <Float VALUE>
```

### Get all Prices:

To get all prices use GET request on following endpoint

```
http://127.0.0.1:8000/get_price
```

### Get Price by Id:

To get price by ID use GET request on following endpoint

```
http://127.0.0.1:8000/get_price_by_id?id=<ID>
```

### Add new Price:

To add new price use POST request on following endpoint

```
http://127.0.0.1:8000/new_Price
```

Make sure to add following form data 

```
total_distance: <INTEGER VALUE (in Km)>
total_time : <INTEGER VALUE (in hours)>
dap : <INTEGER VALUE (in Rs)>
```


# For UI:

Got to following URL to use UI

```
http://127.0.0.1:8000/admin
```

To create an admin account:

```
python manage.py createsuperuser

<FILL NEEDED DETAILS>
```

