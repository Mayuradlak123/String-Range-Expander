# String Range Expander

This Python utility provides a single, robust function called `expand_string_range` that parses a string of numbers and ranges and expands it into a clean, ordered sequence of integers. It is designed to handle a wide variety of formats and edge cases gracefully.

## Features

- **All-in-One Function**: A single entry point `expand_string_range` handles all the logic.
- **Multiple Delimiter Support**: Automatically recognizes common range delimiters like `-`, `..`, `to`, and `~` without extra configuration.
- **Step Value Parsing**: Supports step syntax for ranges, such as `"1-10:2"` to generate `[1, 3, 5, 7, 9]`.
- **Reversed Range Handling**: Correctly processes descending ranges like `"10-5"` to produce `[5, 6, 7, 8, 9, 10]`.
- **Smart Input Cleaning**: Automatically ignores leading/trailing whitespace and empty, comma-separated parts.
- **Duplicate & Overlap Handling**: Automatically merges overlapping ranges and removes duplicate numbers (e.g., `"1-3,2-5"` becomes `[1, 2, 3, 4, 5]`).
- **Flexible Output**: You can specify the output format as a Python `list` (default), `set`, or a CSV `string`.
- **Robust Error Handling**: The script includes `try...except` blocks to catch and report errors for invalid parts (like `"1-a"`) without crashing, allowing the rest of the valid parts to be processed.

---

## How to Use the `expand_string_range` Function

The primary way to use this utility is to import the `expand_string_range` function into your own Python scripts.

### 1. Basic Usage

Simply pass the string you want to expand to the function. It will return a sorted list of integers by default.

```python
from range_expander_modular import expand_string_range

# Basic range
print(expand_string_range("1-5, 8, 11-13"))
# Output: [1, 2, 3, 4, 5, 8, 11, 12, 13]

# With different delimiters handled automatically
print(expand_string_range("1..3, 5~7, 10 to 12"))
# Output: [1, 2, 3, 5, 6, 7, 10, 11, 12]


2. Using Step Values
The function can parse ranges with a step value, defined by a colon (:).
from range_expander_modular import expand_string_range

# Ascending with a step of 2
print(expand_string_range("1-10:2"))
# Output: [1, 3, 5, 7, 9]

# Descending with a step of 3
print(expand_string_range("20-1:3"))
# Output: [1, 4, 7, 10, 13, 16, 19, 20]


3. Changing the Output Format
You can control the output format by using the output_format parameter. The supported formats are "list", "set", and "csv".
from range_expander_modular import expand_string_range

# Get a set as output
print(expand_string_range("1-4,3-6", output_format="set"))
# Output: {1, 2, 3, 4, 5, 6}

# Get a CSV string as output
print(expand_string_range("1-4, 8", output_format="csv"))
# Output: "1,2,3,4,8"


4. Error Handling
If the input string contains an invalid part, the function will print a warning and skip that part, continuing to process the rest of the string.
from range_expander_modular import expand_string_range

# The invalid parts "1-a" and "10:b" will be skipped
result = expand_string_range("1-a, 2-4, 8, 10:b")

# Console Output:
# Warning: Skipping invalid part '1-a'. Reason: Invalid range with non-numeric values: 1-a
# Warning: Skipping invalid part '10:b'. Reason: Invalid step value: b

print(result)
# Final Result: [2, 3, 4, 8]


Running the Script Directly
If you run the range_expander_modular.py script directly from your terminal, the code inside the if __name__ == '__main__': block will execute. This section contains several print statements that demonstrate the function's capabilities across all defined scenarios, making it easy to see examples of its behavior.
python range_expander_modular.py


