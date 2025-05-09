from work_environment import Office, Car, Employee

# Office and employee setup
iti = Office("ITI Smart Village")
my_fiat = Car("Fiat 128", speed=60, fuel_rate=100)
sam = Employee("Samy", 1000, "Neutral", 80, emp_id=1, car=my_fiat, email="samy@iti.org", salary=5000, distanceToWork=20)

iti.hire(sam)

print("-- Sam is starting his daily routine --")
sam.drive(velocity=60, km=20)
iti.check_lateness(emp_id=1, move_hour=7.0)

print(f"Salary: {sam.salary}")
print(f"Fuel left in car: {sam.car.fuel_rate}")
