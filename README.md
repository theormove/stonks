
# StockMoon API Reference

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

