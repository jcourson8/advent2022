total_score_first_method = 0
total_score_second_method = 0
outcomes = {
    "draw":[0],
    "lose":[-2,1],
    "win":[-1,2]
}

"""
ROCK PAPER SCISSOR
A    B     C

A - A = 0  (A draw)
A - B = -1 (A lose)
A - C = -2 (A wins)

B - A = 1  (B wins)
B - B = 0  (B draw
B - C = -1 (B lose)

C - A = 2  (C lose)
C - B = 1  (C wins)
C - C = 0  (C ties)

"""

with open('input.txt','r') as file:
    
    while True:
        line = file.readline()
        if not line:
            break       
        
        round_score = 0
        opponent_hand = ord(line[0]) - 65 # Zeroing A
        hand = ord(line[2]) - 23 - 65 # Zeroing X

        if (opponent_hand - hand) in outcomes['draw']:
            print(f'{line[0:3]}: draw')
            round_score = hand + 1 + 3

        elif (opponent_hand - hand) in outcomes['win']:
            print(f'{line[0:3]}: win')
            round_score = hand + 1 + 6

        elif (opponent_hand - hand) in outcomes['lose']:
            print(f'{line[0:3]}: lose')
            round_score = hand + 1

        
        else:
            raise "this should not happen"
        
        ### PART 2 Code ###

        outcome = hand
        round_score_second_method = 0

        if outcome == 0: #lose
            for i in outcomes['win']: 
                hand_needed = opponent_hand + i
                if hand_needed in range(0,3):
                    round_score_second_method = hand_needed 

        elif outcome == 1: #draw
            round_score_second_method = opponent_hand + 3

        elif outcome == 2: #win
            for i in outcomes['lose']: 
                hand_needed = opponent_hand + i
                if hand_needed in range(0,3):
                    round_score_second_method = hand_needed + 6 
        else:
            raise "this should not happen"


        ###################
        total_score_second_method = total_score_second_method + round_score_second_method
        total_score_first_method = total_score_first_method + round_score

print(f'Total Score: {total_score_first_method}')
print(f'Total Score: {total_score_second_method}')


 
