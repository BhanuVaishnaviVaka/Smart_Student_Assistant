from datetime import datetime
def add_task(task,deadline):
    with open("tasks.txt","a",encoding="utf-8") as f:
        f.write(f"{task}|{deadline}\n")
    print(f"Task added: {task}(Deadline:{deadline})")
def list_tasks():
    try:
        with open("tasks.txt","r",encoding="utf-8") as f:
            tasks = f.readlines()
        if tasks:
            print("\nYour Tasks: ")
            for i,task in enumerate(tasks, start=1):
                print(f"{i}.{task.strip()}")
        else:
            print("\nNo Tasks Found.")
    except FileNotFoundError:
        print("No Tasks File Found. Add a Task First!")
def main():
    while True:
        print("\nSmart Student Assistant")
        print("1.Add a Task with deadline")
        print("2.List Tasks")
        print("3.Exit")
        choice=input("Choose an option: ")
        if choice=="1":
            task=input("Enter your Task: ")
            deadline=input("Enter deadline(YYYY-MM-DD.):")
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
                add_task(task,deadline)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice=="2":
            list_tasks()
        elif choice=="3":
            print("GoodBye!!")
            break
        else:
            print("Invalid Choice. Try Again")
if __name__=="__main__":
    main()
