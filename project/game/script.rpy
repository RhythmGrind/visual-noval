# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kyle",color="#fff")
define d = Character("Daniella",color="#fff")
define j = Character("John",color="#fff")
define i = Character("Isabel",color="#fff")
define g = Character("George",color="#fff")

image picture_1 = im.Scale("kungfu.jpg",1920,1080)
image picture_2 = im.Scale("trooo.jpg",1920,1080)
image picture_3 = im.Scale("johnoffice.jpg",1920,1080)
image picture_4 = im.Scale("away1.jpg",1920,1080)
image picture_5 = im.Scale("away.jpg",1920,1080)
image picture_6 = im.Scale("inside.jpg",1920,1080)
image picture_7 = im.Scale("ozoz.jpg",1920,1080)
image picture_8 = im.Scale("night.jpg",1920,1080)

image d_mad = "Daniella/madred.png"
image k_sad = "Kyle/sad.png"
image j_j = "John/j.png"
image k_upset = "Kyle/upset.png"
image j_smile = "John/smile.png"
image j_natural = "John/natural.png"
image j_worried= "John/worried.png"
image j_suprised = "John/supreised.png"
image k_angry = "Kyle/angry.png"
image k_laugh = "Kyle/laugh.png"
image k_shy = "Kyle/shy.png"
image k_natural= "Kyle/natural.png"
image k_lilupset = "Kyle/little upset.png"







# The game starts here.

label start:
    show black
   
    centered "{color=#fff}this is a test"

    scene picture_1
 
    
    "1968 HOLLYWOOD"
    "Kung-Fu movies are at its peak. Legend Bruce Lee is changing the movie industry by being a representation for the Asian community. "
    "Upcoming actor, {b}Kyle Wang{/b}, is also making his mark."
    scene picture_2
    with dissolve
    hide picture_1

    "Having been nominated for an academy award the year prior, his new project {i}Time is Running Out{/i}, stars Kyle and his co-star, {b}Daniella Tako{/b}, who was making her name known overseas in Japan. "
    "Hollywood producers and managers hesitated for months to make this project, questioning how many Americans would see an action packed film starring two Asians with a supporting cast of other well known Hollywood actors."
    "As a solution, Kyle’s manager, John, and producers of {i}Time is Running Out{/i} decide to set Kyle up with the top bachelorette in Hollywood: {b}Isabel Adams{/b}. "
    scene picture_7
    with dissolve
    hide picture_2
    
    
    "Isabel is focused on her own project, a prequel to the popular film {i}The Wizard of Oz{/i}. By pairing these two actors together, America will be drawn into the newest, unexpected interracial couple. This is to build publicity for both {i}Time is Running Out{/i} and the untitled prequel for {i}The Wizard of Oz{/i}."
    
    show black
    centered "{size=+10}{color=#fff}At John’s Office in upper Los Angeles…"
    scene picture_3
    with dissolve
    hide picture_7

    show k_sad
    k "Isabel… Adams? Like, the actress who every man had in their helmet for a pinup over in Vietnam? "

    hide k_sad
    show j_j
    j "For the 100th time… YES. Look, I know you don’t want to be in a fake relationship but it’s to get people to go see you in the theater. The producers are already talking about firing Daniella for someone else. "

    hide j_j
    show k_upset
    k "*Visibly upset*"
    
    hide k_upset

    show j_smile
    j "It’s just for two years. We’ll have photographers catch you two coming from dinner and the world will know of Kyle and Isabel."
    j "If you won’t do it for yourself, do it for Daniella? Better yet, do it… for me?"
    hide j_smile


    menu:
        "Fine, I’ll do it. But only if you’ll be by my side the entire time.":
            call k1
        "No! I will not compromise my values for some silly charade!":
            call k2

    scene picture_4
    with dissolve
    hide picture_3

    "AT THE SAME TIME, 20 MILES AWAY"
    scene picture_6
    with dissolve
    hide picture_5
    i "I have to date WHO?"
    g "Kyle Wang. John’s actor. The one who was nominated for best actor last year."

    i "*Worried tone* You, you don’t think John told Kyle about us right?"

    g "Sweetie, no. No one knows about us except John. And he’s my brother - he would never tell others about us until we’re ready. "
    g "He just wanted to tell me so I could break the news to you first. Look, it’ll be good publicity for the prequel for {i}The Wizard of Oz{/i}. "
    i "Hey, I could get all of America to see MY film - without the help of any man."
    g "Yes, but that was before the paparazzi took photos of you conversing with that cult leader. What was his name? Manson? "
    i "FOR THE LAST TIME, he and his little group were blocking my way in the street! I had to tell them to get out of my way. "
    g "The pictures told a different story."

    menu:
        "Nonetheless, I guess I’ll “date” Kyle Wang for the time being.":
            call i1
        "Nonetheless, I am not “dating” Kyle Wang - it’s my film and mine to promote.":
            call i2
        
    i "Ok. I’ll go through with it. But it’s not for me - 'cause I could do it alone - it’s for a reason bigger than myself."
    g "Thank you"


    scene picture_5
    with dissolve
    hide picture_4

    "LATER THAT DAY AT KYLE’S HOUSE"
    

    k "Ok. Daniella, say it again but add more emotion. Ready? Go!"

    show d_mad
    d "You? You… KILLED MY FATHER!"

    d "*as a single tear streams down her face*"

    d "I trusted you and this… this is how you repay me? I should have listened to Papa when he was alive… men are to never be trusted."
    d "Prepare… prepare to meet your end!"
    k "That was better!"
    d "It’s dumb how we have to film the last scene before the first ones."
    k "Well it’s because…"
    d "I KNOW, I KNOW. It’s because of scheduling and when we can get the set and blah blah blah"
    k "Geez Dani, what's got you all riled up"

    d "(How do I tell him it's because he’s going to date THE Isabel Adams…)"

    d "Just stressed for the film to do well."

    d "(Good.. good reason, Dani)"

    d "As I was walking down the street today, a group of white people started pulling their eyes back and laughing at me. I am just so tired of people underestimating me - especially since I’m an actor."
    d "Do they not know how popular I am in Japan? Well, obviously not. BUT the sentiment would be appreciated. I just want to prove to everyone that I belong on the big screens in America; that I worked my ass off to get where I am. "
    
    d "(Which is all true, I want nothing more than to be accepted here…)"

    d "( I just can’t tell Kyle about my feelings toward Isabel, what would people think? I guess not ALL of me will be accepted…)"

    "*Daniella flops on the couch next to Kyle*"
    k "I get it… it's hard out here in LA. People already look at us funny and it’s not like we’ve had too much good representation on the big screen. But, we have to start somewhere"

    k "*Kyle nudges Daniella with his elbow* That’s where we come in. We could change history with this movie…"

    d "Yeah… history…"

    d "*says sarcastically* Hey Kyle, then remind me why the producers and your own manager are forcing you to date Isabel Adams for TWO YEARS?"

    k "WOAH I said we “COULD change history”... I didn’t say who would HELP us change history"
    d "Since the filming schedule “isn’t dumb”, it is dumb we need help promoting OUR movie. It’s ridiculous how we “need” some other person who we don’t even know."
    k "Dani… I hate to say it but let’s just be glad we’re even in this film."

    d "*hangs her head in sadness yet understanding*"

    k "For once, you AREN’T one-dimensional. You actually HAVE a story. Go ahead, tell me your characters story"
    d "I’m a ~gorgeous ~ spy for the Japanese government who is in America to avenge her fathers death."
    d "*Her tone gets more excited as she goes on…*"
    d "I am stronger than 10 American soldiers combined, all from my exceptional martial arts training I’ve received since I was born."
    d "At the same time, I’m struggling with coming to terms with who I am - will I continue to stay in America and conform to a new life in the states with the knowledge of my fathers killer living among me? Or go back to Japan where the people who control my life want me dead…"
    k "See! So much more than some Asian woman who is OVERLY sexualized"
    d "And you! You aren’t a “scary Asian man”. You’re a kind hearted soul who isn’t afraid to do whatever it takes to protect the ones he loves. "
    k "This movie could really change how people see us…"
    k "Two Asian leads in a Hollywood movie?? Come on now… it’s groundbreaking"

    k "(Being Asian American is already hard here in the film industry, how would people react if they knew WHO I was really in love with.. )"

    k "*Kyle’s big smile quickly turns into one of frustration*"
    d "Your turn… what’s got YOU all riled up?"

    menu:
        "I have a secret I need to tell you":
            call k3
        "Nervous, nervous for filming":
            call k4

    k "I think… I think I’m in love with someone"
    d "WHO??? "
    k "John"
    
    k "*he stares at Daniella to see her reaction*"

    d "John? YOUR MANAGER??"

    k "(Why is the first thing she thought about is that he’s my manager… not that he’s a… man?)"

    k "Yes, my manager"
    d "wow… so… you’re gay"
    k "Yes. Please, please don’t let this change how you see me. I’m still capable of doing my job, I’ll play a convincing partner for you on the big screen."
    d "So… the real reason I’m extremely bothered is because… you’re going to be “dating” Isabel Adams."
    k "Really? Why? Do YOU want to date her?"

    k "*Kyle lets out a loud laugh*"

    d "*purses her lips and furrows her brows as she does not break eye contact with Kyle*"

    k "HOLD ON…"
    k "I meant that as a joke but Dani… DO you want to date her?"
    d "I think I’m in love with the most beautiful girl in the world…"

    show black
    centered "{size=+10}{color=#fff}THE NEXT WEEK, DOWNTOWN LA"
    scene picture_8
    with dissolve
    hide picture_5

    
    k "One day, I’m getting my own star"
    j "I see it."




    return



label k1:
    j " By your side in a conundrum like this? Kyle, I will be there the whole time. And I… I will always love yo-y- your ambition in this industry! It’ll be quick, two years will fly by. I promise. "
    k "AH! Thanks! Um, you’re the, uh,  best manager. Truly, Thank you. Thank you."

    j "*Voice starts to get nervous*"

    j "Yeah! Uh, of course. You pay me to do my job haha…ha. Okay! Well, I’ll catch you on the flip side"

    j " *awkward finger guns to Kyle*"
    return
label k2:
    j "Kyle, you do not have a choice in this situation. I’m sorry but as your manager, you have to do this. It’ll be the best path for OUR success. "
    k "God, if it weren’t for how well you do your job… I don’t know if you’d still be my manager. "
    j "Alright. Well, I have to go to a meeting. We’ll speak more on this later. I have to tell the producers we’re all on the same page. "
    return

label i1:
    g "Ok, I’ll tell John you’re good to go. It’ll be fuuuun!"

label i2:
    g "Isa, I understand. But Kyle’s already agreed and it’s for the both of you. Think of it this way - it’s for the minority community. They’re just as American as we are, but so much is happening in the world right now we need to push for more."

label k3:
    d "Tell me, please. And I’ll tell you one as well"
    k "You have a secret too? It’s probably not as bad as mine. But alright… here I go…"

label k4:
    d "You have a secret too? It’s probably not as bad as mine. But alright… here I go…"
    k "How do you know me so well? Fine… this is what’s really bothering me"
