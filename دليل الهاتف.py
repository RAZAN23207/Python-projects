# تعريف دليل الهاتف كقائمة من القواميس
phone_book = {
    "Amal": "1111111111",
    "Mohammed": "2222222222",
    "Khadijah": "3333333333",
    "Abdullah": "4444444444",
    "Rawan": "5555555555",
    "Faisal": "6666666666",
    "Layla": "7777777777"
}

def search_by_number(number):
    # التحقق من صحة الرقم
    if not number.isdigit() or len(number) != 10:
        return "This is invalid number"
    
    # البحث عن الاسم باستخدام الرقم
    for name, num in phone_book.items():
        if num == number:
            return name
    
    return "Sorry, the number is not found"

def search_by_name(name):
    # البحث عن الرقم باستخدام الاسم
    if name in phone_book:
        return phone_book[name]
    return "Sorry, the name is not found"

def add_new_entry(name, number):
    # التحقق من صحة الرقم
    if not number.isdigit() or len(number) != 10:
        return "This is invalid number"
    
    # إضافة إدخال جديد للدليل
    if name in phone_book:
        return "This name already exists in the phone book"
    
    phone_book[name] = number
    return "Entry added successfully"

# واجهة المستخدم
while True:
    print("\nPhone Book Menu:")
    print("1. Search by number")
    print("2. Search by name")
    print("3. Add new entry")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        number = input("Enter the phone number: ")
        print(search_by_number(number))
    elif choice == "2":
        name = input("Enter the name: ")
        print(search_by_name(name))
    elif choice == "3":
        name = input("Enter the name: ")
        number = input("Enter the phone number: ")
        print(add_new_entry(name, number))
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select again.")
