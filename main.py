import random
import time

#important comment
# ● ┌ ─ ┐ │ └ ┘ 

money,income,brain_cell,work_energy= 0,0,0,0
mainloop,gain_brain_cell = 1,1
job = ""
job_id = ["0","1","2","3","4","999"]
max_energy,energy = 100,100
inventory = []
items = ["potato","super potato","carrot","shiny carrot","tomato","big tomato","watermelon","square watermelon","pumpkin","golden pumpkin"]
item_chances = [10,4,15,7,15,7,15,6,15,6]

card = {
    'wlcm': ("┌─────────────────────────────────────────────────┐",
             "│ Welcome to the world! Say hello world!          │",
             "│ This is a game of hello to the world            │",
             "│ Type /command to check out what command we have │",
             "└─────────────────────────────────────────────────┘"),

    'command': ("┌─────────────────────────────────────────────────┐", 
                "│ /command to find out what are all the commands  │",
                "│ /work to work for money                         │",
                "│ /sleep to sleep and gain energy                 │",
                "│ /study to study and gain brain cells            │",
                "│ /stop to stop playing the game                  │",
                "└─────────────────────────────────────────────────┘"),

    'joblist': ("┌─────────────────────────────────────────────────┐",
                "│ Quit the job[id: 0]                             │",
                "│ Farmer[id: 1]                                   │",
                "│ Miner[id: 2]                                    │",
                "│ Engineer[id: 3]                                 │",
                "│ Scientist[id: 4]                                │",
                "│ /jobchoose to choose the job                    │",
                "└─────────────────────────────────────────────────┘"),

    'farmer': ("┌─────────────────────────────────────────────────┐",
               "│ Salary: 20$                                     │",
               "│ Energy: 50                                      │",
               "│ Brain cells required: 0                         │",
               "│ Desc: Potato farming                            │",
               "└─────────────────────────────────────────────────┘"),
            
    'miner': ("┌─────────────────────────────────────────────────┐",
              "│ Salary: 40$                                     │",
              "│ Energy: 70                                      │",
              "│ Brain cells required: 1                         │",
              "│ Desc: Trying to get diamond                     │",
              "└─────────────────────────────────────────────────┘"),

    'engineer': ( "┌─────────────────────────────────────────────────┐",
                  "│ Salary: 100$                                    │",
                  "│ Energy: 50                                      │",
                  "│ Brain cells required: 20                        │",
                  "│ Desc: I fix and make machine                    │",
                  "└─────────────────────────────────────────────────┘"),

    'scientist': ( "┌─────────────────────────────────────────────────┐",
                   "│ Salary: 1000$                                   │",
                   "│ Energy: 50                                      │",
                   "│ Brain cells required: 100                       │",
                   "│ Desc: Doing for the greater good of humanity    │",
                   "└─────────────────────────────────────────────────┘"),
}

def cards(name,card):
    for row in card.get(name):
        print(row)

def start():
    while (len(name := input("Enter your name[must be 3 character or more]: "))) < 3:
        print()

    print(f"hi {name},")
    cards("wlcm",card)

def command():
    print("Here is a list of commands")
    cards("command",card)

def work():
    global money,income,energy
    if job == "":
        print("get a job with /joblist")
        return

    elif energy < work_energy:
        print("You have not enough energy")
        return

    else:
        match job:
            case "farmer":
                if random.randrange(1, 100) < 51:
                    item = str(random.choices(items, item_chances)).strip("[']")
                    print(f"You got a {item}")
                    inventory.append(item)
                    print(inventory)

            case "miner":
                pass

            case "engineer":
                pass

            case "scientist":
                pass

        energy -= work_energy
        money += income
        print(f"You work as a {job}")
        print(f"You earned {income} dollar")
        print(f"You now have {money}$\n")

def joblist():
    print("\nHere is a list of jobs")
    cards("joblist",card)

def jobchoose():
    global job,job_id,income,work_energy
    while (job_choice := input("\nEnter the job id to get a job[Enter 999 to exit]: ")) not in job_id:
        print("Invalid id")
    if job_choice == "999":
        pass

    elif job_choice == "0":
        job = ""
        print("\nJob quited")

    elif job_choice == "1":
        job = "farmer"
        income = 20
        work_energy = 50
        print(f"\nYou work as a {job}")
        cards("farmer",card)

    elif job_choice == "2":
        if brain_cell < 1:
            print("\nYou have not enough brain cells")
            return

        job = "miner"
        income = 40
        work_energy = 70
        print(f"\nYou work as a {job}")
        cards("miner",card)

    elif job_choice == "3":
        if brain_cell < 20:
            print("\nYou have not enough brain cells")
            return

        job = "engineer"
        income = 100
        work_energy = 50
        print(f"\nYou work as a {job}")
        cards("engineer",card)

    elif job_choice == "4":
        if brain_cell < 20:
            print("\nYou have not enough brain cells")
            return
            
        job = "scientist"
        income = 1000
        work_energy = 50
        print(f"\nYou work as a {job}")
        cards("scientist",card)

def sleep():
    global energy
    energy = max_energy
    print(f"\nEnergy restored. You now have {energy}/{max_energy}")

def study():
    global brain_cell
    brain_cell += gain_brain_cell
    print(f"\nYou gain {gain_brain_cell} brain cell. You now have {brain_cell} brain cells")

def main():
    global mainloop
    while mainloop:
        commands = input("\nType something here: ")
        match commands.lower():
            case "/command":
                command()
            case "/work":
                work()
            case "/sleep":
                sleep()
            case "/stop":
                mainloop = 0
                print("\nThanks for playing\n")
            case "/joblist":
                joblist()
            case "/jobchoose":
                jobchoose()
            case "/study":
                study()

if __name__ == "__main__":
    try:
        start()
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for playing\n")