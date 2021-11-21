import random
import math
import matplotlib.pyplot as plt

n = 4  # number of players
num_game = 20000;
current_game = 0;
s1 = 0;
s2 = 0;
game_count = []
s1_winrates = []
s2_winrates = []
hist1 = []
hist2 = []
'''
index from 0 to 12 is Spade
index from 13 to 25 is Heart
index from 26 to 38 is Diamond
index from 39 to 51 is Club
card[n] % 4 + 1 gives me the number on the card
int(card[n] / 4) gives me the suits of the card (0 is Spade, 1 is Heart, 2 is Diamond, 3 is Club)
each index has number 1 to 4 represent which player own this card
after playing a card, the corresponding number in that index becomes 0
after drop a card, the corresponding number in that index times -1
'''
card = [0] * 52  # store rules above
deal_card = [0] * 52  # number from 0 to 51 of which card is not deal
turn = 1;  # in which player's turn

'''deal'''


def deal():
    global deal_card, card
    card = [0] * 52  # renew the value if playing more times
    deal_card = [0] * 52  # renew the value if playing more times
    for i in range(0, 52):
        deal_card[i] = i
    for player in range(1, 5):
        for count in range(0, 13):
            length = len(deal_card) - 1
            rand = random.randint(0, length)
            card[deal_card[rand]] = player
            deal_card.pop(rand)


'''play one game'''


def playgame():
    global turn, card, game_count, current_game
    current_game = current_game + 1
    game_count.append(current_game)
    deal()
    turn = card[6]  # Spade 7
    # print("Player", turn, "plays", "Spade 7")
    card[6] = 0
    switch_turn()
    for round in range(0, 51):
        if turn == 1:
            play = strategy3()  # play from 1 to 52, is ith card
        else:
            play = strategy2()
        if play > 0:
            card[play - 1] = 0
            # print("Player", turn, "plays", formalize(play - 1))
        elif play < 0:
            card[-1 * play - 1] = -1 * card[-1 * play - 1]
            # print("Player", turn, "drops", formalize(-1 * play - 1))
        switch_turn()
    count_Score()


'''switch player'''


def switch_turn():
    global turn
    if turn == 4:
        turn = 1;
    else:
        turn = turn + 1


'''a complicated strategy'''


def strategy1():
    attempt_drop = 0
    for i in range(0, 52):
        if card[i] == turn:
            attempt_drop = -1 * (i + 1)
            break

    play, drop = search_play(0, 6, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(13, 19, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(26, 32, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(39, 45, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(6, 13, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(19, 26, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(32, 39, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop
    play, drop = search_play(45, 52, True)
    if play != 0: return play
    if drop != 0 and (-1 * attempt_drop - 1) % 13 >= (-1 * drop - 1) % 13: attempt_drop = drop

    if play != 0:
        return play
    else:
        return attempt_drop


'''a simple strategy'''


def strategy2():
    play, drop = search_play(0, 52, False)
    if play != 0:
        return play
    else:
        for i in range(0, 52):
            if card[i] == turn:
                return -1 * (i + 1)


def strategy3():
    playlist = []
    for i in range(0, 52):
        if card[i] == 0:
            if i % 13 != 0:
                if i % 13 < 7:
                    if card[i - 1] == turn:
                        playlist.append(i)
                if 5 < i % 13 < 12:
                    if card[i + 1] == turn:
                        playlist.append(i + 2)
    if playlist:
        return playlist[random.randint(0, len(playlist) - 1)]
    else:
        droplist = []
        for i in range(0, 52):
            if card[i] == turn:
                droplist.append(i + 1)
        return -1 * droplist[random.randint(0, len(droplist) - 1)]


def search_play(range1, range2, if_drop):
    play = 0;
    drop = 0;
    for i in range(range1, range2):
        if card[i] == 0:
            if i % 13 != 0:
                if i % 13 < 7:
                    if card[i - 1] == turn:
                        play = i
                        break
                if 5 < i % 13 < 12:
                    if card[i + 1] == turn:
                        play = i + 2
                        break
        if if_drop:
            if card[i] == turn and i % 13 <= (-1 * drop - 1) % 13:
                drop = -1 * (i + 1)
    if play == 0:
        if card[19] == turn:
            play = 20
        elif card[32] == turn:
            play = 33
        elif card[45] == turn:
            play = 46
    return play, drop


'''formalize the print statement'''


def formalize(play):
    num = play % 13
    suits = int(play / 13)
    if suits == 0:
        output = "Spade "
    elif suits == 1:
        output = "Heart "
    elif suits == 2:
        output = "Diamond "
    else:
        output = "Club "
    if 0 < num < 10:
        output = output + str(num + 1)
    elif num == 0:
        output = output + "A"
    elif num == 10:
        output = output + "J"
    elif num == 11:
        output = output + "Q"
    elif num == 12:
        output = output + "K"
    return output


def count_Score():
    global s1_winrates, s2_winrates, s1, s2
    player = [0, 0, 0, 0]
    for i in range(0, 52):
        if card[i] == -1:
            player[0] = player[0] + i % 13 + 1
        elif card[i] == -2:
            player[1] = player[1] + i % 13 + 1
        elif card[i] == -3:
            player[2] = player[2] + i % 13 + 1
        elif card[i] == -4:
            player[3] = player[3] + i % 13 + 1
    # print("player 1 scores:", str(player[0]))
    # print("player 2 scores:", str(player[1]))
    # print("player 3 scores:", str(player[2]))
    # print("player 4 scores:", str(player[3]))
    minScore = min(player)
    player1 = -1
    player2 = -1
    player3 = -1
    player4 = -1
    if player.count(minScore) == 1:
        player1 = player.index(minScore) + 1
        '''print("The winner is: player", str(player1))'''
    elif player.count(minScore) == 2:
        player1 = player.index(min(player)) + 1
        player2 = player[player1:].index(min(player)) + 1 + player1
        '''print("The winner is: player", str(player1), "and", str(player2) )'''
    elif player.count(minScore) == 3:
        list = [1, 2, 3, 4]
        for i in range(0, 4):
            if player[i] != minScore:
                list.pop(i)
                break
        player1 = list[0]
        player2 = list[1]
        player3 = list[2]
        output = "The winner is: player "
        output = output + str(player1) + ", "
        output = output + str(player2) + ",and "
        output = output + str(player3)
        '''print(output)'''
    else:
        player1 = 1
        player2 = 2
        player3 = 3
        player4 = 4
        '''print("The winner is: player", "1,", "2,", "3,and 4")'''
    if 0 < player1 < 2:
        s1 = s1 + 1
    if 1 < player1 < 5:
        s2 = s2 + 1
    if 0 < player2 < 2:
        s1 = s1 + 1
    if 1 < player2 < 5:
        s2 = s2 + 1
    if player3 > 0:
        s2 = s2 + 1
    if player4 > 0:
        s2 = s2 + 1
    s1_winrates.append(s1 / current_game)
    s2_winrates.append(s2 / current_game)


for i in range(0, 10):
    print(i)
    s1_winrates = []
    s2_winrates = []
    s1 = 0
    s2 = 0
    current_game = 0
    game_count = []
    for j in range(0, num_game):
        '''print("Game:", str(i))'''
        playgame()
    hist1.append(s1_winrates[num_game - 1])
    hist2.append(s2_winrates[num_game - 1])
print(hist1)
print(hist2)
print(min(hist1))
print(max(hist1))
print(min(hist2))
print(max(hist2))
'''
plt.hist(hist1, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
plt.xlabel("win rates")
# 显示纵轴标签
plt.ylabel("frequency")
# 显示图标题
plt.title("Strategy A")
plt.show()

plt.hist(hist2, bins=40, facecolor="red", edgecolor="black", alpha=0.7)
plt.xlabel("win rates")
# 显示纵轴标签
plt.ylabel("frequency")
# 显示图标题
plt.title("Strategy B")
plt.show()
'''
'''
plt.plot(game_count, s1_winrates, color="r", linestyle="--", marker="*", linewidth=1.0, label='StrategyB')
plt.plot(game_count, s2_winrates, color="b", linestyle="-", marker="*", linewidth=1.0, label='StrategyC')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.xlabel('games count')
plt.ylabel('win rates')
plt.show()
'''
