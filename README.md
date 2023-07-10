# Data-Warehouse-Project
A project created with the objective of turning a database of student information into a Data Warehouse as well as creating a GUI that interacts with the warehouse such that one can complete OLAP commands and automatically query the data to their needs.

##  Overview
#### A full breakdown of research and development can be found in Project_Report.pdf. The following is an abridged description of the program

### Data Model Design
Student data was broken into 3 dimensions that can be described below:

![Cube](/img1.png?raw=true "Cube")

Program represents what major they are and relating info.
Academics represents everything regarding the academic information (status, GPA, ID, etc.).
Time represents time (as time is always a dimension in Data Modeling).

### Data Model Implementation
The data is then given a hierarchy of how the fields intermingle, and are then created in SQL by using a staging table to populate our fact table into this implementation.

![Fact Table](/readme1.PNG?raw=true "Fact Table")

### GUI
Finally, to interact with the generated data warehouse there must be a GUI. This GUI is designed with viewability of hierarchies in mind, and will be able to filter and query by selecting the OLAP 'command' operation they would like to perform. 

![GUI](/readme2.PNG?raw=true "GUI")
Start Querying: Used to begin a query. 
Continue Querying: Used to continue querying on the previously used query.
