# Создание класса "Телефонная книга" с атрибутами "имя", "номер телефона".
# Реализовать методы для добавления и удаления контакта, изменения данных контакта, вывода информации о всех контактах, а также поиска контакта по имени.

# импортируем класс
class Phonebook:
    all_contacts = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Phonebook.all_contacts.append(self)
    @classmethod
    def add_contact(cls,contact):
        cls.all_contacts.append(contact)


    def change_phone(self,phone):
        self.phone_number = phone

    @classmethod
    def print_contacts(self):
        for contact in Phonebook.all_contacts:
            print(f'имя: {contact.name}, номер телефона: {contact.phone_number}')


    @classmethod
    def search_contact(cls, name):
        for contact in Phonebook.all_contacts:
            if contact.name == name:
                print(f'Имя : {contact.name}, номер : {contact.phone_number}' )






# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contact("Петр Петров")