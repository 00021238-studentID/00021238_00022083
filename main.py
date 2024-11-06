#Timetable Creator by 00021238 & 00022083

def add_subject(subject, day, order): #adds subject to the timetable
    if order < 1: #checks if the order is valid
        print("Order is too low. Please enter a valid order.")
        return

    if order > len(timetable[day]): #checks if the order is valid
        timetable[day].insert(order-1, subject)
        print(f"{subject} added to {day} at the last position.")
    else: #adds subject to the timetable
        timetable[day].insert(order-1, subject)
        print(f"{subject} is added to {day} at order {order}.")