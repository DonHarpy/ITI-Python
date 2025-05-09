import datetime

class Person:
    def __init__(self, full_name, health_rate, cash, emotion):
        self.name = full_name
        self.health_rate = health_rate
        self.money = cash
        self.mood = emotion

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'Happy'
        elif hours < 7:
            self.mood = 'Tired'
        else:
            self.mood = 'Lazy'

    def buy(self, item_count):
        self.money -= item_count * 10

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50


class Car:
    def __init__(self, name, speed, fuel_rate):
        self.model = name
        self.velocity = min(max(speed, 0), 200)
        self.fuel_rate = min(max(fuel_rate, 0), 100)

    def run(self, velocity, km_distance):
        self.velocity = min(max(velocity, 0), 200)
        fuel_usage = km_distance * 0.1
        if self.fuel_rate >= fuel_usage:
            self.fuel_rate -= fuel_usage
            self.stop("Arrived successfully.")
        else:
            km_done = self.fuel_rate / 0.1
            self.fuel_rate = 0
            self.stop(f"Stopped after {km_done:.1f} km - out of fuel.")

    def stop(self, message):
        self.velocity = 60
        print(f"[{self.model}] stopped: {message}")


class Employee(Person):
    def __init__(self, full_name, cash, emotion, health_rate, emp_id, car, email, salary, distanceToWork):
        super().__init__(full_name, health_rate, cash, emotion)
        self.emp_id = emp_id
        self.car = car
        self.salary = salary
        self.email = email
        self.commute_distance = distanceToWork

    def send_mail(self, to, subject, body, receiver_name):
        print(f"""
        To: {to}
        Subject: {subject}
        Hi {receiver_name},
        {body}
        """)

    def work(self, hours):
        if hours == 8:
            self.mood = 'Happy'
        elif hours > 8:
            self.mood = 'Tired'
        else:
            self.mood = 'Lazy'

    def drive(self, velocity, km):
        self.car.run(velocity, km)

    def refuel(self, quantity=100):
        self.car.fuel_rate = min(self.car.fuel_rate + quantity, 100)


class Office:
    employee_count = 0

    def __init__(self, office_name):
        self.name = office_name
        self.employees = []

    def hire(self, emp):
        self.employees.append(emp)
        Office.employee_count += 1

    def fire(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        Office.employee_count -= 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        return next((e for e in self.employees if e.emp_id == emp_id), None)

    def reward(self, emp_id, value):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += value

    def deduct(self, emp_id, value):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= value

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            late_by = Office.calculate_lateness(9, move_hour, emp.commute_distance, emp.car.velocity)
            if late_by is None:
                print("Can't calculate lateness (speed is zero).")
                return

            if late_by > 10:
                self.reward(emp_id, 10)
            elif late_by < -10:
                self.deduct(emp_id, 10)
            else:
                print(f"{emp.name} arrived on time.")

    @staticmethod
    def calculate_lateness(target_hour, departure, distance, speed):
        if speed == 0:
            return None
        total_time = distance / speed
        return (departure + total_time) - target_hour

    @classmethod
    def change_emps_num(cls, value):
        cls.employee_count = value
