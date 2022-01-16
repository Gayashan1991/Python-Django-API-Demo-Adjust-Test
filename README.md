# AdjustTest
 Django project for several test api callings

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.
Dataset is expected to be stored and processed in a relational database.

Client of this API should be able to:

   filter by time range (date_from+date_to is enough), channels, countries, operating systems
   group by one or more columns: date, channel, country, operating system
   sort by any column in ascending or descending order
   see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

Prerequisites:

1. for virtual environment
  
  ```python -m venv <envname>``` 
 
2. install following libraries

  ```pip install django```
  
  ```pip install djangorestframework```
  
  ```pip install pandas```
  
3. run local server

  ```python manage.py runserver```

Test Scenarios:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

 ```    
 http://127.0.0.1:8000/adjustapi/?groupb=channel&groupb=country&dateb=2017-06-01&sum=impressions&sum=clicks&orderb=clicks&desc=true
 ```


2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
```
http://127.0.0.1:8000/adjustapi/?groupb=date&orderb=date&datef=2017-05-01&datet=2017-05-31&os=ios&sum=installs
 ```


3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
```
http://127.0.0.1:8000/adjustapi/?groupb=os&dateb=2017-06-01&country=US&orderb=revenue&desc=true&sum=revenue
 ```


4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
```
http://127.0.0.1:8000/adjustapi/?groupb=channel&conutry=CA&isCpi=cpi&sum=spend&orderb=cpi&desc=true
 ```
