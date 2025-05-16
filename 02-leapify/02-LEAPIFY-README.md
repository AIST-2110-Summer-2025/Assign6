# Leap Year with Calendar Module

In the previous exercise, you wrote a program to determine if a given year is a
leap year using the rules for leap years. Now, let's revisit this problem and
use a built-in Python module to simplify our work! Python has a fantastic
`calendar` module that can help us determine if a year is a leap year without
manually checking the rules.

In this follow-up exercise, you'll learn how to use the `calendar` module to
streamline the leap year check. By leveraging modules, we can make our programs
cleaner and more efficient!

## Inputs
- A year entered by the user as an integer.
  + _The program should only accept years greater than `0`_

## Expected Output
When you run your program, the console should display the following
 text based
on the input provided:

- If you enter `2000`, your program should output: `2000 is a leap year.`
- If you enter `2020`, your program should output: `2020 is a leap year.`
- If you enter `2011`, your program should output: `2011 is not a leap year.`
- If you enter `1800`, your program should output: `1800 is not a leap year.`
- If you enter `0`, your program should output: `INVALID YEAR`
- If you enter `-100`, your program should output: `INVALID YEAR`
- If you enter `jaguar`, your program should output: `INVALID YEAR`

## Hints

- _This is an easy one...you are basically replacing most of your if logic
  (excluding the input validation) with a single function call._
- Remember to import the `calendar` module at the start of your script.
- Investigate the `calendar` documentation
  [https://docs.python.org/3/library/calendar.html](https://docs.python.org/3/library/calendar.html)
  to determine the correct function to check if the year is a leap year.
- Ensure you handle cases where the year entered is not greater than 0 by
  printing an appropriate message.
