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
data: [
        {
            "distance": <INTEGER VALUE (in km)>,
            "price": <INTEGER VALUE (in Rs)>
        },
        {
            "distance": <INTEGER VALUE (in km)>,
            "price": <INTEGER VALUE (in RS)>
        },
    ]
enabled : <STRING VALUE ("true"/"false")>
```

### Update DBP
Post on following endpoint to create a DAP

```
http://127.0.0.1:8000/update_DBP
```

Make sure to add following form data 

```
id : <INTEGER VALUE (id of DBP)>
data: [
        {
            "distance": <INTEGER VALUE (in km)>,
            "price": <INTEGER VALUE (in Rs)>
        },
        {
            "distance": <INTEGER VALUE (in km)>,
            "price": <INTEGER VALUE (in RS)>
        },
    ]
enabled : <STRING VALUE ("true"/"false")>
```


### Create TMF
Post on following endpoint to create a TMF

```
http://127.0.0.1:8000/new_TMF
```

Make sure to add following form data 

```
data: [
        {
            "time": <INTEGER VALUE (in hrs)>,
            "price": <INTEGER VALUE (in Rs)>
        },
        {
            "time": <INTEGER VALUE (in hrs)>,
            "price": <INTEGER VALUE (in RS)>
        },
    ]
enabled : <STRING VALUE ("true"/"false")>
```

### Update TMF
Post on following endpoint to create a DAP

```
http://127.0.0.1:8000/update_TMF
```

Make sure to add following form data 

```
id : <INTEGER VALUE (id of TMF)>
data: [
        {
            "time": <INTEGER VALUE (in hrs)>,
            "price": <INTEGER VALUE (in Rs)>
        },
        {
            "time": <INTEGER VALUE (in hrs)>,
            "price": <INTEGER VALUE (in RS)>
        },
    ]
enabled : <STRING VALUE ("true"/"false")>
```

### Create DAP
Post on following endpoint to create a DAP

```
http://127.0.0.1:8000/new_DAP
```

Make sure to add following form data 

```
value : <INTEGER VALUE (in Rs)>
enabled : <STRING VALUE ("true"/"false")>
```

### Update DAP
Post on following endpoint to create a DAP

```
http://127.0.0.1:8000/update_DAP
```

Make sure to add following form data 

```
id : <INTEGER VALUE (id of DAP)>
value : <INTEGER VALUE (in Rs)>
enabled : <STRING VALUE ("true"/"false")>
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
```

Return Value: 

```
{
    "id": <ID>,
    "total_distance": <INTEGER VALUE (in Km)>,
    "total_time": <INTEGER VALUE (in hours)>,
    "total_price": <INTEGER VALUE (in Rs)>
}
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

