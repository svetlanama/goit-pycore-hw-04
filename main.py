from app.total_salary import total_salary
from app.get_cats_info import get_cats_info

# Task 1:
total, average = total_salary("app/data/salary_file.txt")
print(f"Total salary sum: {total}, AVG sum: {average}")

# Task 2:
cats_info = get_cats_info("app/data/cats_file.txt")
print(cats_info)
