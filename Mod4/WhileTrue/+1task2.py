seat_count=0
soft_seats=0
hard_seats=0
num_seats=4

# loops tallying seats using soft pads vs hard, until seats full or user "exits"

while True:
    seat_type=input('enter seat type of "hard", "soft" or "exit"(to finish): ')
    
    if seat_type.lower().startswith('e'):
        print()
        break
    elif seat_type.lower()=="hard":
        hard_seats +=1
    elif seat_type.lower()=="soft":
        soft_seats +=1
    else:
        print("invalid entry counted as hard")
        hard_seats+=1
    
    seat_count+=1    
    if seat_count>=num_seats:
        print("\nSeats are full")
        break
print(seat_count,"Seats total: ",hard_seats,"hard and ", soft_seats,"soft")