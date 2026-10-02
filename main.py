tasks = []

while True:
    print("\n--- To-do Manager ---")
    print("[1] Aufgabe hinzufügen")
    print("[2] Aufgaben anzeigen")
    print("[3] Beenden")

    choice = input("Auswahl: ")

    if choice == "1":
        task = input("Neue Aufgabe: ")
        tasks.append(task)
        print("Aufgabe hinzugefügt.")

    elif choice == "2":
        print("\nAufgaben:")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")