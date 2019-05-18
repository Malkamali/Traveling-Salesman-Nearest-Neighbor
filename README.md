# Traveling Salesman Problem
The travelling salesman problem (TSP) asks the question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city. (https://en.wikipedia.org/wiki/Travelling_salesman_problem). The problem might sound simple, but unfortunetly, there are no algorithms that can solve the TSP for a large input in a feasible amount of time. TSP is known as an NP-complete problem, where it is believed that there is no deterministic polynomial-time algorithm that solves the TSP.

# The Nearest Neighbor Hueristic, a Nondeterministic Algorithim
A Hueristic is a method of solving a problem that may not always yeild the optimal result. In the case of the TSP, a hueristic might find the shortest route, or something that is longer the shortest route. One such hueristic algortihm is the nearest neighbor algorithm. The algorithm goes as follows:
<pre>
. Start from the first city
. Find the nearest neighbor to that city and travel to it
. Keep traveling to the neerest neighbor until all cities have been visited
. Travel from the last reached city back to the first city </pre>

# Inputs
The code reads from an external text file. The input should look like:
<pre>{number of cities}
{City number} {X-coordinate} {Y-coordinate}
{City number} {X-coordinate} {Y-coordinate}</pre>

So for example, a text file that stores the information of two cities should look like:
<pre>---Example.txt---
2
1 0.5 0.5
2 1.5 2.5
---end of file---</pre>
