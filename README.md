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

# Sprint 3

The web app is capable of running on a server, but it must be manually restarted each day so we reverted it back to run locally. User feedback has been added to both the login page(incorrect/correct login notifications) and the map display page (when connected to api will show lots according to their name and whether or not they're full). The GUI for both the login and main html was updated to be suitable for mobile use.

#### Building:

No building neccessary. Every team member had to install python3 with all
dependencies to run the API, as well as MySQL for the DB. 

    - flask
    - json
    - mysql-connector
    
The "run.py" file may need to be updated to reflect the DB connection parameters. The API can now be run as:

    python run.py

Then `index.html` can be opened in the browser.

#### Notes:

While we tried to move the API to AWS, we decided to go with a free MySQL database. The downside to this was that the connection between the API and the DB reset once per day (given that the DB service is only intended for tests), resulting in the API having to be restarted before it can be used. The last change that was added, was due to us reverting the API location back to "localhost". 

#### Accomplishments:

- Alex: Made quality of life changes to the file 'login.html' which is located in the 'front-end' folder, the changes which I added are a confirm password box and multiple checks to prevent potential user errors from occuring and to give feedback. I also added 'popup.css' which is located in the 'front-end/css' and was used for creating user feedback.
- Patrick: Worked on the frontend and backend to display all the lots in an ordered list. When opened, the nearest lot is the assumed to be the target. Additionally made the list interactable with the map (as well as the other way around), meaning that lots can be selected as targets from the map and the list. Moved the API to AWS, so the app has a remote location to pull information from. 
- Rogelio: Worked on the frontend to and made changes to CS3398-Oberon-F2018/front-end/prioritypark.html to display the current status of each parking lot. Also, added a function to CS3398-Oberon-F2018/api/db/ReportInterface.py to return last reported time for a lot, but it did not make it on demo due to bugs. 
- Gary: Ported the app to work on mobile devices. I made the mobile logo a picture of our group’s moon which can be found in the frontend/pgicons-5c0029b8a2093 folder. I created the config.xml file in the front-end folder. This allowed me to figure out how to make stuff work on the mobile version. The mobile app can be downloaded using the QR code in QR folder. The app doesn’t work with IPhones because I need an apple developer code to put make it work for them. Also, the mobile app doesn’t connect to the database for reasons stated in the notes section. I used Phone Gap when making all this.


#### Next steps:

- Alex: 
- Patrick: 
- Rogelio: Fix the bugs so that the last reported time for each lot is displayed, and have the map markers change color based on the lot status
- Gary: Fix up some of the somewhat buggy features of the mobile app. Also make it smoother and more app-like



