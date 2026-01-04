# https://adventofcode.com/2025/day/10

import ast #for getting tuples from input

#Find the minimum number of pushes required to make the lights match the target
#Observation: it never makes sense to push a button twice.
#Otherwise, the button could be pushed zero times for the same result
def find_min_pushes(target, buttons):
    #display: the current display. We're done if it reaches target.
    #pushed: number of buttons that have been pushed
    #start: the first index in buttons to look at. If we've already used buttons[2], 
    #   then we won't look at any earlier indexes because they're covered by other cases
    #This is the case because we use a queue to prioritize looking at the smallest number of buttons pushed first
    #   and early buttons are prioritized over later buttons
    q = [{"display": ([False for _ in range(len(target))]), "start": 0, "pushed": 0}]
    entry_num = 0
    while entry_num < len(q):
        entry = q[entry_num]
        display = entry["display"]
        start = entry["start"]
        pushed = entry["pushed"]
        if display==target:
            return entry["pushed"]
        for i in range(start, len(buttons)):
            button = buttons[i]
            new_display = list(display)
            #push the button, updating the new display
            for switch in button:
                new_display[switch] = not new_display[switch]
            q.append({"display": tuple(new_display), "start": i+1, "pushed": pushed+1})
        entry_num+=1
        
if __name__ == "__main__":
    with open("input.txt") as file:
        total_pushes = 0
        for line in file:
            #Input
            parsed_line = line.rstrip().split()
            str_target = parsed_line[0][1:len(parsed_line[0])-1] #leave out opening and trailing brackets
            target = tuple([True if c=="#" else False for c in str_target]) #get target diagram into boolean form
            str_buttons = parsed_line[1:len(parsed_line)-1]
            buttons = []
            for str_button in str_buttons:
                #get the tuple from the string
                t = ast.literal_eval(str_button)
                #isinstance is used because (3) will be evaluated as integer 3
                if isinstance(t,tuple):
                    buttons.append(t)
                else:
                    buttons.append((t,))
            total_pushes += find_min_pushes(target, buttons)
        print(total_pushes)
