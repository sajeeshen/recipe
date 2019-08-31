# recipe


## Installation

Clone the git and go the the app folder and run the 
following command 

```bash
docker-compose build 
```

Then run makemigrations 

```bash
docker-compose run app sh -c "python manage.py makemigrations"

```
Then migrate 

```bash
docker-compose run app sh -c "python manage.py migrate"

```
Create Super Admin

```bash
docker-compose run app sh -c "python manage.py createsuperuser "

```

Then run 

```bash
docker-compose up
```
