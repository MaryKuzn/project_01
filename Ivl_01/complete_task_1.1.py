my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# 1 способ
print((my_favorite_songs[:14] +  
       my_favorite_songs[-14:] + 
       my_favorite_songs[15:22] + 
       my_favorite_songs[23:30] + 
       my_favorite_songs[50:62]))
# 2 способ
print(my_favorite_songs.split(sep=',')[0],
      my_favorite_songs.split(sep=',')[-1],
      my_favorite_songs.split(sep=',')[1],
      my_favorite_songs.split(sep=',')[-2])