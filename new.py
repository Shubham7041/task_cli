import argparse
import json

# Global variables
parser = argparse.ArgumentParser()
name_list = {}

#This code checks and add new tasks
def add_task(task : str, list : dict):
    if len(task) > 0:
        if len(list.keys()) == 0:
            return list.update({1:task})
        else:
            return list.update({len(list.keys())+1 : task})
    else: return


#Loading jason file to read
with open("name.json", 'r+') as file:
    name_list = json.load(file)

    parser.add_argument('--add', help="To Add New Task", action='store_true')
    parser.add_argument('--list', help='List all Names', action='store_true')
    parser.add_argument('task', nargs='?' ,help="The Task you want to add", type=str)
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()

    if args.add:
        print(f"your name is {args.task}")
        add_task(args.task, name_list)

    if args.list:
        print(f"list of name : {name_list}")    
    
    print(vars(args))

    file.seek(0)

    #This code stores the name_list into a json file
    json.dump(name_list, file)


file.close()