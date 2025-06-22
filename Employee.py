class Employee:
    def __init__(self, emp_id, name, salary):

        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary


    def get_emp_id(self):
        return self.__emp_id


    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id


    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name


    def get_salary(self):
        return self.__salary


    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")


    def display_info(self):
        print("\n--- Employee Information ---")
        print(f"Employee ID   : {self.__emp_id}")
        print(f"Name          : {self.__name}")
        print(f"Current Salary: ₹{self.__salary:.2f}")


    def give_hike(self, percentage):
        if percentage > 0:
            hike = self.__salary * (percentage / 100)
            self.__salary += hike
            print(f"\nSalary increased by {percentage}%. New Salary: ₹{self.__salary:.2f}")
        else:
            print("\nInvalid hike percentage. Must be greater than 0.")
