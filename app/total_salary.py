def total_salary(path) -> (int, int):
    """
    Analyzes a file with developer salaries and returns a tuple:
    (total salary sum, average salary)
    """
    try:
        with open(path, encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    # Not a correct row - skip
                    continue
            if count == 0:
                return 0, 0
            average = total // count
            return total, average
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0
