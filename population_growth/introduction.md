# Population growth kata

In a small town the population is `population0 = 1000` at the beginning of the year. The population regularly increases by `2 percent` per year and moreover `50` new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to `population_goal = 1200` inhabitants?

```
At the end of the first year there will be:
1000 + 1000*0.02 + 50 = 1070 inhabitants

At the end of the 2nd year there will be:
1070 + 1070*0.02 + 50 = 1141 inhabitants

At the end of 3rd year there will be:
1141 + 1141*0.02 + 50 = 1213 inhabitants

Answer: The town will need 3 years to reach population 1200 or higher.
```

More general:

the function `pop_growth_years` takes the following parameters:

- `population0` start population (positive integer)
- `percent` yearly growth in percent (a positive number or 0)
- `external` inhabitants coming or leaving each year (an integer)
- `population_goal` population to surpass (positive integer)


```
Examples:

pop_growth_years(1000, 2, 50, 1200) => 3
pop_growth_years(1500, 5, 100, 5000) => 15
```

## Running tests

- If you're in folder python_exercises: `python population_growth/tests.py`
- If you're in folder population_growth: `python tests.py`

