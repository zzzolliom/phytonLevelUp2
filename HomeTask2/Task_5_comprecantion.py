# Задача 5: Допустим, у нас есть два списка одинаковой длины, names и ages, содержащие соответственно имена и возрасты людей.
# Мы хотим создать новый список строк, в которых будут указаны имена и возрасты в формате "Имя - возраст". Напишите comprehension, который решает эту задачу

def create_name_age_strings(names: list, ages: list) -> list:
    lst=(list(zip(names, ages)))
    new_lst = [f"{name} - {age}" for name, age in lst]
    return new_lst

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
create_name_age_strings(names,ages)
def test_create_name_age_strings():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    expected = ['Alice - 25', 'Bob - 30', 'Charlie - 35']
    result = create_name_age_strings(names, ages)
    assert result == expected

    names = []
    ages = []
    expected = []
    result = create_name_age_strings(names, ages)
    assert result == expected
    print("All test_create_name_age_strings pass")
test_create_name_age_strings()

