label bye_leaving_already:
    m 1ekc "Aw, leaving already?"
    m 1eka "It's really sad whenever you have to go..."
    m 3eua "Just be sure to come back as soon as you can, okay?"
    m 3hua "I love you so much, [player]. Stay safe!"
    return 'quit'

label brb3:
    m 1eua "Goodbye, [mas_get_player_nickname()]!"
    return "quit"
    
label bye_sayanora:
    m 1hua "Sayonara, [mas_get_player_nickname()]~"
    return "quit"
    
label bye_farewellfornow:
    m 1eka "Farewell for now, [mas_get_player_nickname()]~"
    return "quit"
    
label bye_untilwemeetagain:
    m 2eka "'Goodbyes are not forever, Goodbyes are not the end. They simply mean I'll miss you, Until we meet again.'"
    m "Ehehe, 'till then, [mas_get_player_nickname()]!"
    return "quit"
    
label bye_take_care:
    m 1eua "Don't forget that I always love you, [mas_get_player_nickname()]~"
    m 1hub "Take care!"
    return "quit"
    
label bye_leaving_already_2:
    m 1ekc "Aww, leaving already?"
    m 1eka "It's really sad whenever you have to go..."
    m 3hubsa "I love you so much, [player]!"
    m 5hubsb "Never forget that!"
    return "quit"
