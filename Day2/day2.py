with open("day2.txt") as file_object:
    data = file_object.read()
    splt = data.split("\n")
    splt.remove('')
    
    abc = []
    xyz = []
    draw_score = 0
    outcome_score = 0
    y = 0
    #x = ""
    for x in splt:
        abc.append(x[0])
        xyz.append(x[2])

    '''for i in range(0,2500):
        if xyz[i] == "X":
            draw_score += 1
        elif xyz[i] == "Y":
            draw_score += 2
        elif xyz[i] == "Z":
            draw_score += 3

        if xyz[i] == "X" and abc[i] == "A" or xyz[i] == "Y" and abc[i] == "B" or xyz[i] == "Z" and abc[i] == "C":
            outcome_score += 3
        if xyz[i] == "X" and abc[i] == "C" or xyz[i] == "Y" and abc[i] == "A" or xyz[i] == "Z" and abc[i] == "B":
            outcome_score += 6'''


    for i in range(0,2500):
        if abc[i] == "A":
            if xyz[i] == "X":
                outcome_score += 0
                draw_score += 3
            elif xyz[i] == "Y":
                outcome_score += 3
                draw_score += 1
            elif xyz[i] == "Z":
                outcome_score += 6
                draw_score += 2
        elif abc[i] == "B":
            if xyz[i] == "X":
                outcome_score += 0
                draw_score += 1
            elif xyz[i] == "Y":
                outcome_score += 3
                draw_score += 2
            elif xyz[i] == "Z":
                outcome_score += 6
                draw_score += 3
        elif abc[i] == "C":
            if xyz[i] == "X":
                outcome_score += 0
                draw_score += 2
            elif xyz[i] == "Y":
                outcome_score += 3
                draw_score += 3
            elif xyz[i] == "Z":
                outcome_score += 6
                draw_score += 1


        

        
total_score = draw_score + outcome_score
print(total_score)
