# Chilliest State for John

John is considering moving to a new state because he loves chilly weather. He
currently lives in Georgia, but he's thinking about moving to Oregon or Maine.
To decide, John wants to compare the average temperatures and how much
temperatures vary throughout the year in these states.

Your job is to help John by calculating the average annual temperature and the
standard deviation for each state. The standard deviation will tell John how
much temperature fluctuations he might experience. He prefers a place where the
temperatures are not only cool but also relatively stable throughout the year.

## Summary: What is Standard Deviation, and Why Is It Useful Here?

Standard deviation measures how much the monthly temperatures vary from the
average. A lower standard deviation means temperatures are more consistent and
stable throughout the year, while a higher standard deviation indicates greater
fluctuation.

In this scenario, standard deviation will help John understand the
predictability of the weather. Even if a state has a low average temperature, a
high standard deviation means he might still experience some warmer months,
which he might not prefer.

By comparing both the average temperature and the standard deviation for each
state, John can decide not just where the weather is coolest, but also where it
is most steady and predictable.

## Inputs

- There are no user inputs

## Imported Data

- Lists of temperatures for Oregon and Maine will be stored in a file named `states.py` which has the following attributes:
  - `oregon_temps`: A list of monthly average temperatures for Oregon.
  - `maine_temps`: A list of monthly average temperatures for Maine.

## Expected Output

When you run your program, the console should display the following text, formatted as in this example:

```
Oregon: XX.XX F, Variation: YY.YY 
Maine: XX.XX F, Variation: YY.YY

Oregon has the chilliest weather. 
Maine has the most stable temperatures.
```
Where `XX.XX` represents the average temperature and `YY.YY` represents the
standard deviation for each state.

> Note: The output template is provided. You need to calculate the statistics
> and assign the results to the variables prior to running these `print()`
> statements.
>
> Minimally, make sure you assign values to:
>
> - `average_oregon`
> - `average_maine`
> - `chilliest_state`
> - `most_stable_state`

## Hints

- Make sure you import the local module `states`, which will contain the
  temperature lists inside of variables `states.oregon_temps` and
  `states.maine_temps`
- Use the `statistics.mean()` function to calculate the average temperature for
  each state.
- Use the `statistics.stdev()` function to calculate the standard deviation for
  each state's temperatures.
- Yes, I will test this using a different set of temps, as well, so don't try to
  fool me by just _hard coding_ in the values into the print statement. ;)