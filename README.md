# Catch the Falling Objects (PS 55)

A Python 3 + Pygame game in which objects fall from random positions
and the player moves a basket left and right to catch them.

## Features
- Window 500x600, basket 80x20 moves 10 px per key press
- Objects (20x20) fall 5 px per frame from a random x position
- +1 score for every catch, -1 life for every miss
- Starts with 3 lives; "Game Over" with final score at 0 lives
- Press R to restart after Game Over

## How to Run
1. Install the library: `pip install pygame-ce`
2. Run the game: `python catch_the_falling_object.py`
3. Run test cases: `python catch_the_falling_object.py test`

## Controls
- LEFT arrow: move basket left
- RIGHT arrow: move basket right
- Any other key is ignored

## Test Cases
1. Normal input: Basket x=210, object at (230, 545) -> Object caught, Score 1, Lives 3
2. Boundary: Basket x=0 + LEFT, Basket x=420 + RIGHT -> no movement
3. Invalid input: UP arrow -> key ignored, Basket x=210
4. Different valid scenario: object falls past y=600 -> Lives 2; with 1 life -> Lives 0, Game Over

## Screenshots
(Add game, Game Over and test output screenshots here)