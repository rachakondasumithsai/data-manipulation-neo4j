# data-manipulation-neo4j

## Section A: Exploring the given dataset Dataset name: DNR Camping Parks Reservation Data 2016 [1]
* Dataset url: https://data.novascotia.ca/Lands-Forests-and-Wildlife/DNR-Camping-Parks-Reservation-Data-2016/4zt7-x443
* Dataset description: This dataset contains camping reservation information of parks in different countries. It has about 35 thousand instances with 13 attributes. This information is collected through the reservation system for the general public to reserve camping sites in the Nova Scotia Provincial Parks for the year 2016. It was updated on July 5, 2017. It belongs to natural resources department. The attributes are ParkName, State, Country, Adult, Child, partySize, RateType, BookingType, Equipment, BookingStartDate, BookingEnddate, Night, Permits. Initials of state names are used. Only three types of Country data are present, they are CANADA, USA and OTHER. For Canada and USA, state names are in State column but for other countries, the country name is filled in the State column. There are exactly 20 unique parks in Nova Scotia with different values at different attributes. These parks can be booked for camping. There will be party size for every camp held at any park. This size is inclusive of both adults and child. The cost for ticket booking is categorized to senior, full, veteran and host. There are three types of permits, they are campsite, backcountry and yurt. For each booking user must book equipment too. This equipment may be less than 20ft/30ft/40ft, single tent and a couple of tents. The starting and ending dates of booking is provided along with the number of nights camping is done. By looking at this data and identifying trends, we can get the patterns in booking within a period.
## Section B: Python program to perform data manipulation on given dataset
* I have downloaded the original dataset as original.csv file.
* Then I have extracted all data on parks which belongs to Canada and named that file as file1.csv.
* From file1.csv I have extracted data based on specified attributes ParkName, State, PartySize, BookingType, RateType, Equipment, and created another CSV file by naming it as file2.csv.
* From file2.csv I have selected Equipment attribute and scanned all the rows and replaced all values with patterns “Less Than” as “LT” and “Single Tent” as “ST” and saved the data to file3.csv
* I have used pycharm tool with python programming language and pandas package to carry out the above operations, and the code/script is provided in this assignment folder.
## Section C: Exploring and Installing “Neo4j”
* I have installed Neo4j Desktop version 1.2.4 from https://neo4j.com/download/ with all required dependencies. I have created a graph database, after creating I have started the database. By opening the browser in Neo4j Desktop we can perform operations in graph database. I have explored sample datasets which are inbuilt using “:play movie graph” and “:play northwind graph” commands.  
<a href="https://ibb.co/tm6KJSk"><img src="https://i.ibb.co/C1y8HqN/image.png" alt="image" border="0"></a>  
<a href="https://ibb.co/LNx3nZf"><img src="https://i.ibb.co/jJySgrF/image.png" alt="image" border="0"></a>
## Section D: Building graph using Neo4j
* From file3.csv, I have extracted parks which belongs to Nova Scotia province and saved it into file4.csv by using python script.
* In this file4.csv, I have used MS Excel tool to remove duplicates and selected only 20 unique parks with maximum party size.
* I have loaded updated file4.csv into graph database with prescribed attributes using Cypher query language. Each park is considered as a node here. The below image demonstrates this step.
<a href="https://ibb.co/YtSfLc4"><img src="https://i.ibb.co/gD8tRSb/image.png" alt="image" border="0"></a>
* All parks with similar RateType are connected by creating a relationship NeighbourByRate. The following image is a demonstration.
<a href="https://ibb.co/hXH6zyd"><img src="https://i.ibb.co/TKRf3k0/image.png" alt="image" border="0"></a>
* All parks with identical State are connected by creating a relationship Same_State. The following image is a demonstration
<a href="https://ibb.co/swjjLnK"><img src="https://i.ibb.co/Kq66Cd2/image.png" alt="image" border="0"></a>
* All parks with same Equipment are connected by creating a relationship NeighbourByEquipment. The below image is a demonstration
<a href="https://ibb.co/R3fMbS8"><img src="https://i.ibb.co/gSNX97Y/image.png" alt="image" border="0"></a>
* The park which is having highest party size is displayed. Below image is a demonstration. Graves Island is the park that is having highest party size value 35.
<a href="https://ibb.co/7YvSD7Z"><img src="https://i.ibb.co/BzLfJ8Q/image.png" alt="image" border="0"></a>
* The whole graph looks like the following image.
<a href="https://ibb.co/z4hPMsx"><img src="https://i.ibb.co/crc2BJ3/image.png" alt="image" border="0"></a>
## References:
[1] “DNR Camping Parks Reservation Data 2016,” Novascotia.ca, 23-Jan-2017. [Online]. Available: https://data.novascotia.ca/Lands-Forests-and-Wildlife/DNR-Camping-Parks-Reservation-Data-2016/4zt7-x443. [Accessed: 26-Feb-2020]