# MoveInSync
# How I approached this problem.

I am approaching this project firstly using simple method. Like there is person who wants to go for a trip in efficient way from a particular given place.

Things which I implemented:
In starting firstly i will take the location of the person and according to his or her location I will appoint driver who is nearest to them and at the same time his rating is more than 3.5 out 5 star. This will ensure that a person is getting a proper authenticated driver and there will be more chance that their drive will be safe and good.
Then I saw all the paths and ways to reach the destination from the given point. And using Dijkstra’s Algorithm i found the shortest path to reach to the destination and it's travelling cost calculated using "distance_cost = distance * 10" using that path. Also I saw the total waiting time on every path during travelling and by combining both factor of travelling and waiting cost I had given the path which is best suited for the person.
Atlast I had provided the live location of a person. 

I had perform all these steps in this project as the time was limited and it was hard to implement more funtions and ways and make this thing more good.
