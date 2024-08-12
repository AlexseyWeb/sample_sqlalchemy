import keyboard

def enter_data():
    try:
        while True:
            # id = int(input("Enter id -> "))
            title = input("Title of product -> ")
            price = float(input("Enter float numbers-> "))
    except KeyboardInterrupt as e:
        print("     OK      ")
    finally:
        return (id, title, price)
