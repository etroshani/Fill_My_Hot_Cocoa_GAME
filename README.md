# Fill My Hot Cocoa!
Fill My Hot Cocoa is a game built in Python using the Pygame module. It consists of lively music, fun gameplay, and a feel-good mood. A player has the challenge of catching as many marshmallows as possible, all while avoiding the bombs in order to beat the game! This is an indie game created as a personal project to further develop my skills as a programmer. Initiated out of a desire to delve into new programming concepts and test my abilities, this project has been a proving ground for both learning and creativity. Through the challenges faced and the solutions devised, I've not only navigated unfamiliar territories but also honed my craft, adding a wealth of knowledge and techniques to my development arsenal. In the end, I can confidently say that I have mastered new aspects of game creation and programming, and will continue to undertake new challenging projects in the future.

Below are some brief descriptions on the elements of my code files:
# main.py: The Core Game Loop and Mechanics
main.py serves as the heart of the game, orchestrating the game's core loop, event handling, and rendering processes. It handles graphical rendering, event management, and sound playback. Key functionalities include dynamic background scrolling, sprite creation and management, level difficulty, collision detection, and score tracking, event handling, and more. The game loop follows a structured approach to update game states, process user inputs, and render updates to the display, ensuring smooth and responsive gameplay.
## Dynamic Background Scrolling: 
Implements an efficient method to create an endless vertical scrolling effect to enhance the game's visuals.
## Sprite Management: 
Utilizes sprite groups for efficient rendering and updates of game objects to optimize performance.
## Collision Detection: 
Implements collision detection for gameplay mechanics such as collision with items and obstacles.
## Score Tracking: 
Handles data by tracking player scores and integrating pandas for high scores management to display in the "scores" page.

# sprites.py: Sprite Classes and Movement
Object-oriented programming was used for the organization of the game's logic and data. sprites.py defines the Sprite classes for the player character and game objects, encapsulating properties like position, movement, and collision detection.
## Main Sprite Class: 
Manages the player character's movement using the arrow keys, including acceleration, friction and screen wrapping logic.
## Object Sprite Class: 
Defines the behavior and movement patterns of collectible and obstacle sprites, including vertical and different types of sinusoidal movements based on the level reached in the game.

# ui.py: User Interface Elements
ui.py focuses on the game's user interface components, including title animations, button interactions and animations, and score displays. It showcases custom UI drawing capabilities and event handling for interactive elements.
## Title Animation: 
Creates an engaging entry screen with animated game titles using a sinusoidal movement.
## Button Class: 
Provides interactive buttons with hover effects and click detection for navigating through the game's menus.
## Score Display: 
Implements a dynamic score display during gameplay and in the score menu.

# settings.py: Game Configuration
settings.py contains the game's configuration settings, including screen dimensions, font settings, and global variables. It acts as a centralized location for managing game settings, facilitating easy adjustments and maintenance.
## Screen and Font Configurations: 
Defines essential settings for the game's display and text rendering to ensure consistency across the game.
## Global Variables: 
Houses global variables that control game states, rounds, and user interactions.

# sounds.py: Sound Effects and Music
sounds.py manages the game's audio components, including background music and sound effects for game actions. 
## Sound Effects: 
Incorporates sound effects for various game events, such as collecting items and game wins.
## Background Music: 
Handles the loading and playing of background music tracks for different menus.
