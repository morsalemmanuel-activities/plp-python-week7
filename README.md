# PLP Python Week 7 — Lists and Shopping List Manager

## Project Files

- `list_warmup.py` — Demonstrates list creation, index access, adding and removing items, and counting list elements.
- `shopping_list.py` — Provides an interactive shopping list manager to add, remove, and display items.
- `list_report.py` — Prints a numbered shopping list, counts item names with more than four characters, and finds the longest item name.
- `screenshots/` — Contains screenshots showing the three programs running successfully.
- `README.md` — Describes the assignment and explains why checking list membership is important.

## Why is it safer to check `in` before calling `.remove()`?

Checking `in` first confirms that an item exists in the list before attempting to remove it. If the item is missing, calling `.remove()` directly raises a `ValueError` and may stop the program. Using an `if` statement allows us to display a helpful message and keep the program running.