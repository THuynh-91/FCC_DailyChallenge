
# Free Shipping
## Prompt
Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

To compare them, convert both values to joules using the following conversions:

1 Calorie equals 4184 joules.
1 watt-hour equals 3600 joules.
Return:

"Workout" if the workout used more energy.
"Devices" if the device used more energy.
"Equal" if both used the same amount of energy.

## My Thoughts
Just convert the energy into the same units, and compare them. I could have done a mapping of a calorie into joules, but for this case it wasn't that necessary.

## Solution (Python)
```python
def compare_energy(calories_burned, watt_hours_used):
    c = calories_burned * 4184
    w = watt_hours_used * 3600

    if c > w:
        return "Workout"
    elif c < w:
        return "Devices"
    else:
        return "Equal"
```
