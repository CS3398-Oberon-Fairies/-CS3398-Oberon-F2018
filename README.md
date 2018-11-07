# Priority Parking

is a web-based application that will be used by students, teachers, or just 
regular people to make parking less of a hassle. The app will show an 
interactive map of the campus parking lots and actively show which parking spots 
are open or taken. It will also give users the option to let it be known when 
they are leaving a certain parking spot, so others will know that a spot will 
be available soon.

### STATUS:

# Sprint 1

*We completed almost all of the tasks that we had planned, and the app works as
expected.*

The web app is currently complete. It needs to be run local, however. Once the DB
has been imported into MySQL (./DB/parkinglot.sql into a database called `pp`), 
the API needs to be started with the command `python api/main.py test`. Then the 
frontend (./front-end/prioritypark.html) should be able to connect to the API.

# Sprint 2

*Completed all tasks that we planned, and the new features we added work*

The web app still runs locally, and requires the same steps from the first sprint to run.
The Login and registration pages correctly call the API to create user and session entries 
in the Database. The Report functions also correctly call the API to create report entries 
in the Database.
Database server is up and ready to keep data synchronized across all users. It still needs to be implemented in code


#### Building:

No building neccessary. Every team member had to install python3 with all
dependencies to run the API, as well as MySQL for the DB. 

    - flask
    - json
    - mysql-connector
    

#### Goals:

- Alex: Create user feedback and improve design to support mobile
- Patrick and ?: Extend the API for more features (such as social parking spot 
    reports of full lots, etc).
- Rogelio: Finalize importing parking spots to DB from OSM.
- Gary: Help Alex with front-end and make changes with database whenever needed. Study up on JavaScript before next Sprint

#### Parts:

- Alex: ./front-end/*
- Gary: ./DB/parkinglot.sql && ./DB/Main.mwb && ./DB/Server site 
- Rogelio: ./DB/caching_san_marcos_parking_info/*
- Patrick: ./api/*
