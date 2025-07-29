# Turning a List into a Random Walk: General Principle

A **random walk** is a sequence where each new value depends on the previous value, usually by adding some random change at each step.  
To turn a list into a random walk, you use a loop to **accumulate changes step by step**, appending each new value to your list.

---

## General Principle

- **Start with a list containing the initial value** (often 0).
- **Loop over your random events** (like coin flips, dice rolls, etc.).
- **At each step, calculate the new value** based on the previous value and the result of the random event.
    - For example, add 1 for "tails", add 0 for "heads".
- **Append the new value to your list**.
- **The list grows into a record of the random walk**—each element shows the cumulative total up to that step.

---

## Pseudocode Template

    walk = [starting_value]
    for event in sequence_of_random_events:
        new_value = walk[-1] + (change based on event)
        walk.append(new_value)

- `walk[-1]` always refers to the most recent value.
- `change based on event` is how the event modifies the walk (e.g., +1 for tails, 0 for heads).

---

## Example: Counting Tails in Coin Flips

Here’s how you can track the total number of tails (random walk) while simulating coin flips:

      import random
      tails = [0]  # Start with 0 tails
      for i in range(10):
          coin = random.randint(0, 1)  # 0 = heads, 1 = tails
          tails.append(tails[-1] + coin)
      print(tails)
      # Output: e.g. [0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6]

- The list `tails` shows the running total of tails after each flip.
- The final element is the total number of tails after 10 flips.

---

## Key Takeaways

- A random walk **accumulates changes** step by step.
- Always base each new value on the previous value plus the random outcome.
- Appending each result creates a list you can analyze or plot to see the path of the random walk.

---
