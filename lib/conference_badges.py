def badge_maker(name):
    # return None
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # return None
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    pass
    return [f"Hello, {name}! You'll be assigned to room {idx + 1}!" for idx, name in enumerate(names)]

def printer(names):
    # return None
    pass
    for badge in batch_badge_creator(names):
        pass
        print(badge)
        
    for room_assign in assign_rooms(names):
        pass
        print(room_assign)