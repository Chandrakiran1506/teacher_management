class Teacher:
    def __init__(self, full_name, age, dob, num_classes):
        self.full_name = full_name
        self.age = age
        self.dob = dob
        self.num_classes = num_classes

class TeacherManagementSystem:
    def __init__(self):
        self.teachers = []

    def show_all_teachers(self):
        for i, teacher in enumerate(self.teachers, 1):
            print(f"{i}. {teacher.full_name} - Age: {teacher.age}, DOB: {teacher.dob}, Classes: {teacher.num_classes}")

    def add_teacher(self, full_name, age, dob, num_classes):
        new_teacher = Teacher(full_name, age, dob, num_classes)
        self.teachers.append(new_teacher)
        print(f"Teacher {full_name} added successfully!")

    def filter_teachers_by_age(self, target_age):
        filtered_teachers = [teacher for teacher in self.teachers if teacher.age == target_age]
        for teacher in filtered_teachers:
            print(f"{teacher.full_name} - Age: {teacher.age}, DOB: {teacher.dob}, Classes: {teacher.num_classes}")

    def filter_teachers_by_num_classes(self, target_num_classes):
        filtered_teachers = [teacher for teacher in self.teachers if teacher.num_classes == target_num_classes]
        for teacher in filtered_teachers:
            print(f"{teacher.full_name} - Age: {teacher.age}, DOB: {teacher.dob}, Classes: {teacher.num_classes}")

    def search_teacher(self, full_name):
        for teacher in self.teachers:
            if teacher.full_name.lower() == full_name.lower():
                print(f"{teacher.full_name} - Age: {teacher.age}, DOB: {teacher.dob}, Classes: {teacher.num_classes}")
                return
        print(f"Teacher {full_name} not found.")

    def update_teacher_record(self, full_name, new_age, new_dob, new_num_classes):
        for teacher in self.teachers:
            if teacher.full_name.lower() == full_name.lower():
                teacher.age = new_age
                teacher.dob = new_dob
                teacher.num_classes = new_num_classes
                print(f"Teacher {full_name}'s record updated successfully.")
                return
        print(f"Teacher {full_name} not found.")

    def delete_teacher(self, full_name):
        for teacher in self.teachers:
            if teacher.full_name.lower() == full_name.lower():
                self.teachers.remove(teacher)
                print(f"Teacher {full_name} deleted successfully.")
                return
        print(f"Teacher {full_name} not found.")


# Example usage
if __name__ == "__main__":
    teacher_management_system = TeacherManagementSystem()

    while True:
        print("\nTeacher Management System\n")
        print("1. Show all teachers")
        print("2. Add a teacher")
        print("3. Filter teachers by age")
        print("4. Filter teachers by number of classes")
        print("5. Search for a teacher")
        print("6. Update a teacher's record")
        print("7. Delete a teacher")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            teacher_management_system.show_all_teachers()
        elif choice == "2":
            full_name = input("Enter full name: ")
            age = int(input("Enter age: "))
            dob = input("Enter date of birth: ")
            num_classes = int(input("Enter number of classes: "))
            teacher_management_system.add_teacher(full_name, age, dob, num_classes)
        elif choice == "3":
            target_age = int(input("Enter target age: "))
            teacher_management_system.filter_teachers_by_age(target_age)
        elif choice == "4":
            target_num_classes = int(input("Enter target number of classes: "))
            teacher_management_system.filter_teachers_by_num_classes(target_num_classes)
        elif choice == "5":
            full_name = input("Enter full name to search: ")
            teacher_management_system.search_teacher(full_name)
        elif choice == "6":
            full_name = input("Enter full name to update: ")
            new_age = int(input("Enter new age: "))
            new_dob = input("Enter new date of birth: ")
            new_num_classes = int(input("Enter new number of classes: "))
            teacher_management_system.update_teacher_record(full_name, new_age, new_dob, new_num_classes)
        elif choice == "7":
            full_name = input("Enter full name to delete: ")
            teacher_management_system.delete_teacher(full_name)
        elif choice == "8":
            print("Exiting Teacher Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
