**Get User Exists**
----
Returns user object if a user exists and empty json otherwise

* **URL**

  /users/api/v1.0/exists/<userid>

* **Method**

  `GET`

* **URL Params**

  **Required:**

  `userid=[integer]`

* **Data Params**

  None

* **Response**

  * **Code:** 200 <br />
    **Content:**
    If user exists:
    ```json
    { 
      "user_id": 2,
      "full_name": "Victor Par",
      "phone_number": "604-384-3483",
      "credit": 40.30,
      "email": "testing@testing.com",
      "restaurant_id": 30483,
      "table_id": 34893,
      "role": 0 (0 if customer, 1 if waiter)
    }
    ```
    If user does not exists:
    ```json
    {
    }
    ```

**Get User Object**
----
Returns user object from userid

* **URL**

  /users/api/v1.0/<userid>

* **Method**

  `GET`

* **URL Params**

  **Required:**

  `userid=[integer]`

* **Data Params**

  None

* **Response**

  * **Code:** 200 <br />
    **Content:** `TODO: USER OBJECT JSON`

**Post new User Object**
----
Makes new user object from request json

* **URL**

  /users/api/v1.0/register

* **Method**

  `POST`

* **URL Params**

  None

* **Data Params**

    ```json
    { 
      "user_id": 2,
      "full_name": "Victor Par",
      "phone_number": "604-384-3483",
      "credit": 40.30,
      "email": "testing@testing.com",
      "restaurant_id": 30483,
      "table_id": 34893,
      "role": 0 (0 if customer, 1 if waiter)
    }
    ```

* **Response**

  * **Code:** 200 <br />
    **Content:**
    ```json
    { 
      "user_id": 2,
      "full_name": "Victor Par",
      "phone_number": "604-384-3483",
      "credit": 40.30,
      "email": "testing@testing.com",
      "restaurant_id": 30483,
      "table_id": 34893,
      "role": 0 (0 if customer, 1 if waiter)
    }
    ```

**Put new table id in user Object**
----
Puts new table id in user object

* **URL**

  /users/api/v1.0/

* **Method**

  `PUT`

* **URL Params**

  None

* **Data Params**

    ```json
    { 
      "user_id": 2,
      "table_id": 34893
    }
    ```

* **Response**

  * **Code:** 200 <br />
    **Content:**
    ```json
    { 
      "user_id": 2,
      "table_id": 34893
    }
    ```

