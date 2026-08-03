room_map = {
    "main block": 1,
    "mechanical block": 2,
    "canteen": 3,
    "cse department": 4,
    "cse aiml department": 5,
    "is department": 6,
    "ai ml lab 1": 7,
    "ai ml lab 2": 8,
    "ai ml lab 3": 9,
    "2nd year classroom": 10,
    "3rd year classroom": 11,
    "4th year classroom": 12
}


def get_node(room):

    return room_map.get(room.strip().lower())


#if __name__ == "__main__":

 #   start = get_node("Entrance")
  #  end = get_node("AI Lab")

   # print("Start Node:", start)
    #print("End Node:", end)