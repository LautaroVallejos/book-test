# Instrutions for run the project with docker-compose (Windows and other OS)
## 1. Clone the repo.
## 2. Enter in 'book-test/' directory: `cd book-test/`.
## 3. Run docker-compose file: `docker-compose up`.

# Instructions for run the project without docker-compose (Linux based OS)
## 1. Clone the repo.
## 2. Enter in 'book-test/' directory: `cd book-test/`.
## 3. Create a virtual enviroment: `virtualenv venv`, and activate it: `source venv/bin/activate`.
## 4. Install dependencies: `pip install -r requierments.txt`.
## 5. Run the server: `python manage.py runserver`.

# Instructions for Testers
By default the application comes with authentication by bearer token, if you want to disable it for a better visualization from the browser you can do it from _Dadmin/settings.py_ uncommenting _line 142_.

When starting the program there is the /api section where you access all the system information, however to access this you must be authenticated with the access_token which is obtained from an authenticated user.

__Valid credentials:__
User: fulltester
Pass: notSecureChangeMe

_(I recommend using an api rest client like Postman or Insomnia to test the API)_

Once you get the access_token you must pass it in the request as bearer token on postman or insomnia. Then you can make get, post and other requests sending the data by json from the rest client completing the corresponding fields.

_(I recommend that when creating new items and testing the api you use the unauthenticated option (from Dadmin/settings.py uncommenting line 142) to avoid constantly passing the token.)_