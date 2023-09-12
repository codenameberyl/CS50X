# Lab 6: World Cup

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Lab 6: World Cup](https://cs50.harvard.edu/x/2023/labs/6/). This Python program simulates the outcome of the FIFA World Cup tournament based on team ratings. It uses FIFA Ratings to estimate the probability of a team winning a game and then simulates the tournament multiple times to determine the likelihood of each team winning the championship.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Download and unzip the folder:

    ```bash
    cd "Lab 6: World Cup"
    ```

3. Run the program by providing the team data CSV file as a command-line argument. For example:

    ```bash
    python tournament.py 2018m.csv
    ```

## Program Structure

- `tournament.py`: The main Python program that simulates the FIFA World Cup tournament.

## Usage

1. Open a terminal and navigate to the `Lab 6: World Cup` directory.
2. Run the program using the command `python tournament.py FILENAME.csv`, where `FILENAME.csv` is the name of the team data CSV file you want to use for simulation.

## Simulating the Tournament

1. The program reads the team data from the provided CSV file and stores it in a list called `teams`.
2. It then simulates the tournament N times, where N is the value specified in the program (default is 1000).
3. For each simulation, the program uses the `simulate_tournament` function to determine the winning team.
4. The count of each team's victories is maintained in the `counts` dictionary.
5. After all simulations are completed, the program calculates and prints the estimated probability of each team winning the World Cup.

## Customizing the Number of Simulations

You can adjust the number of simulations by modifying the value of the `N` constant at the top of the `tournament.py` file. More simulations will provide more accurate predictions but may increase the runtime.

## Example Output

For example, running the program with the command `python tournament.py 2018m.csv` might produce the following output:

```
Belgium: 20.9% chance of winning
Brazil: 20.3% chance of winning
Portugal: 14.5% chance of winning
Spain: 13.6% chance of winning
Switzerland: 10.5% chance of winning
Argentina: 6.5% chance of winning
England: 3.7% chance of winning
France: 3.3% chance of winning
Denmark: 2.2% chance of winning
Croatia: 2.0% chance of winning
Colombia: 1.8% chance of winning
Sweden: 0.5% chance of winning
Uruguay: 0.1% chance of winning
Mexico: 0.1% chance of winning
```

## Additional Notes

- The program uses FIFA Ratings to estimate the probability of a team winning a game. The probability calculation is based on the Elo rating system.
- The simulation is a simplified representation of the actual World Cup, and the results may vary due to randomness in the simulation.
- The program structure and logic are provided in the `tournament.py` file, and you can customize it as needed to improve performance or add additional features.

Remember that the accuracy of the simulation predictions increases with the number of simulations performed. You can experiment with different values of `N` to find the right balance between accuracy and runtime.