room_map = {
    "entrance":1,
    "reception":2,
    "block a junction":3,
    "lift":4,
    "canteen":5,
    "ai lab":6
}


def get_node(room):

    return room_map.get(room.strip().lower())


if __name__ == "__main__":

    start = get_node("Entrance")
    end = get_node("AI Lab")

    print("Start Node:", start)
    print("End Node:", end)