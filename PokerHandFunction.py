








def find_poker_hand(hand):
    ranks=[]
    suits=[]
    possible_ranks=[]
    for card in hand:
        if len(card)==2:
            rank=card[0]
            suit=card[1]
        else:
            rank=card[0:2]
            suit=card[2]
        if rank=="A":rank=14
        if rank=="K":rank=13
        if rank=="Q":rank=12
        if rank=="J":rank=11


        ranks.append(int(rank))
        suits.append(suit)
    #print(ranks)
    sorted_ranks=sorted(ranks)
    #print(sorted_ranks)


    # ROYAL FLUSH AND STRAIGHT FLUSH AND FLUSH
    if suits.count(suits[0])==5:#Check for Flush
        if 14 in sorted_ranks and 13 in sorted_ranks and 12 in sorted_ranks and 11 in sorted_ranks and 10 in sorted_ranks:#Royal Flush
            possible_ranks.append(10)
        elif sorted_ranks[0]+1==sorted_ranks[1] and sorted_ranks[1]+1==sorted_ranks[2] and sorted_ranks[2]+1==sorted_ranks[3] and sorted_ranks[3]+1==sorted_ranks[4] :#Straight Flush
            possible_ranks.append(9)
        else:
            possible_ranks.append(6)#Flush
    #Straight
    if sorted_ranks[0]+1==sorted_ranks[1] and sorted_ranks[1]+1==sorted_ranks[2] and sorted_ranks[2]+1==sorted_ranks[3] and sorted_ranks[3]+1==sorted_ranks[4] :
        possible_ranks.append(5)

    hand_unique_values = list(set(sorted_ranks))
    #Four of a kind
    if len(hand_unique_values)==2:
        for val in hand_unique_values:
            if sorted_ranks.count(val)==4:
                possible_ranks.append(8)
            if sorted_ranks.count(val)==3:
                possible_ranks.append(7)

    #
    if len(hand_unique_values)==3:
        for val in hand_unique_values:
            if sorted_ranks.count(val)==3:#Three of a Kind
                possible_ranks.append(4)
            if sorted_ranks.count(val)==2:#Two Pair
                possible_ranks.append(3)
    #Pair
    if len(hand_unique_values) == 4:
        possible_ranks.append(2)

    #High Card
    if not possible_ranks:
        possible_ranks.append(1 )




    poker_hand_ranks={
        10:"Royal Flush",
        9:"Straight Flush",
        8:"Four of a Kind",
        7:"Full House",
        6:"Flush",
        5:"Straight",
        4:"Three of a Kind",
        3:"Two Pair",
        2:"Pair",
        1:"High Card",
    }
    output=poker_hand_ranks.get(max(possible_ranks))
    print(hand,output)
    return output

if __name__ == '__main__':
    find_poker_hand(["AH","KH","QH","JH","10H"])#royal flush
    find_poker_hand(["QC","JC","10C","9C","8C"])#straight flush
    find_poker_hand(["5C","5S","5H","5D","QH"])# Four of a kind
    find_poker_hand(["2H","2D","2S","10H","10C"])# Full House
    find_poker_hand(["2D","KD","7D","6D","5D"])# Flush
    find_poker_hand(["JC","10H","9C","8C","7D"])# Straight
    find_poker_hand(["10H","10C","10D","2D","5S"])# Three of a Kind
    find_poker_hand(["KD","KH","5C","5S","6D"])# Two Pair
    find_poker_hand(["2D","2S","9C","KD","10C"])# Pair
    find_poker_hand(["KD","5H","2D","10C","JH"])# High Card
