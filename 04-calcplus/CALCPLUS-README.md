# Upgraded RPN Calculator

Here's that calculator agagin! This time we're just tweaking things a bit now that we have access to "other people's functions". Specifically we're doing two things:

1. Adding in num1-to-the-power-of-num2 functionality
2. Cleaning up the output to remove stray .0's

The first part will leverage python's built in `pow()` function. This is simple
to use. If you want 4 squared ($ 4^2 $ which is 4x4 or 16) you would call
`pow(4,2)` and store the result. If you want 5 cubed ($ 5^3 $ which is 5x5x5 or
125), you would call `pow(5,3)`. Generically this is `pow(base,exponent)`.

The new operator for this "power" will be `^` since that's the closest we have
to a super-script in keyboard-ese.

The second part will leverage a function I wrote called `format_float`. It's
available in the file `i_am_human.py` which you should import into your
`calcplus.py` module. This function is fully documented, but basically you just
pass in a float (and optionally a maximum number of decimal places for rounding)
and it gives you back a human-friendly-formatted string version of that number.

## Inputs

Prompt the user to enter the following information:

- Enter the first number (float)
- Enter the second number (float)
- Enter the operator ( + , - , x , / , ^ )

## Input Validation

If ANY of the validation checks fails, then print `INVALID NUMBER` or 'INVALID
OPERATOR' and exit immediately.

- Both numbers must currectly convert to float
- The operator must be `+`, `-`, `x`, `/`, or `^`

## Expected Output

This one is pretty easy. Simply display the full calculation in the form:

`{num1} {operator} {num2} = {result}`

But you must also change the 

Note the spaces between each part. For example:

`1.0 + 1.0 = 2.0`

**NEW IMPORTANT NOTE**: Do _**NOT**_ use `round()` function to round anything
this time. You want to let math be math without adding in potential errors
through rounding. Instead, just reformat num1, num2, and result prior to
printing.

 - num1 and num2 should be formatted with no specified max number of decimal
   places. In other words, these should display with as many digits to the right
   of the decimal as the user entered (though with trailing 0's removed).
 - result should be formatted to display at most 4 digits after the decimal.

### Special Case : Division by Zero

If the user enters `0` for the second number and `/` for the operator, then
obviously you'll get an exception. Use exception handling for this one scenario.
Set the anser to `ERROR` when you catch this exception. For example:

`8.0 / 0.0 = ERROR`

### Special Case : Big pow's

There are two potential special cases here. Big numbers can be represented using
scientific notation (e.g., `1.7426e+204`). This is not a big deal. The number is
just formatted that way when printed. Just be aware of it.

The other possibility is that the number is just too big for the computer to
deal with at all. `1000 ^ 1000` is _ginormous_, and python just raises an
exception. So as with the division operation, you will need to catch an
exception here and output a similar message. For example:

`1000 ^ 1000 = ERROR`

## Input + Output Examples

| number 1 | number 2 | operator | output
|:--------:|:--------:|:--------:|-------------------
| 5        | 6        | +        | 5 + 6 = 11
| 10       | 2        | /        | 10 / 2 = 5
| 5        | 6        | x        | 5 x 6 = 30
| 1.1      | .2       | -        | 1.1 - 0.2 = 0.9
| 3.0      | 2.0      | +        | 3 + 2 = 5
| -4       | 3        | x        | -4 x 3 = -12
| 8        | -10      | +        | 8 + -10 = -2
| 2.02468  | 2.00000  | /        | 2.02468 / 2 = 1.0123 (THIS IS DIFFERENT...CAREFUL)
| -6.6     | -3       | /        | -6.6 / -3 = 2.2
| 4        | 0        | x        | 4 x 0 = 0
| 4        | 0        | /        | 4 / 0 = ERROR
| 4        | 3        | ^        | 4 ^ 3 = 64
| 4.5      | 3        | ^        | 4.5 ^ 3 = 91.125
| 16       | .5       | ^        | 16 ^ 0.5 = 4
| -5       | 3        | ^        | -5 ^ 3 = -125
| 2        | -2       | ^        | 2 ^ -2 = 0.25
| 123      | 123      | ^        | 123 ^ 123 = 1.1437436793461719e+257
| 123      | 456      | ^        | 123 ^ 456 = ERROR
| ten      |          |          | INVALID NUMBER
| 10       | two      |          | INVALID NUMBER
| 3.5      | 2.0      | *        | INVALID OPERATOR
| 175      | 232      | times    | INVALID OPERATOR
