# Number Guessing Game

A command-line number guessing game built in Python where players try to guess a randomly generated number within a specified range. The game features customizable difficulty levels, attempt limits, and best score tracking.

## Features

### Core Gameplay
- **Random Number Generation**: Computer selects a random number within the specified range
- **Interactive Guessing**: Players input their guesses and receive immediate feedback
- **Smart Hints**: Game provides "higher" or "lower" hints after incorrect guesses
- **Attempt Limit**: Players have exactly 10 attempts to guess the correct number
- **Win/Loss Feedback**: Clear messages for successful guesses or game over scenarios

### Customizable Difficulty
- **Default Range**: First game uses standard 1-100 range
- **Custom Ranges**: Players can set any range for subsequent games
- **Flexible Limits**: Supports positive, negative, and mixed number ranges
- **Range Validation**: Automatically handles reversed ranges (e.g., 20 to 5 becomes 5 to 20)
- **Smart Input**: Prevents invalid ranges like identical upper and lower limits

### Score Tracking
- **Best Score System**: Tracks the fewest attempts needed to win across all games
- **Persistent Tracking**: Best score maintains throughout the entire session
- **Achievement Feedback**: Notifies players when they set a new personal record
- **Session Statistics**: Displays current best score after each game

### User Experience
- **Clean Interface**: Minimalist design focused on gameplay
- **Input Validation**: Robust error handling for all user inputs
- **Game Flow Control**: Intuitive menu system for continuing or quitting
- **Clear Feedback**: Immediate response to all player actions

## How It Works

### Game Flow
1. **Welcome & First Game**: Starts with default range (1-100)
2. **Guessing Phase**: Player has 10 attempts with hints after each wrong guess
3. **Game Resolution**: Win (show attempts used) or lose (reveal correct number)
4. **Menu System**: Option to play again with custom range or quit
5. **Best Score Update**: Track and display personal records

### Range Customization
- Players can specify any integer range after the first game
- System automatically adjusts reversed ranges for logical gameplay
- Supports creative ranges like negative numbers (-50 to -10) or large spans (1 to 1000)

### Validation Systems
- **Numeric Input**: Ensures all guesses and range inputs are valid integers
- **Range Logic**: Prevents impossible ranges and adjusts user errors
- **Menu Choices**: Validates menu selections with helpful error messages
- **Graceful Recovery**: Game continues smoothly even with invalid inputs

## Technical Implementation

### Code Structure
- **Modular Functions**: Separate functions for range input, gameplay, menu system, and main control
- **Error Handling**: Comprehensive try-catch blocks for all user interactions
- **State Management**: Tracks game state, best scores, and turn progression
- **Clean Logic Flow**: Clear separation between game rounds and overall session management

### Key Algorithms
- **Random Number Generation**: Uses Python's `random.randint()` for fair number selection
- **Attempt Tracking**: Calculates attempts used (10 - remaining + 1) for accurate scoring
- **Best Score Logic**: Compares current performance against session-wide personal best
- **Range Normalization**: Automatically sorts range limits for consistent gameplay

## Usage Example

```
WELCOME TO NUMBER GUESSING GAME
Guess the number between 1 and 100
You have 10 attempts.

Enter your guess: 50

Incorrect, try again!
Attempts left: 9
Hint: The number is higher

Enter your guess: 75

Congratulations! You found the number 75!
You used 2 attempts.
New best score: 2 attempts!

GAME MENU

1. Play again
2. Quit

Best Score: 2 attempts

Enter your choice (1 or 2): 1

Set your custom range:
Enter lower limit: -50
Enter upper limit: 50
```

## Requirements
- Python 3.x
- No external dependencies (uses only built-in modules)

## Running the Game
```bash
python number_guessing_game.py
```

## Educational Value
This project demonstrates several important programming concepts:
- **Control Flow**: While loops, conditional statements, and function calls
- **Error Handling**: Try-catch blocks and input validation
- **Data Management**: Variable scope, state tracking, and data persistence
- **User Interface**: Command-line interaction and menu systems
- **Algorithm Design**: Random generation, scoring systems, and game logic
