class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return f"Имя: {contact.name}\n Номер телефона: {contact.phone}\nEmail: {contact.email}"
        return "Контакт не найден"

    def list_contacts(self):
        if not self.contacts:
            print("Список контактов пуст")
        else:
            print("Список контактов:")
            for contact in self.contacts:
                print(f"Имя: {contact.name}\n Номер телефона: {contact.phone}\nEmail: {contact.email}\n")

# Создание экземпляров класса "Contact"
contact1 = Contact("Иван Петров", "+123456789", "ivan@example.com")
contact2 = Contact("Мария Иванова", "+987654321", "maria@example.com")

# Создание экземпляра класса "ContactManager"
manager = ContactManager()

# Добавление контактов в адресную книгу
manager.add_contact(contact1)
manager.add_contact(contact2)

# Вывод списка контактов
manager.list_contacts()

# Поиск контакта по имени
result = manager.find_contact("Иван Петров")
print(result)
