# RPG Dice Roller

In role-playing games (RPGs), dice rolls are often used to determine the outcome
of various actions, such as attacking an enemy or searching for hidden
treasures. Sometimes, a modifier is applied to the dice roll to account for
specific advantages or disadvantages, such as a character's skill or the
difficulty of a task. This exercise will allow you to simulate rolling a die
with a given number of sides and applying a modifier to the result.

## Inputs
- **Number of sides:** An integer representing the number of sides on the die.
  This must be at least 4.
- **Modifier:** An integer that will be added to (or subtracted from) the die
  roll. For example, `3`, `-2`, or `0`.

## Expected Output

When you run your program, the console should display one of the following
messages based on user input and the result of the die roll:

1. If the user enters `6` for the dice sides and `3` for the modifier:
    ```
    ROLL: 4 + 3 = 7
    ```
    _**NOTE**: `4` above is a randomly generated value from 1-6 because the user
    specified a 6-sided die. Your actual number will likely be different._

2. If the user types `20` and `0` (i.e., no modifier):
    ```
    ROLL: 14
    ```
3. If the user types `12`  and `-5`:
    ```
    ROLL: 7 + -5 = 2
    ```
4. If the user types `8` for the dice sides and `-4`:
    ```
    ROLL: 3 + -4 = 0
    ```
    _**IMPORTANT NOTE**: Results cannot be negative. If the final result with
    the modifier is less than zero, it should be restricted to zero._

    _**HINT**: python's built-in `max()` function is a great way of
    accomplishihg this. Try to figure out how (though falling back to if/else is
    fine, also)._

5. If invalid input is entered for sides or modifier:
    ```
    MUST ENTER A NUMBER
    ```

6. If the number of sides is less than 4:
    ```
    MUST ENTER 4 OR MORE SIDES
    ```

## Hints
- Use the `random.randint` function to simulate rolling a die.
- Remember to handle exceptions for invalid input using `try...except`.
- Validate that the number of sides is at least 4.
- A modifier can be positive, negative, or zero.
- Results cannot be negative.
