# Fampay Assignment  
# About Project
An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for music query in a paginated response.
## Basic Requirements
- Server should call the YouTube API continuously in background (async) with some interval (5 minutes) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimised.
## Task For Bonus Points
- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`.
## Instructions:
- Chose <b>music</b> search query
- Preferred language & Framework
    1. Python (DRF, Django, Flask)
## Reference:
- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: q=music, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old.
    
# How to setup on local machine(Linux/macOS)?
## Without Docker 

- Clone the repository  
```
$ https://github.com/todi-2000/Fampay_Assignment/
```  

- Change the directory  
```
$ cd Fampay_Assignment
```  

- Create a virtual environment and activate it.
``` 
$ python3 -m venv .env 
$ . .env/bin/activate
```  

- Install all the dependencies
```
$ pip install -r requirements.txt 
```

- Install redis and start redis server(macOS)
```
$ brew install redis
$ redis-server
```

- Install redis and start redis server(Linux)
```
$ sudo apt install redis
$ redis-server
```

- Run migrations
```
$ cd fampay_task
$ python manage.py migrate
```

- Create a superuser to access the admin panel
```
$ python manage.py createsuperuser
```

- Run the server
```
$ python manage.py runserver
```

- Open the admin panel, and add API key [here](http://127.0.0.1:8000/admin/youtube_search/apikey/) or use API `POST /api/apikey/`

- Open a new terminal tab and go to the same path as before and activate the same environment
- Run Celery worker using the following command
```
$ celery -A fampay_task worker --beat --scheduler django --loglevel=info
```

Videos fetched from youtube and stored in db can be displayed by visiting `http://127.0.0.1:8000/api/videos/list/` in your browser.

## With Docker(Recommended):

 - Clone the repository using git clone and change directory
 ```
$ git clone https://github.com/todi-2000/Fampay_Assignment
$ cd Fampay_Assignment/fampay_task
```

- Change the permissions for entrypoint.sh  
```
$ chmod 775 entrypoint.sh
```

- Create and start the container.
```
$ docker-compose up -d --build
```

- Add appropriate key using same steps as above.
<b>The server will start on port 8000, API usage same as above.</b>

- In case of any errors for port already in use, run the following scripts to kill all running processes.
```
$ chmod 775 ./docker-fresh-start.sh
./docker-fresh-start.sh
```

# API Endpoints  
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
```
GET http://127.0.0.1:8000/api/videos/list/
```

- A basic search API to search the stored videos using their title and description.
```
GET http://127.0.0.1:8000/api/videos/list/?search=<query> 
```

- An API to GET the list of stored API Keys
```
GET http://127.0.0.1:8000/api/apikey/
```

- An API to save the key in database.  
```
POST http://127.0.0.1:8000/api/apikey/

Request Body
{
"key": <string>
}
```
