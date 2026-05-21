messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

game_name = video_game_sales[4][NAME]

pokemon_word = game_name[:7]

print(pokemon_word)
messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

for name in messy_names:
    cleaned_name = name.strip().lower()
    print(cleaned_name)
top_game = video_game_sales[0]

print(f"#1 Best Seller: {top_game[NAME]} ({top_game[YEAR]}) - ${top_game[GLOBAL_SALES]}M global sales")   
