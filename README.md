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

![Fact Table](/img1.png?raw=true "Fact Table")
