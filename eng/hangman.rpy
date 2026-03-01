label start:
    m 1eua "I'll think of a word..."
    m "Alright, I've got one."
    $ char = "I"
    if hm_hint == "y":
        $ char = "Yuri"
    if hm_hint == "n":
        $ char = "Natsuki"
    if hm_hint == "s":
        $ char = "Sayori"
    if hm_hint == "m":
        $ char = "I"

    m "[char] like this word the most."
    return

label tip:
    $ char = "Мне"
    if hm_hint == "y":
        $ char = "Yuri"
    if hm_hint == "n":
        $ char = "Natsuki"
    if hm_hint == "s":
        $ char = "Sayori"
    if hm_hint == "m":
        $ char = "I"

    m "[char] like this word the most."
    return

label lose:
    m "And the correct word was... [word]."
    m 1hua "Better luck next time~"
    m "Would you like to play again?"
    menu:
        "Yes.":
            call_func hm_restart
        "No.":
            call_func hm_close
    return

label win:
    m 1hua "Wow, you guessed the word correctly!"
    m "Good job, [player]!"
    m "Would you like to play again?"
    menu:
        "Yes.":
            call_func hm_restart
        "No.":
            call_func hm_close
    return
    

label quit:
    if guesses == 0:
        m "I thought you said you wanted to play hangman."
        m 1lksdlc "But you didn't even guess a single letter."
        m "..."
        m 1ekc "I really like playing with you, you know."
    if guesses > 0:
        if chances == 5:
            m 1ekc "Don't give up so quickly."
            m 3eka "That was only your first wrong letter!"
            if chances > 1:
                m 1eka "You still had [chances] more lives left."
            if chances == 1:
                m 1eka "You still had [chances] more life left."
            m 1hua "I know you can do it!"
            m 1eka "It would really mean a lot to me if you just tried a bit harder."
        if chances <= 4:
            if chances != 0:
                m "You should at least play to the end..."
                m 1ekc "Giving up so easily is a sign of poor resolve."
                m "I mean, you'd have to miss [chances] more letters to actually lose."
            
    m "And the correct word was... [word]."
    random
    menu:
        "1":
            m 1eka "Can you play to the end next time, [player]? For me?"
        "2":
            m 1euc "Hangman is actually a pretty hard game.."
            m "You need to have a good vocabulary to be able to guess different words."
            m 1hua "The best way to improve that is to read more books!"
            m 1eua "I'd be very happy if you did that for me, [player]."
    return