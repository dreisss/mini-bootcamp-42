#!/usr/bin/env python

from random import choice

group_size = 3
groups = []

with open("./participants") as file:
    participants = file.read().split("\n")

while len(participants) > group_size:
    group = []

    for _ in range(group_size):
        participant = choice(participants)

        group.append(participant)
        participants.remove(participant)

    groups.append(group)

groups.append(participants)

print(groups)
