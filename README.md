<h1>E -Menu </h1>

<h3>Project dependencies:</h3>
<ul>
<li>Python 3.6</li>
<li>PostgreSQL 9+</li>
<li>Python packages:</li>
<li>atomicwrites==1.2.1</li>
<li>attrs==18.2.0</li>
<li>Django==1.11.15</li>
<li>django-filter==2.0.0</li>
<li>djangorestframework==3.8.2</li>
<li>djangorestframework-filters==0.10.2</li>
<li>more-itertools==4.3.0</li>
<li>pluggy==0.7.1</li>
<li>psycopg2==2.7.5</li>
<li>py==1.6.0</li>
<li>pytz==2018.5</li>
<li>six==1.11.0</li>
 </ul>
 <h3>Project installation:</h3>
 <ol>
 <li>Clone repo to desired location</li>
  <li>Create and activate python virtual environment (recommended) </li>
 <li>Install packages from requirements.txt</li>
      pip3 install -r requirements.txt
  <li> Configure PostgreSQL database creating user, database, table defined in settings.py or change it to yours.</li>
  <li> Migate data to your database </li>
      python manage.py migrate
  <li>Load inital data from -> initial_data.json</li>
      python manage.py loaddata initial_data.json
  <li>Run app</li>
      python manage.py runserver
   </ol>
