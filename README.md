
# Monte-Carlo-Machine-For-Hand-Cricket

## Introduction
Hand Cricket was this very nostalgic game that I have played when i was a kid.. its very popular here in India. I thought to myself.. what's the most optimal way to play this game? I used Probability to find the direct answer, but ultimately decided to build a Monte Carlo Machine to simulate and plot the results.

## How does Hand Cricket work?
Hand Cricket is very complex in its nature.. its a 2 player game where person A and person B throw signs with their hands in synchorinzed time.. like Rock Papers Scissors, instead of rocks and papers we have numbers 1 to 10.. firstly, the whole game is based on cricket.. so the game starts with a toss.. both players pick either odd or even.. then the show their numbers.. if sum of the numbers matches their prediction of odd or even, then they get to decide wether they bat or bowl.. As a bowler your goal is to pick the same number as batsman to score a game over for Batsman.. As a batsman, the consecutive sum of the numbers you select are your score, you have to score a target high enough for the bowler.

## Monte Carlo? Isnt That A Casino?
Yes, Monte Carlo is a casino, but the method is just named after it.. simply put, instead of brute forcing calculations using probability, you simulate it using computer algorithims, thats the Monte Carlo method. For The Time Being, You Play as the bowler and the batsman in main.py tries to Adapt to your playstyle.. but you have to give it time to adapt.. lesser the time.. more the AI will converge towards 10.. it will keep convering to 10 at counts of less than 200 or 300.. in the future im thinking of training it with human input but for now enjoy having to play 300 times to get an adaptive batsman hehe :D

## Results

| Strategy | Avg Score | Trials |
|---|---|---|
| Fixed number (10), random bowler | ~90 | 10,000 |
| Fixed number (10), biased bowler (60% repeat) | ~225 | 10,000 |
| Random pick avoiding bowler's last number | ~125 | 10,000 |
| Random pick, greater than bowler's last number | ~140 | 10,000 |

Here is how, without any probability calculation.. i was able to predict the perfect outcome of each case.. for a random bowler.. each number wil obviously have a probability of 1/10.. multiply that probability with the number itself to get a risk * reward value of the number.. for a random bowler the risk * reward will be maximum for 10 and 10 always as the probability doesnt change.. this is a geomtric distribution so no of attempts before fail will be 1/(1/10) which will come as 10.. since the 10th attempt is where the batsman is gone out. 9 * 10 should give us an average score of 90... and that was exactly what was predicted by my model

<img width="2978" height="1774" alt="results_chart" src="https://github.com/user-attachments/assets/27000451-6248-41bf-bd10-74e14d5a5b8a" />

## Python Stuff
See [iterations.py](iterations.py) for the iterations used to get the graph data.. main.py is the Work In Progress Adaptive Batsman.. [graph.py](graph.py)
was used to generate the graph for the results... results are hardcoded in it, as it wouldnt use the remaining decimal anyway.
