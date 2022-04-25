





**Title**
----
  *Getting crawl Data of any specific website use get method.*

* **URL**

  http://14.140.15.88:8002/crawl/searchUrlAPI/

* **Method:**
  
  <_The request type_>

  `GET` 
  
*  **URL Params**

   url

   **Required:**
 
   `url=[string]`

   

* **Data Params**

  http://14.140.15.88:8002/crawl/searchUrlAPI/?url=darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion/

* **Success Response:**
  {
    "message": "Record fetch successfully",
    "status": true,
    "data": [
        "6266624b2b2b086f11447d4e"
    ]
}

  * **Code:** 200 <br />

 
* **Error Response:**

  {
    "message": "Record Already fetch",
    "status": true,
    "data": [
        "62666276c4631b57afdaf2a7"
    ]
}
  * **Code:** 409 ALREADY EXISTS <br />
    **Content:** `{ error : "Record Already fetch" }`

  OR
  {"error" : "Url not found", "status": False, "data": []}

  * **Code:** 400  BAD REQUEST <br />
    **Content:** `{ error : "Email Url" }`

 **Title**
----
  *Getting data from ids of any specific website (which is crawled previously) use get method.*

* **URL**

  http://14.140.15.88:8002/crawl/getDataById/

* **Method:**
  
  <_The request type_>

  `GET` 
  
*  **URL Params**

   id

   **Required:**
 
   `id=[string]`

   

* **Data Params**

  http://14.140.15.88:8002/crawl/getDataById/?id=626642e5aa2da0381bd8cf91

* **Success Response:**
  {
    data[
        {
            "_id": "626642e5aa2da0381bd8cf91",
            "url":"darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion",
            "title":['Darknetlive', 'Darknetlive','...'],
            "link":['http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion/','...'],
            "content":['A Florida woman was sentenced to more than six years in federal prison for attempting to hire a hitman on the darkweb.','...'],
            "email":[],
            "bit_coin":['Crypto http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion/crypto/','....'],

        }
    ]
}

  * **Code:** 200 <br />

 
* **Error Response:**

  {"error": "obj does not exists", "status": False, "data": []}
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "obj does not exists" }`

  OR
  {"error": "please entry valid id", "status": False, "data": []}

  * **Code:** 400  BAD REQUEST <br />
    **Content:** `{ error : "Invalid id" }`

 
**Title**
----
  *Getting all ids and urls (which is crawled previously) use get method.*

* **URL**

  http://14.140.15.88:8002/crawl/getAllIds/

* **Method:**
  
  <_The request type_>

  `GET` 
  
*  **URL Params**

   None

   **Required:**
 
   None

   

* **Data Params**

  http://14.140.15.88:8002/crawl/getAllIds/

* **Success Response:**
  {
    "message": "Record Retrieve Successfully",
    "status": true,
    "data": [
        {
            "_id": "626642e5aa2da0381bd8cf91",
            "url": "darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion"
        }
    ]
}

  * **Code:** 200 <br />

 
* **Error Response:**

  {"error":"Database Empty","status": False, "data": []}}
  * **Code:** 204 NO CONTENT <br />
    **Content:** `{ error : "Database Empty" }`
