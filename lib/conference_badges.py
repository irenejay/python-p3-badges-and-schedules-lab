def badge_maker(name):
    return "Hello, my name is " + name + "."


print(badge_maker("Arel"))


def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append("Hello, my name is " + name + ".")
    return badge_messages

def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(speaker, i))
    return room_assignments

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append("Hello, my name is " + name + ".")
    return badge_messages

def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(speaker, i))
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)