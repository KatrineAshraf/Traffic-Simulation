# <img src="assets/icon.png" width=50 height=50> Traffic Simulation </img>
Traffic simulation is a simple game with python (pygame) that integrates system and discipline among cars in driving in traffic, with major probabilities of taking turns and switching roads whenever accessible.
This game not only does it automates the traffic but also can accept any kind of input from users: Deleting cars, adding cars, changing roads, ...etc.\
\
![Window App](assets/trial.png)
<details>
<summary><h3><ins>Scientific Idea behind the App</ins></h3></summary>
This game simply injects the idea of 1D Cell Automata where the idea is to consider a set of adjacent cells representing a street along which a car can move. The car jumps to its nearest neighbor cell unless this cell is already occupied by another car. Decelerate, if tailing distance to the next car is less than strength of pheromone suggests. Accelerate, if there is no pheromone or tailing distance is greater than suggested by pheromone strength.<br>
<b>The rule of motion can be expressed by:</b><br>
$x(t+1)  =  x_{in} (t) (1-x(t)) + x_{out}(t).x(t)$ <br>
where $x$ is the cell, $x_{in}$ is the cell from which the car come, $x_{out}$ the destination cell, and $t$ is time.
</details>

##  To directly play Traffic Simulation:
+ Download the [zipped folder](https://github.com/KatrineAshraf/Traffic-Simulation-With-User-Input/blob/789f902fd162384ca07d16db7d6886aac843f660/Traffic%20Simulation.zip) in my repository.
+ Extract the zip folder.
+ Run the `Traffic Simulation.exe` file.
>[!CAUTION]
> The executable file could mal-function if removed from the final extracted folder.

## To play from source code:
+ Clone the repository or download it and open it with any python interpreter.
+ `pip install pygame` or simply ignore if requirement is satisifed.
+ Run the `ui.py` file.

## The controls to the Traffic Simulation Application:
| Controls | Description |
| :-------: | :------: |
|![spacebar](assets/spacebar.png)| To Pause/Resume the simulation|
|![Esc](assets/esc.png)| To exit the game|
|![R](assets/r.png)| To randomly generate cars in the available tiles|
|![N](assets/n.png)| To view the next state/movement when paused|
|![C](assets/c.png)| To clear all the cars |
|![Tab](assets/tab.png)| To clear all the road tiles in the simulation|
|![RMouse](assets/r_mouse.png)| To Add/Remove a car on a road tile|
|![G](assets/g.png) ![plus](assets/plus.png) ![LMouse](assets/l_mouse.png)| To add a green tile|
|![Up](assets/up.png) ![plus](assets/plus.png) ![LMouse](assets/l_mouse.png)| To add up road tile|
|![Down](assets/down.png) ![plus](assets/plus.png) ![LMouse](assets/l_mouse.png)| To add down road tile|
|![Left](assets/left.png) ![plus](assets/plus.png) ![LMouse](assets/l_mouse.png)| To add left road tile|
|![Right](assets/right.png) ![plus](assets/plus.png) ![LMouse](assets/l_mouse.png)| To add right road tile|

