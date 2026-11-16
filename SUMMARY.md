# Project Summary - Catch the Falling Objects (PS 55)

## Overview
A Python 3 game built with Pygame. Objects fall from random positions at
the top of the screen and the player moves a basket left and right to
catch them. Each catch adds to the score and every missed object costs a life.

## How It Works
- Window size is 500x600. The basket is 80x20, placed at y = 560, and
  moves 10 px per key press while staying inside the window.
- Each object is 20x20 and falls 5 px per frame from a random x position
  (random.randint(0, 480)).
- A rectangle collision between basket and object adds 1 to the score.
- If an object falls past the bottom of the window, the player loses a life.
- The game starts with 3 lives. At 0 lives, "Game Over" is shown with the
  final score, and pressing R restarts the game.
- Only the LEFT and RIGHT arrow keys are used. All other keys are ignored.

## Concepts Used
Pygame, coordinates, rectangle collision, score tracking, random module.

## Code Structure
- Game logic is written as separate functions (move_basket, is_caught,
  update_state) so it can be tested without opening a game window.
- The Pygame loop (drawing, events, frame rate) is inside main().

## Test Cases (all passed)
1. Normal input: Basket x = 210, object at (230, 545) -> Object caught,
   Score: 1, Lives: 3.
2. Boundary input: Basket x = 0 with LEFT, and Basket x = 420 with RIGHT
   -> no movement, basket stays inside the window.
3. Invalid input: UP arrow pressed -> key ignored, Basket x = 210.
4. Different valid scenario: object falls past y = 600 -> Lives: 2. With
   1 life left -> Lives: 0, Game Over, Final Score: 7.

## Conclusion
The project meets all the bare minimum requirements: basket movement with
arrow keys, random falling objects, score and lives display, and a Game
Over screen with the final score. The code was tested and all 4 test
cases pass.
