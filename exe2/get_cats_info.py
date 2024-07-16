def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                cat_id, cat_name, cat_age = line.split(",")
                cat_dict = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age
                }
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Помилка: '{path}' - за таким шляхом файлу не знайдено.")
        return []  
    
    return cats_list

