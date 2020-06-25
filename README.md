
# StockMoon Project Reference

As of this writing, the following API endpoints exist: 
##### `/API/token/`- returns two jwt tokens used for user authentification.
        HTTP Methods: POST
        HTTP codes: 200, 400, 401
        no jwt auth required
- Parameters
    `username`: username of an existing user
    `password`: password for that user
- Response
    -  **If the user exists and the password is correct**, you will get a   
        ```javascript
        200 OK,{    
            "refresh": "refresh_jwt",     
            "access": "access_jwt"
        }
        ```
     1) `access_jwt` can be used to access other api features and endpoints
      (`/article/,/auth/users/`,etc).
     2) `refresh_jwt` is used to obtain a new `access_jwt`.
    To accomplish this, send a `POST ` request to `/API/token/refresh/`.
    
    - **If you have supplied bad credentials**, the server will give you a 
    `401 Unauthorized` and return a `JSON` that looks like this:
        ```
            {
            "detail":"No active account found with the given credentials"
            }
        ```
    - **If no credentials are supplied**, the server will give you a
        ```javascript 400 Bad Request, 
        {    
        "username": ["This field is required."],  
         "password": ["This field is required."]
        }
        
---
##### `/API/token/refresh/` - returns a new access jwt token. 
        HTTP Methods: POST
        HTTP codes: 200, 400, 401
        refresh token required
    
- Parameters
    - refresh -  refresh jwt token obtained via `/API/token/`.
- Response
    - **If a token is valid** the server will send you a `200 OK` and a new access token:
        ```javascript
       {
        "access": "access_jwt"
        }
        ```
    - **if no token is provided**, you will get a following response: 
        ```javascript 
        400 Bad Request, 
        {
            "refresh":["This field is required."]
        }
        ```
    - **If the token is corrupted or has expired**, you will get a
        ```javascript
        401 Unauthorized, 
        {
            "detail": "Token is invalid or expired",
            "code": "token_not_valid"
        }
        ```
---
##### `/API/article/` -  returns a list of all available articles.
        HTTP Methods: GET
        HTTP codes: 200,401
      	access token required
- Parameters
    No parameters required, though you have to authorize with a jwt access token.
- Response
    - **if the token is valid**, the server will give you a `200 OK` and a list of all existing articles with the attributes as shown here:
        ```javascript
        [   
            {      
            "url":"http://localhost:8000/API/article/1/",
            "title":"An Example Article",
             "category":[
                 "Some category"
                ],
              "source":"google.com",
              "content":"Lorem ipsum dolor sit amet",
              "date_posted":"2020-04-03T19:47:44Z",
              "image":"cute_cat.jpg"
            }
        ]   
        ```
    - **If the token is invalid** (expired of broken), the server will give you a `401 Unauthorized` and the following `JSON`:   
    ```javascript
      {   
         "detail": "Given token not valid for any token type",   
         "code": "token_not_valid",   
          "messages": 
          [ 
              {            
                  "token_class": "AccessToken",       
                  "token_type": "access",      
                  "message": "Token is invalid or expired"    
              }    
          ]
        }
    ```
---
##### `/API/auth/users/` -  adds a new user to the database.
        HTTP Methods: POST,GET
        HTTP Codes: 200,201,400,401    
        access token required(GET Request)
- Parameters
    `username` - new user\`s username
    `password` - new user\`s password
    `email` - new user\`s email
    
- **POST Request**
  - Response
      - **If the user with this username does not exist yet** , you will get a   
          `201 Created` and a `JSON` with the user\`s personal details:
          ```javascript
          {    
              "email": "helloworld@fake.com",   
              "username": "user6",    
              "id": 6
          }
          ```
      - **If the username already exists**, the server will throw a `400 Bad Request` and return a 
          ```javascript
          {"username": ["A user with that username already exists."] }
          ```
- **GET Request**  
Access JWT token is required and no parameters need to be supplied. If a token is valid, you will get a `200 OK` and a list of all existing users, including admins:
```javascript
[
    {
        "email": "email1@random.site",
        "id": 1,
        "username": "root"
    },
    {
        "email": "email2@random.site",
        "id": 2,
        "username": "user2"
    },
]
```
---
##### `/API/auth/users/me` -  get info about a specific user.
      HTTP Methods: GET
      HTTP Codes: 200,401    
      access token required
- Parameters
No parameters required except for the JWT token.  
- Response
If your token is valid, you will get a `200 OK` and a `JSON` with your user details:
	```javascript 
	{
		"email": "user7mail@random.site",
		"id": 7,
		"username": "user7"
	}
If you provide an invalid or expired token, you will get a `401 Unauthorized` and a following `JSON`:
```javascript
{
	"detail": "Given token not valid for any token type",
	"code": "token_not_valid",
	"messages": [
		{
			"token_class": "AccessToken",
			"token_type": "access",
			"message": "Token is invalid or expired"
		}
	]
}
```
If token is not provided, the server will throw a `401 Unauthorized`.
---
# Jenkins and Docker deployment and setup procedure.
    In this manual it is layed out how to setup  Jenkins and Docker on a  server and deploy our environment onto the server. 
    A quick guid on how to interact with  docker containers and volumes is present in this section too.
### Step 1: Install Docker
Refer to Docker documentation located [here](https://docs.docker.com/engine/install/ubuntu/).
### Step 2: Install and pre-configure Jenkins
RTFM [here](https://jenkins.io/doc/book/installing/#debianubuntu). By default, Jenkins is running on http://localhost:8080. You have to install the following plugins in order to be able to proceed:
    - __[Git Plugin](https://plugins.jenkins.io/git/)__
    - __[Github Plugin](https://plugins.jenkins.io/github/)__
### Step 3: Configure Jenkins to play nice with Docker
If you try to execute a docker command inside jenkins, you will get an error saying that a docker server is not accessible. In order to fix this issue, you have to add a `jenkins` user to the `docker` group and make docker server listen on a specific port. To do that, run `sudo gpasswd -a jenkins docker`. Next step is to edit docker service config file(`/usr/lib/systemd/system/docker.service
`) with your favourite text editor and append `-H tcp://localhost:2375` at the end of the `ExecStart` line. Now, you have to reload daemon config files with `sudo systemctl daemon-reload` and restart Docker and Jenkins: 
`sudo systemctl restart docker && sudo systemctl restart jenkins`.
### Step 4: Add a new Jenkins build Job
Go to Jenkins dashboard, select `New item`, choose a `Freestyle project` option and enter a job name. Scroll down to the `Source Control Management` section, select `Git` and add a repository url, your credentials and a branch to clone. 

__Disclaimer__
Since at the time of this writing I was not able to set up a proper webhook-triggered job, this guide shows how to create a simple polling job that checks a repo once in so while. Although when we will have a public  IP address for Jenkins to run on, this documentation page will be changed to fit.
__Disclaimer ended__

Next you need to go to the `Build triggers` section and tell Jenkins to  `Poll SCM`. You have to provide a `cron-like` schedule for Jenkins to check a repo on a specific time  intervals.
[Cron string documentation](https://support.acquia.com/hc/en-us/articles/360004224494-Cron-time-string-format)

### Step 5: Add a build script
Scroll down to `Build` section, click on `Add build step` and add a new `shell` step. Next, add the following lines to the `Command` input field:
```
chmod +x ./jenkins-buildscript.sh
./jenkins-buildscript.sh
```
This will run a script that is going to build three Docker containers that you can see if you run `docker ps`:
- `$JOB_NAME_web` - a Django container with a gunicorn wsgi server running on port 8000. This port is exposed only to these three containers.
- `$JOB_NAME_nginx` - an Nginx container that acts as a reverse proxy for our gunicorn server and serves static files and media.
- `postgres` - a PostgreSQL Server.
### Overview of Docker volumes used by Docker containers
A `Docker volume` is a tool that allows for data persistence. 
Conceptually it works just like a USB drive or any other persistent storage device - you can mount it wherever you want and later access it with your typical linux tools such as `ls, vim` and others. Currently there are three `Docker volumes` used by the aforementioned containers:
- `nginx_logs_volume` - correspons to the `/var/log/nginx` directory and stores all of the nginx logs.
- `static_volume` - stores Django static files and is used in order for Nginx to be able to access them, since Django and Nginx are running in different containers.
- `media_volume` - stores Django media files.

__To get all mounted volumes__, run `docker volume ls`. 
__To remove a specific volume__, run `docker volume rm volume_name`
__To inspect a specific volume__, run `docker volume inspect volume_name`
If you want to interact with the files stored in that volume, go to the `Mountpoint` directory.
