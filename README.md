# Pong Game 🏓

This project is a simple Pong game built using Python's **Turtle** module. It features two paddles, a ball, and a scoring system. Players can control the paddles to hit the ball and try to score against each other.

## Game Features

- Two-player game with controls for both left and right paddles.
- The ball bounces off the walls and paddles.
- The game keeps score and resets the ball position when a player misses.
- Visual effects using Turtle graphics.

## How to Play

- **Right Paddle Controls:**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

- **Left Paddle Controls:**
  - Move Up: `W`
  - Move Down: `S`

The game ends when one player reaches the winning score.

## Project Structure

- **main.py**: The main game logic, which initializes the screen, paddles, ball, and score system, and handles game controls and gameplay.
- **paddle.py**: Contains the Paddle class to manage paddle movement.
- **ball.py**: Contains the Ball class to manage ball movement, including bouncing off walls and paddles.
- **score.py**: Contains the Score class to manage and display the score on the screen.
