class StudentRegistration:
    def __init__(self, Name, Registration):
        self.Name = Name
        self.Registration = Registration

    def display_registration(self):
        print(f"Student: {self.Name}, Registration Number: {self.Registration}")

# Example usage:
student1 = StudentRegistration("Alice", "S24B13/123")
student2 = StudentRegistration("Bob", "S24B13/456")

student1.display_registration()
student2.display_registration()
