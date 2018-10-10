# Priority Parking

is a web-based application that will be used by students, teachers, or just 
regular people to make parking less of a hassle. The app will show an 
interactive map of the campus parking lots and actively show which parking spots 
are open or taken. It will also give users the option to let it be known when 
they are leaving a certain parking spot, so others will know that a spot will 
be available soon.

### STATUS:

*We completed almost all of the tasks that we had planned, and the app works as
expected.*

The web app is currently complete. It needs to be run local, however. Once the DB
has been imported into MySQL (./DB/parkinglot.sql into a database called `pp`), 
the API needs to be started with the command `python api/main.py test`. Then the 
frontend (./front-end/prioritypark.html) should be able to connect to the API.

#### Building:

No building neccessary. Every team member had to install python3 with all
dependencies to run the API, as well as MySQL for the DB. 

    - flask
    - json
    - mysql-connector
    

#### Goals:

- Improve front-end display to show more than just the location of parking lots.
- Extend the API for more features (such as social parking spot reports of full 
lots, etc).
- Finalize importing parking spots to DB from OSM.

#### Parts:

- Alex: ./front-end/*
- Gary: ./DB/parkinglot.sql && ./DB/Main.mwb
- Rogelio: ./DB/caching_san_marcos_parking_info/*
- Patrick: ./api/*
