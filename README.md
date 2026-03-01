# Client-Server-Development

Najah Thompson 

CS 340 Project Two: Grazioso Salvare Dashboard 

Developer: Najah Thompson 

Project Functionality 

The main goal of this project was to build a functional, interactive web dashboard for Grazioso Salvare, a rescue animal training company. The dashboard connects to a MongoDB database containing outcomes from the Austin Animal Center. It allows the user to filter through thousands of animal records to find dogs that fit specific profiles for search-and-rescue training (like Water Rescue, Mountain/Wilderness Rescue, and Disaster Tracking). 

The dashboard includes interactive radio buttons that filter a data table. When the table updates, a pie chart automatically adjusts to show the breakdown of dog breeds currently on the screen, and a geolocation map drops a pin on the exact location of the specific dog selected in the table. 

Dashboard Execution & Proof of Functionality: 

1. Reset (Show All) 

 

This shows the default state of the dashboard with no filters applied, loading the unfiltered dataset. 

2. Water Rescue 

 

This shows the data filtered for Water Rescue candidates (Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland, Intact Female, 26-156 weeks old). 

3. Mountain or Wilderness Rescue 

 

This shows the data filtered for Mountain/Wilderness Rescue candidates (German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler, Intact Male, 26-156 weeks old). 

4. Disaster or Individual Tracking 

 

This shows the data filtered for Disaster Tracking candidates (Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler, Intact Male, 26-156 weeks old). 

Tools and Rationale 

MongoDB: I used Mongo as the main database (the "Model" in the MVC pattern). Since animal shelter records can be pretty messy and dont always have the exact same fields, a NoSQL document database was the perfect fit. Also, MongoDB uses BSON (which is basically JSON), meaning the data translates perfectly into standard Python dictionaries without needing heavy conversions. 

Dash (by Plotly): I used the Dash framework to build the View and Controller pieces of the web application. Dash is great because it lets you build full interactive web apps using just Python, without needing to write a ton of HTML, CSS, or JavaScript. The layout components handle the "View," and the @app.callback decorators act as the "Controller" to route data between the database, the table, and the charts. 

Pandas: Used to convert the raw database queries into dataframes, which are much easier to manipulate and feed into the Dash data table. 

Steps Taken to Complete the Project 

Database Connection: First, I made sure my CRUD_Python_Module.py file from Project One was working properly and hardcoded the aacuser credentials so it could authenticate with the local MongoDB instance. 

UI Layout (View): I set up the basic layout using Dash HTML components, adding the Grazioso Salvare logo and my unique identifier to the header. I also initialized the Data Table, Pie Chart, and Leaflet Map placeholders. 

The Controller & Callbacks: I wrote a callback function tied to the radio buttons. Depending on which button is clicked, it builds a specific JSON query and passes it to the MongoDB read() method. 

Dynamic Updates: I wired up two more callbacks so that whenever the data table updates, the pie chart grabs the new breed counts, and the map waits for a row to be clicked to extract the latitude and longitude coordinates. 

Challenges Encountered 

One major challenge I ran into was getting the Dash data table to render the MongoDB results without crashing. Dash tables require the data to be in a very specific, flat dictionary format. Every time I queried the database, MongoDB automatically returned the _id field, which is an ObjectID data type, not a standard string. Dash didn't know how to serialize this object, so the whole app would throw a background error and fail to load the table. 

To overcome this, I had to use Pandas to clean the data before passing it to the front end. I used the df.drop(columns=['_id'], inplace=True, errors='ignore') command right after querying the database. This stripped out the unreadable ObjectID and allowed the rest of the clean text data to populate the dashboard table perfectly. 

Resources Used 

Dash Documentation:  

MongoDB Python Driver (PyMongo):  

Pandas Dataframe Reference:  

Plotly Express Pie Charts:  

 

 

 
