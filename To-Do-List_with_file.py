import time

sl=1.2 # Create a variable to store the sleep time.

# Function to add a task to the to-do list
def add_task(task):
    with open('todo.txt', 'a') as f:  # Open the file in append mode
        f.write(f'{task},0\n')  # Write the task to the file with a status of 0 (not done)
    print('Task added successfully!')  # Print a success message
    time.sleep(sl)

# Function to view the to-do list
def view_list():
    with open('todo.txt', 'r') as f:  # Open the file in read mode
        tasks = f.readlines()  # Read all lines of the file into a list
    if tasks:  # If the list is not empty
        print('To-Do List:')  # Print a header
        for i, task in enumerate(tasks):  # Loop through each task in the list
            task, status = task.strip().split(',')  # Split the task into its name and status
            print(f'{i+1}. {task} done : {status}')  # Print the task with its number, status, and name
    else:  # If the list is empty
        print('Your to-do list is empty.')  # Print a message indicating that the list is empty
    time.sleep(sl)

# Function to mark a task as done
def mark_done(task_num):
    with open('todo.txt', 'r') as f:  # Open the file in read mode
        tasks = f.readlines()  # Read all lines of the file into a list
    if tasks:  # If the list is not empty
        try:  # Try to convert the task number to an integer
            task_num = int(task_num)
            if task_num > 0 and task_num <= len(tasks):  # If the task number is valid
                tasks[task_num-1] = tasks[task_num-1].replace(',0', ',1')  # Replace the task's status with 1 (done)
                with open('todo.txt', 'w') as f:  # Open the file in write mode
                    f.writelines(tasks)  # Write the modified list of tasks to the file
                print('Task marked as done!')  # Print a success message
            else:  # If the task number is invalid
                print('Invalid task number.')
        except ValueError:  # If the task number cannot be converted to an integer
            print('Invalid task number.')
    else:  # If the list is empty
        print('Your to-do list is empty.')  # Print a message indicating that the list is empty
    time.sleep(sl)

# Function to remove a task from the to-do list
def remove_task(task_num):
    with open('todo.txt', 'r') as f:  # Open the file in read mode
        tasks = f.readlines()  # Read all lines of the file into a list
    if tasks:  # If the list is not empty
        try:  # Try to convert the task number to an integer
            task_num = int(task_num)
            if task_num > 0 and task_num <= len(tasks):  # If the task number is valid
                with open('todo.txt', 'w') as f:  # Open the file in write mode
                    for i, task in enumerate(tasks):  # Loop through each task in the list
                        if i != task_num-1:  # If the task is not the one to be removed
                            f.write(task)  # Write the task to the file
                print('Task removed successfully!')  # Print a success message
            else:  # If the task number is invalid
                print('Invalid task number.')
        except ValueError:  # If the task number cannot be converted to an integer
            print('Invalid task number.')
    else:  # If the list is empty
        print('Your to-do list is empty.')  # Print a message indicating that the list is empty
    time.sleep(sl)

# Main program loop
while True:
    print('\nWhat would you like to do?')
    print('1. Add a task')
    print('2. View your to-do list')
    print('3. Mark a task as done')
    print('4. Remove a task')
    print('5. Quit')

    choice = input('Enter your choice (1-5): ')

    if choice == '1':  # If the user chooses to add a task
        task = input('Enter the task: ')
        add_task(task)  # Call the add_task function with the user's input

    elif choice == '2':  # If the user chooses to view the to-do list
        view_list()  # Call the view_list function

    elif choice == '3':  # If the user chooses to mark a task as done
        view_list()  # Call the view_list function
        task_num = input('Enter the task number to mark as done: ')
        mark_done(task_num)  # Call the mark_done function with the user's input

    elif choice == '4':  # If the user chooses to remove a task
        task_num = input('Enter the task number to remove: ')
        remove_task(task_num)  # Call the remove_task function with the user's input

    elif choice == '5':  # If the user chooses to quit
        time.sleep(1)
        break  # Exit the program

    else:  # If the user enters an invalid choice
        print('Invalid choice. Please try again.')  # Print an error message
        time.sleep(sl)
