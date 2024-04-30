# KY Child Support calculator

Don't ask why.

See `main.py` for example usage.
Basically, toss a number of children in with two data-complete `Parent`s, and
out pops your conclusion and [worksheet](https://www.ardfky.org/sites/ardfky.org/files/Child%20Support%20Worksheet%20CS71.pdf).

Current for [2024 guidelines](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=52811).

This should not take the place of your attorney, and has comes with no guarantee of accuracy or fitness-for-purpose.

`python main.py [OTHERS_DAYS] [NUM_CHILDREN]`

```
HisName (B) pays $298.18 to HerName (A)


|  Number|       A|       B|       C|
|========|========|========|========|
|       1|   2,600|   9,167|        |
|       2|       0|       0|        |
|       3|       0|       0|        |
|       4|   2,600|   9,167|        |
|       5|        |        |  11,767|
|       6|  22.10%|  77.90%|        |
|       7|        |        |   1,714|
|       8|       0|     480|     480|
|       9|       0|     335|     335|
|      10|        |        |   2,529|
|      11|     559|   1,970|        |
|      12|     224|   1,155|        |
|      13|     182|     182|        |
|      14|        |  50.00%|        |
|      15|        |     857|        |
|      16|        |     298|        |
|--------|--------|--------|--------|
| Shared-Parenting Adjusted|    True|
|      Self-Support Reserve|   False|
+-----------------------------------+
```
