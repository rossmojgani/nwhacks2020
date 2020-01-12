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

  /users/api/v1.0/user_id

* **Method**

  `PUT`

* **URL Params**

  user_id

* **Data Params**

    ```json
    { 
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

**Post new transaction**
----
Makes new transaction object from request json

* **URL**

  /users/api/v1.0/new_transaction

* **Method**

  `POST`

* **URL Params**

  None

* **Data Params**

    ```json
    {
      "user_id": 2,
      "ammount": 100.00,
      "restraunt_id": 5,
      "table_id": 34893,
      "date": "01-12-2020",
      "time": "15:34"
    }
    ```

* **Response**

  * **Code:** 200 <br />
    **Content:**
    ```json
    { 
      "user_id": 2,
      "ammount": 100.00,
      "restraunt_id": 5,
      "table_id": 34893,
      "date": "01-12-2020",
      "time": "15:34"
    }
    ```
    
    
 **Get User Transaction History**
----
Returns transaction objects if a user's transaction history exists and empty json otherwise

* **URL**

  /users/api/v1.0/transaction_history/<userid>

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
    ```jsonhttps://docs.mongodb.com/manual/reference/method/db.collection.find/
    { 
      "user_id": 2,
      "ammount": 100.00,
      "restraunt_id": 5,
      "table_id": 34893,
      "date": "01-12-2020",
      "time": "15:34"
    }
    { 
      "user_id": 2,
      "ammount": 150.00,
      "restraunt_id": 55
      "table_id": 343,
      "date": "01-12-2020",
      "time": "19:34"
    }
    ```
    If user does not exists:
    ```json
    {
    }
    ```
