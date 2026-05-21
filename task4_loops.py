for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(game[NAME], "-", game[GLOBAL_SALES], "million")
pre_2000_count = 0

for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count += 1

print("Games released before 2000:", pre_2000_count)
total_na_sales = 0
total_jp_sales = 0

for game in video_game_sales:
    total_na_sales += game[NA_SALES]
    total_jp_sales += game[JP_SALES]

print("Total North America sales:", total_na_sales)
print("Total Japan sales:", total_jp_sales)

if total_na_sales > total_jp_sales:
    print("North America had higher sales.")
else:
    print("Japan had higher sales.")

nintendo_games = []

for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games)
print("Number of Nintendo games:", len(nintendo_games))        
