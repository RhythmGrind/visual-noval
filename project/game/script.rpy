# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kyle")
define d = Character("Daniella")
define j = Character("John")
define i = Character("Isabel")
image picture_1 = im.Scale("bg1.jpg",1920,1080)


# The game starts here.

label start:
    show black
   
    centered "this is a test"

    scene picture_1

    
    "1968 HOLLYWOOD"

    "Kung-Fu movies are at its peak. Legend Bruce Lee is changing the movie industry by being a representation for the Asian community. "
    
    "Upcoming actor, {b}Kyle Wang{/b}, is also making his mark."

    "Having been nominated for an academy award the year prior, his new project {i}Time is Running Out{/i}, stars Kyle and his co-star, {b}Daniella Tako{/b}, who was making her name known overseas in Japan. "

    "Hollywood producers and managers hesitated for months to make this project, questioning how many Americans would see an action packed film starring two Asians with a supporting cast of other well known Hollywood actors."

    "As a solution, Kyle’s manager, John, and producers of {i}Time is Running Out{/i} decide to set Kyle up with the top bachelorette in Hollywood: {b}Isabel Adams{/b}. "

    "Isabel is focused on her own project, a prequel to the popular film {i}The Wizard of Oz{/i}. By pairing these two actors together, America will be drawn into the newest, unexpected interracial couple. This is to build publicity for both {i}Time is Running Out{/i} and the untitled prequel for {i}The Wizard of Oz{/i}."

    k "Isabel… Adams? Like, the actress who every man had in their helmet for a pinup over in Vietnam? "

    j "For the 100th time… YES. Look, I know you don’t want to be in a fake relationship but it’s to get people to go see you in the theater. The producers are already talking about firing Daniella for someone else. "

    j "It’s just for two years. We’ll have photographers catch you two coming from dinner and the world will know of Kyle and Isabel. If you won’t do it for yourself, do it for Daniella? Better yet, do it… for me?"

    menu:
        "Fine, I’ll do it. But only if you’ll be by my side the entire time.":
            call k1
        "No! I will not compromise my values for some silly charade!":
            call k2

    "AT THE SAME TIME, 20 MILES AWAY"
    return

label k1:
    j " By your side in a conundrum like this? Kyle, I will be there the whole time. And I… I will always love yo-y- your ambition in this industry! It’ll be quick, two years will fly by. I promise. "

    k "AH! Thanks! Um, you’re the, uh,  best manager. Truly, Thank you. Thank you."

    j "Yeah! Uh, of course. You pay me to do my job haha…ha. Okay! Well, I’ll catch you on the flip side"

    return
label k2:
    j "Kyle, you do not have a choice in this situation. I’m sorry but as your manager, you have to do this. It’ll be the best path for OUR success. "

    k "God, if it weren’t for how well you do your job… I don’t know if you’d still be my manager. "

    j "Alright. Well, I have to go to a meeting. We’ll speak more on this later. I have to tell the producers we’re all on the same page. "
    return