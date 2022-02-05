# PyUncharted

**To design and implement an object-oriented adventure game scenario in python by taking inspiration from the PlayStation game, Uncharted. The overall objective of the game is to locate blue sap of a tree, which when ingested makes the drinker nearly invincible.**

In order to simulate the working of Uncharted, few missions from the game are taken and respective classes based on those missions are created. Each of these classes depict a level to be completed by the user. Only after successful completion of the respective level, the user will be allowed to move to the next level (in terms of code, the object of the next level will only be initialized after a current level is completed without any hinderance).

The application developed is a game in all senses. It contains 8 levels and each of these levels have a small game within itself. Each of these games are independent and unique from the others in terms of code as well as functionalities. Few of the levels might overlap with the others but have a unique flavor in them. 

## Class diagram

<img width="451" alt="image" src="https://user-images.githubusercontent.com/49033060/152642897-b90a8c2d-b02b-4211-a5fc-671626c3d737.png">

## Game and classes description 
An overall of 8 levels are created to depict the working of the game. Each of these 8 levels have a unique obstacles and challenges. Appropriate error handling has been implemented for every class in the program. The following levels were created in the game:

### 1.	Museum
* In this level, the user will enter the Museum and a map will be displayed. The map will contain items at each corner which needs to be checked and if required, stolen. Note: only two items can be stolen from the museum.
* The user is required to move around the map to check the items and steal the items if they match the description mentioned in the objective.
* An artifact node can only be visited once.
* Class Museum is used simulate the above-mentioned activities. An image of the museum map is shown with labels around it providing the user with instructions. Buttons to show directions are also provided.

### 2.	Home
* After stealing the items from the museum, the user will return back home and go through each of the items.
* While checking the map, current possible locations are displayed and the user needs to choose whether they are correct.
* Failure to choose the correct location will lead to restarting the level. 
* Class Home is used simulate the above-mentioned activities. Items previous stolen by the user are used in this level. 
* Images of destinations are shown the user is required to choose the correct one by clicking on the radio button. 

### 3.	Market
* After deciding the location, the user will need to buy a few items with respect to 3 sets of conditions observed in the region.
* For purchasing items in this level, the user has only been allotted 100$.
* With respect to each of the conditions, a set of items will be displayed and the user is required to choose the most appropriate ones while not exceeding the money allotted for this task.
* Class Market is used simulate the above-mentioned activities. Items and prices for respective conditions are shown in the form of check boxes where in only the correct sum of values will lead to the next level

### 4.	Jungle without obstacles
* The expedition begins with the user reaching the location previously discovered and entering the jungle.
* A map is shown on the screen which displays the current location, visited node, obstacles in the path and destination.
* The user must navigate through the jungle while avoiding obstacles.
* Class jungleWithoutObstacles is used simulate the above-mentioned activities. 

### 5.	Jungle expedition
* After crossing a relatively safe region, the user is subjected to a series of obstacles with respect to 3 conditions.
* Two obstacles require the user to use items previously brought in the market in their defense while the other two obstacles require the user to use their logic.
* Failure to complete any of the tasks in the required manner will result in restart of the level.
* Class JungleExpedition is used simulate the above-mentioned activities. Three images are added and they are then used to depict each of the obstacles. Below the images, there are labels and buttons placed which display the obstacle faced and the possible methods of resolution.

### 6.	Cave
* While overcoming the last obstacle faced in the previous mission, the user enters a cave. A map will be shown which depicts the location of the user and possible ways to exit the cave.
* The user needs to navigate their way to the exit.
* While traversing through the cave, few paths will be blocked and the user is required to re-route!
* Class Cave is used simulate the above-mentioned activities. 

### 7.	Pyramid courtyard
* After reaching the pyramid, the lack of light makes it difficult for the user to navigate thus, the user is required to visit the courtyard in order to obtain objects which would help the user in navigation.
* Similar to the first level, the user will be required to view items and their description in order to pick them if they deem fit for lighting a fire. The items will be placed at the corners of the room and user needs to navigate and inspect them.
* Class Pyramid1 is used simulate the above-mentioned activities. 

### 8.	 Pyramid
* Upon re-entering the pyramid, the user needs to navigate their way through a room. The map of the room is displayed to the user and they are required to enter the correct path while avoiding obstacles to reach the next room.
* After exiting the previous room, the user is unable to see anything due to some mysterious effect. A set of options are shown to the which might help in further navigation.
* After reaching the exit door of the room, the user is required to decide based on what is written on the wall. Choosing the correct option will lead the user to the end of the game and make them invincible!
* Class Pyramid1 is used simulate the above-mentioned activities. 

While the above-mentioned levels depict the working of individual levels, an additional class has been created for the smooth function of the game. 
### Class Uncharted:
* Most vital class in the program. It works as the main class for the program.
* Each of the objects of the above-mentioned class is created in this class. Only if the levels have been completed successfully, this class will allow the next level to begin.
* All the maps, descriptions, starting point and bag has been initialized in this class.
* Intermediate GUI’s after completion of every mission is created and displaying through this class.
* If any of the levels are not completed correctly, this class displays and error message and makes sure the mission is completed properly
