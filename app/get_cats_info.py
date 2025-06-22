def get_cats_info(path):
    """
    Reads file and return array of objects: 'id', 'name', 'age'.
    """
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    # Not a correct row - skip
                    continue
        return cats
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return [] 