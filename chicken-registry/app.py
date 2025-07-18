import csv
path="chicken.csv"
def load():
    try:
        chicken=[]
        with open(path,'r',newline='') as file:
            reader=csv.reader(file)
            column_name=next(reader)
            for i in reader:
                chicken.append(i[0])
        return chicken
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
def append(name):
    try:
        with open(path,'a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([name])
            print("Chicken write to the file successfully!")
    except PermissionError:
        print("Still permission denied with simple write.")
    except Exception as e:
        print("An error occurred:", e)
def list(chickens):
    for i in chickens:
        print(i)
def create(chickens):
    print(chickens)
    name=input("Enter the name of the chicken: ")
    if name in chickens:
        print("Chicken already exists!")
        return
    else:
        chickens.append(name)
        append(name)
        print("Chicken created successfully!")    

def update(chickens):
    print(chickens)
    name=input("Enter the name of the chicken to updated")
    if name not in chickens:
        print("Chicken not found")
    else:
        index=chickens.index(name)
        name=input("Enter the new name of the chicken: ")
        chickens[index]=name
        try:
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name"])  # re-write header
                for name in chickens:
                    writer.writerow([name])
        except Exception as e:
            print("An error occurred while updating:", e)
        print("Chicken updated successfully!")

def delete(chickens):
    print(chickens)
    name=input("Enter the name of the chicken to deleted")
    if name not in chickens:
        print("Chicken not found")
    else:
        chickens.remove(name)
        print("Chicken deleted successfully!")
def main():
    chickens=load()
    print(chickens)
    print("Menu -")
    print("0 - Exit App")
    print("1 - Print List of Chicken Records")
    print("2 - Create New Chicken Record")
    print("3 - Update Existing Chicken Record")
    print("4 - Delete a Chicken Record")
    while True: 
        choice = input("Choose an option: ")
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            list(chickens)
        elif choice == '2':
            create(chickens)
        elif choice == '3':
            update(chickens)
        elif choice == '4':
            delete(chickens)
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

main()
