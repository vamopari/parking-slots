# parking-slots

Installing Geo-Django dependencies.

```sh
sudo apt-get install gdal-bin libgdal-dev
sudo apt-get install python3-gdal
sudo apt-get install binutils libproj-dev
```
Install postgres and create user and database and change databsae settings accordingly in settings.py file.

Create python3 virual environment.

Run migrations.
```sh
python manage.py migrate
```

Create Super user with command `python manage.py createsuperuser`.

Login to admin portal.

Create application for Django OAuth Toolkit and set `client_id` and `client_secret` in settings.py file.


Go to url `localhost:<port>/swagger`.

Create new user using user registration API from swagger and use this user for further testing. `super user can also be used for testing purpose`

Create access token using login api from swagger.

Click on Authorize button in Swagger page and add `Bearer <access_token>` and click authorize. This will add access token for every request made via swagger. access_token will be removed if swagger page is reloaded.
