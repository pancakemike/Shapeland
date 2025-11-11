class Node:
    def __init__(self, parent) -> None:
        self.parent = parent

class Stack:
    def __init__(self) -> None:
        self.frontier = []
    
    def push(self, data):
        self.frontier.append(data)
    
    def view_top(self):
        return self.frontier[-1]
    
    def pop(self):
        self.frontier = self.frontier[:-1]
    
    def is_empty(self):
        return len(self.frontier) == 0

stack = Stack() 

print(stack.is_empty())
stack.push("A")
stack.push("B")
stack.push("C")
print(stack.frontier)
print(stack.view_top())
stack.pop()
print(stack.view_top())
stack.pop()
print(stack.view_top())
stack.pop()
print(stack.is_empty())


import random

def roll(sides, bias_list):
    assert len(bias_list) == sides
    number = random.uniform(0, sum(bias_list))
    current = 0
    for i, bias in enumerate(bias_list):
        current += bias
        if number <= current:
            return i + 1

roll(6,[0.8,0.04,0.04,0.04,0.04,0.04])
roll(6,[0.8,0.04,0.04,0.04,0.04,0.04])
roll(6,[0.8,0.04,0.04,0.04,0.04,0.04])
roll(6,[0.8,0.04,0.04,0.04,0.04,0.04])
roll(6,[0.8,0.04,0.04,0.04,0.04,0.04])


def change_status(status, string, stack:Stack):
    if status == 7:
        return 1
    if status == 0:
        status = 1
        stack.push("#")
        return change_status(status, string, stack)
    if status == 1:
        if string[0] == "i" and stack.view_top() == '#':
            string = string[1:]
            status = 2
            stack.push("I")
            return change_status(status, string, stack)
    if status == 2:
        if string[0] == 'i' and stack.view_top() == "I":
            string = string[1:]
            status = 3
            stack.push("I")
            return change_status(status, string, stack)
    if status == 3:
        if string[0] == 'i' and stack.view_top() == "I":
            string = string[1:]
            status = 2
            stack.push("I")
            return change_status(status, string, stack)
        if string[0] == "j" and stack.view_top() == "I":
            string = string[1:]
            status = 4
            stack.push("J")
            return change_status(status, string, stack)
    if status == 4:
        if string[0] == 'j' and stack.view_top() == 'J':
            string = string[1:]
            status = 5
            stack.push("J")
            return change_status(status, string, stack)
    if status == 5:
        if string[0] == 'j' and stack.view_top() == 'J':
            string = string[1:]
            status = 4
            stack.push("J")
            return change_status(status, string, stack)    
        if string[0] == 'k' and stack.view_top() == 'J':
            string = string[1:]
            status = 6
            stack.pop()
            return change_status(status, string, stack)
    if status == 6:
        if string[0] == 'k' and (stack.view_top() == 'J' or stack.view_top() == 'I'):
            string = string[1:]
            status = 6
            stack.pop()
            return change_status(status, string, stack)
        if string[0] == 'l' and stack.view_top() == "#":
            status = 7
            stack.pop()
            return change_status(status, string, stack)
    else: return 0

def automaton(string):
    stack = Stack()
    status = 0
    return change_status(status, string, stack)

print(automaton("iiiijjjjkkkkkkkkl"))
print(automaton("iiijjjjkkkkkkkl"))