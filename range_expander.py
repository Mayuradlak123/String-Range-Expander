import re

# Define supported delimiters as a module-level constant
SUPPORTED_DELIMITERS = ["-", "..", "to", "~"]
STEP_DELIMITER = ":"

def _parse_part(part: str) -> tuple[int, int, int]:
    """
    Parses a single part of the input string (e.g., '1-10:2' or '5').

    Args:
        part: The string part to parse.

    Returns:
        A tuple containing (start, end, step). For single numbers, start and end are the same.
    
    Raises:
        ValueError: If the part is invalid.
    """
    # Handle step values
    step_parts = part.split(STEP_DELIMITER)
    range_part = step_parts[0]
    step = 1
    if len(step_parts) > 1:
        if not step_parts[1].isdigit():
            raise ValueError(f"Invalid step value: {step_parts[1]}")
        step = int(step_parts[1])

    # Handle range delimiters
    delimiter_pattern = "|".join(re.escape(d) for d in SUPPORTED_DELIMITERS)
    range_match = re.split(delimiter_pattern, range_part)

    if len(range_match) == 1: # It's a single number
        if not range_match[0].isdigit():
            raise ValueError(f"Invalid number: {range_match[0]}")
        num = int(range_match[0])
        return num, num, step
    elif len(range_match) == 2: # It's a range
        start_str, end_str = range_match
        if not start_str.isdigit() or not end_str.isdigit():
            raise ValueError(f"Invalid range with non-numeric values: {part}")
        return int(start_str), int(end_str), step
    else:
        raise ValueError(f"Invalid part format: {part}")

def _format_output(numbers: set[int], output_format: str) -> list[int] | set[int] | str:
    """
    Formats the final set of numbers into the desired output type.

    Args:
        numbers: The set of expanded numbers.
        output_format: The target format ('list', 'set', or 'csv').

    Returns:
        The formatted numbers.
    """
    sorted_numbers = sorted(list(numbers))
    if output_format == "list":
        return sorted_numbers
    elif output_format == "set":
        return set(sorted_numbers)
    elif output_format == "csv":
        return ",".join(map(str, sorted_numbers))
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

def expand_string_range(
    input_string: str | None,
    output_format: str = "list",
) -> list[int] | set[int] | str | None:
    """
    Expands a string of numbers and ranges into a list, set, or CSV string of integers.

    This function handles all scenarios including custom delimiters, steps, reversed ranges,
    and different output formats. It includes error handling for invalid parts.

    Args:
        input_string: The string to expand.
        output_format: The desired output format ('list', 'set', or 'csv').

    Returns:
        The expanded sequence in the specified format, or None if the input is None or invalid.
    """
    if input_string is None:
        return None
    
    all_numbers = set()
    try:
        print("Starting range expansion process...")
        # Stage 2: Ignore Whitespace and Empty Parts
        parts = [part.strip() for part in input_string.split(",") if part.strip()]
        
        for part in parts:
            try:
                start, end, step = _parse_part(part)

                # Stage 4: Handle Reversed Ranges
                if start > end:
                    # Generate numbers in descending order
                    all_numbers.update(range(start, end - 1, -step))
                else:
                    # Generate numbers in ascending order
                    all_numbers.update(range(start, end + 1, step))
            except ValueError as e:
                print(f"Warning: Skipping invalid part '{part}'. Reason: {e}")

        return _format_output(all_numbers, output_format)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    finally:
        print("Range expansion process finished.")


if __name__ == '__main__':
    # Example usages demonstrating various scenarios
    print("\n--- Scenario: Basic Expansion ---")
    print(f"Input: '1-3,5,7-9', Output: {expand_string_range('1-3,5,7-9')}")

    print("\n--- Scenario: Invalid Input Handling ---")
    print(f"Input: '1-a,2,4-b,5', Output: {expand_string_range('1-a,2,4-b,5')}")

    print("\n--- Scenario: CSV Output ---")
    print(f"Input: '1-3,3-5', Output: {expand_string_range('1-3,3-5', output_format='csv')}")
