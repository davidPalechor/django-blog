# Restaurant management
Web app for restaurant-based business.

# Run
* `docker-compose build`
* `docker-compose up`
* go to `localhost:8000`

# To Apply Migrations
* `docker exec -it django-restaurant_web_1 python manage.py migrate`
# To Create Superusers
* `docker exec -it django-restaurant_web_1 python manage.py createsuperuser`
* Complete all blank fields.
* Go to `localhost:8000/admin` and you should be able to login.

#Running Tests
`docker exec -it django-restaurant_web_1 python manage.py test`
