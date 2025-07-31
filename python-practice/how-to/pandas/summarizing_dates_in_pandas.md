# Summarizing Dates in Pandas: A Natural Language Explainer

When working with date columns in a pandas DataFrame, you can easily extract summary statistics—just like you do with numbers. For example, you might want to find the **oldest** or **youngest** date in a column of birthdays.

---

## Why Summarize Dates?

- **Find the earliest event:** Who is the oldest dog? When did something first happen?
- **Find the most recent event:** Who is the youngest dog? What’s the latest date in your dataset?

---

## Common Methods

If you have a DataFrame called `dogs` with a `date_of_birth` column, you can use pandas’ `min()` and `max()` methods to quickly get these answers:

- **Earliest date:**  
    `dogs["date_of_birth"].min()`  
    This returns the oldest date of birth in the column (the oldest dog).

- **Most recent date:**  
    `dogs["date_of_birth"].max()`  
    This returns the youngest dog’s birthdate.

      (In the transcript example, the youngest dog was born in 2018.)

---

## Example

Suppose your DataFrame looks like this:

    dogs["date_of_birth"]
    0   2010-05-21
    1   2018-08-15
    2   2012-12-02

- To find the oldest dog's birthdate:  
      `dogs["date_of_birth"].min()`      # 2010-05-21

- To find the youngest dog's birthdate:  
      `dogs["date_of_birth"].max()`      # 2018-08-15

---

## In Summary

- Use `.min()` to get the earliest date (oldest dog).
- Use `.max()` to get the most recent date (youngest dog).
- These methods work the same way as with numbers, but on date columns.

---

**Tip:**  
Make sure your column is in pandas’ `datetime` format for these methods to work properly.  
You can convert it using:  
    `dogs["date_of_birth"] = pd.to_datetime(dogs["date_of_birth"])`

---
