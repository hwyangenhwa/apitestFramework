
"""
 usage
  - get
   : headers = {'User-Agent': 'MyUserAgent/1.0'}
   : apicheck.get('https://www.example.com', headers=headers)
  
  - post
   : headers = {'User-Agent': 'MyUserAgent/1.0'}
   : data = {"name": "John", "username": "johndoe", "email": "john@example.com"}response = requests.post("https://jsonplaceholder.typicode.com/users", json=data
   : apicheck.post('https://www.example.com', headers=headers, data=json)
"""

from requests_func.apicheck import get
from requests_func.apicheck import post

data = {"id": "1"}
response = get("https://www.googles.com", json=data)
#response = apiCheck.post("https://jsonplaceholder.typicode.com/users")