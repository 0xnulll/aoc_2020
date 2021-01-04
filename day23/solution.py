from parse import *
import sys
from collections import defaultdict, Counter

class Node:
    def __init__(self,i,next=None):
        self.val = i
        self.next = next
    def __repr__(self):
        return f"{self.val} => {self.next.val}"

def print_nodes(h):
    v = h.next
    print(h.val,end="")
    while v != h:
        print(",",v.val,end="")
        v = v.next

def simulate(cups, maxx, minn, steps):
    head = Node(cups[0])
    all_index = { cups[0] : head }
    prev = head
    for c in cups[1:]:
        n = Node(c)
        all_index[c], prev.next, prev = n, n, n
    prev.next, current = head, head
    for i in range(steps):
        pick = []
        k = current.next
        for j in range(3):
            pick.append(k)
            k = k.next
        current.next = k # removing picked up cups
        d = current.val
        picked_up_val = {pick[0].val,pick[1].val,pick[2].val }
        while True:  # finding proper destination
            d = d - 1
            if d < minn:
                d = maxx
            if d not in picked_up_val:
                break
        #changing links, pushing picked up cups after destination cups
        all_index[d].next, pick[2].next = pick[0] , all_index[d].next
        current = current.next # next current
    return all_index


def get_solution_1(cups):
    all_index = simulate(cups,max(cups),min(cups),100)
    s,ans = all_index[1].next, ""
    while s != all_index[1]:
        ans += str(s.val)
        s= s.next
    return ans

def get_solution_2(cups):
    maxx = max(cups)
    for i in range(1000000-len(cups)):
        maxx = maxx+1
        cups.append(maxx)
    all_index = simulate(cups,1000000,1,10000000)
    s = all_index[1].next
    return s.val * s.next.val


def process_input(input):
    cups = {}
    for line in input.split("\n\n"):
        pass
    return cups

input_processed = [int(d) for d in list("467528193")]
r1 = get_solution_1(input_processed)
print(
    f"Solution 1 = {r1}")
r2 = get_solution_2(input_processed)
print(
    f"Solution 2 = {r2}")
