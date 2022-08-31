# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/B5.ogg",channel="sound",loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define k = Character("Kyle",color="#fff",callback=type_sound)
define d = Character("Daniella",color="#fff",callback=type_sound)
define j = Character("John",color="#fff",callback=type_sound)
define i = Character("Isabel",color="#fff",callback=type_sound)
define g = Character("George",color="#fff",callback=type_sound)

image picture_1 = im.Scale("kungfu2.jpg",1920,1080)

image picture_2 = im.Scale("trooo.jpg",1920,1080)
image picture_3 = im.Scale("johnoffice.jpg",1920,1080)
image picture_4 = im.Scale("away1.jpg",1920,1080)
image picture_5 = im.Scale("away.jpg",1920,1080)
image picture_6 = im.Scale("inside.jpg",1920,1080)
image picture_7 = im.Scale("ozoz.jpg",1920,1080)
image picture_8 = im.Scale("night.jpg",1920,1080)
image picture_10 = im.Scale("road.jpg",1920,1080)
image pra = im.Scale("pra.jpg",1920,1080)
image hallway = im.Scale("hallway.png",1920,1080)

image picture_9:
   "star2.png"
   yalign 3
   xalign 0.83

image mic:
    "mic.png"
    yalign 0.83
    xalign 0.42

image d_mad = im.Scale("Daniella/madred.png",900,1080)
image d_cry = im.Scale("Daniella/cry.png",900,1080)
image d_normal = im.Scale("Daniella/normal.png",900,1080)
image d_red = im.Scale("Daniella/red.png",900,1080)
image d_nomood = im.Scale("Daniella/nomood.png",900,1080)
image d_laugh = im.Scale("Daniella/laugh.png",900,1080)
image d_dontcare = im.Scale("Daniella/dontcare.png",900,1080)
image d_smile = im.Scale("Daniella/smile.png",900,1080)
image d_lilsup = im.Scale("Daniella/lilsup.png",900,1080)
image d_sup = im.Scale("Daniella/sup.png",900,1080)

image k_sup =im.Scale("Kyle/sup.png",900,1080)

image k_n = im.Scale("Kyle/n.png",900,1080)
image k_angry = im.Scale("Kyle/angry.png",900,1080)

image k_laugh = im.Scale("Kyle/laugh.png",900,1080)

image k_shy = im.Scale("Kyle/shy.png",900,1080)
image k_natural= im.Scale("Kyle/natural.png",900,1080)
image k_lilupset = im.Scale("Kyle/little upset.png",900,1080)
image k_grouch = im.Scale("Kyle/grouch.png",900,1080)
image k_upset = im.Scale("Kyle/upset.png",900,1080)
image k_sad = im.Scale("Kyle/sad.png",900,1080)
image k_happy = im.Scale("Kyle/happy.png",900,1080)
image k_u = im.Scale("Kyle/u.png",900,1080)
image k_say = im.Scale("Kyle/say.png",900,1080)

image j_normal = im.Scale("John/normal.png",900,1080)
image j_awkward = im.Scale("John/awkward.png",900,1080)
image j_j = im.Scale("John/j.png",900,1080)
image j_smile = im.Scale("John/smile.png",900,1080)
image j_natural = im.Scale("John/natural.png",900,1080)
image j_worried= im.Scale("John/worried.png",900,1080)
image j_suprised = im.Scale("John/surprised.png",900,1080)
image j_q = im.Scale("John/q.png",900,1080)
image j_relieved = im.Scale("John/relieved.png",900,1080)
image j_annoyed = im.Scale("John/annoyed.png",900,1080)
image j_sad = im.Scale("John/sad.png",900,1080)

image i_worried = im.Scale("Isabel/worried.png",900,1080)
image i_nothing = im.Scale("Isabel/nothing.png",900,1080)
image i_angry = im.Scale("Isabel/angry.png",900,1080)
image i_ren = im.Scale("Isabel/ren.png",900,1080)
image i_sup = im.Scale("Isabel/surprised.png",900,1080)
image i_natural = im.Scale("Isabel/natural.png",900,1080)
image i_smile = im.Scale("Isabel/smile.png",900,1080)

image g_nothing = im.Scale("George/nothing.png",900,1080)
image g_natural= im.Scale("George/natural.png",900,1080)
image g_cu = im.Scale("George/cu.png",900,1080)
image g_angry = im.Scale("George/angry.png",900,1080)
image g_smile = im.Scale("George/smile.png",900,1080)

image g_sup = im.Scale("George/surprised.png",900,1080)

# The game starts here.

label start:
    show black
   
    centered "{color=#fff}1968 HOLLYWOOD"
    play music "audio/mus.mp3" volume 0.3 fadein 1.0
    scene picture_1
 
    "Kung-Fu movies are at its peak. Legend Bruce Lee is changing the movie industry by being a representation for the Asian community. "
    show k_happy
    with dissolve
    "Upcoming actor, {color=#E0B0FF}{i}{b}Kyle Wang{/b}{/i}{/color=#E0B0FF}, is also making his mark."
    hide k_happy
    scene picture_2
    with dissolve
    hide picture_1
    
    show d_laugh
    with dissolve
    "Having been nominated for an academy award the year prior, his new project {i}Time is Running Out{/i}, stars Kyle and his co-star, {color=#E0B0FF}{i}{b}Daniella Tako{/b}{/i}{/color=#E0B0FF}, who was making her name known overseas in Japan. "
    hide d_laugh
    "Hollywood producers and managers hesitated for months to make this project, questioning how many Americans would see an action packed film starring two Asians with a supporting cast of other well known Hollywood actors."
    
    show j_smile at left
    with moveinleft
    show i_natural at right
    with moveinright
    "As a solution, Kyle’s manager, {color=#E0B0FF}{i}{b}John{/color=#E0B0FF}{/i}{/b}, and producers of {i}Time is Running Out{/i} decide to set Kyle up with the top bachelorette in Hollywood: {color=#E0B0FF}{i}{b}Isabel Adams{/color=#E0B0FF}{/i}{/b}. "
    hide j_smile
    with moveoutleft
    hide i_natural
    with moveoutright

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
    k "{color=#D2B9D3}{i}*Visibly upset*"
    
    hide k_upset
    show j_smile
    j "It’s just for two years. We’ll have photographers catch you two coming from dinner and the world will know of Kyle and Isabel."
    j "If you won’t do it for yourself, do it for Daniella? Better yet, do it… for me?"
    hide j_smile


    menu:
        "{color=#2E8B57}Fine, I’ll do it. But only if you’ll be by my side the entire time.":
            call k1
        "{color=#2E8B57}No! I will not compromise my values for some silly charade!":
            call k2

    scene picture_4
    with dissolve
    hide picture_3

    "AT THE SAME TIME, 20 MILES AWAY"

    show picture_6
    with zoomin
    hide picture_4

    pause 1.0
    show i_worried
    with hpunch
    i "I have to date WHO?"
    hide i_worried
    show g_natural
    g "Kyle Wang. John’s actor. The one who was nominated for best actor last year."
    hide g_natural
    show i_worried
    i "{color=#D2B9D3}{i}*Worried tone*{/color=#D2B9D3}{/i} You, you don’t think John told Kyle about us right?"
    hide i_worried
    show g_natural
    g "Sweetie, no. No one knows about us except John. And he’s my brother - he would never tell others about us until we’re ready. "
    g "He just wanted to tell me so I could break the news to you first. Look, it’ll be good publicity for the prequel for {i}The Wizard of Oz{/i}. "
    hide g_natural
    show i_nothing
    i "Hey, I could get all of America to see MY film - without the help of any man."
    hide i_nothing
    show g_cu
    g "Yes, but that was before the paparazzi took photos of you conversing with that cult leader. What was his name? Manson? "
    hide g_cu
    show i_angry
    with hpunch
    i "FOR THE LAST TIME, he and his little group were blocking my way in the street! I had to tell them to get out of my way. "
    hide i_angry
    show g_cu
    g "The pictures told a different story."
    hide g_cu

    menu:
        "{color=#2E8B57}Nonetheless, I guess I’ll “date” Kyle Wang for the time being.":
            call i1
        "{color=#2E8B57}Nonetheless, I am not “dating” Kyle Wang - it’s my film and mine to promote.":
            call i2
    

    show i_nothing
    i "Ok. I’ll go through with it. But it’s not for me - 'cause I could do it alone - it’s for a reason bigger than myself."
    hide i_nothing
    show g_nothing
    g "Thank you"
    hide g_nothing


    show black
    centered "{size=+10}{color=#fff}LATER THAT DAY AT KYLE’S HOUSE"
    scene picture_5
    with dissolve
    hide picture_4

    pause 1.0
    show k_natural
    k "Ok. Daniella, say it again but add more emotion. Ready? Go!"
    hide k_natural
    show d_mad
    with hpunch
    d "You? You… KILLED MY FATHER!"
    hide d_mad
    show d_cry
    d "{color=#D2B9D3}{i}*as a single tear streams down her face*"
    d "I trusted you and this… this is how you repay me? I should have listened to Papa when he was alive… men are to never be trusted."
    d "Prepare… prepare to meet your end!"
    hide d_cry
    show k_natural
    k "That was better!"
    hide k_natural
    show d_normal
    d "It’s dumb how we have to film the last scene before the first ones."
    hide d_normal
    show k_n
    k "Well it’s because…"
    hide k_n
    show d_mad
    d "I KNOW, I KNOW. It’s because of scheduling and when we can get the set and blah blah blah"
    hide d_mad
    show k_sup
    k "Geez Dani, what's got you all riled up"
    hide k_sup
    show d_red
    d "{color=#D2B9D3}{i}(How do I tell him it's because he’s going to date THE Isabel Adams…)"
    hide d_red
    show d_nomood
    d "Just stressed for the film to do well."
    hide d_nomood
    show d_laugh
    d "{color=#D2B9D3}{i}(Good.. good reason, Dani)"
    hide d_laugh
    show d_mad
    d "As I was walking down the street today, a group of white people started pulling their eyes back and laughing at me. I am just so tired of people underestimating me - especially since I’m an actor."
    d "Do they not know how popular I am in Japan? Well, obviously not. BUT the sentiment would be appreciated. I just want to prove to everyone that I belong on the big screens in America; that I worked my ass off to get where I am. "
    hide d_mad
    show d_dontcare
    d "{color=#D2B9D3}{i}(Which is all true, I want nothing more than to be accepted here…)"
    hide d_dontcare
    show d_red
    d "{color=#D2B9D3}{i}(I just can’t tell Kyle about my feelings toward Isabel, what would people think? I guess not ALL of me will be accepted…)"
    hide d_red
    "{color=#D2B9D3}{i}*Daniella flops on the couch next to Kyle*"
    show k_happy
    k "I get it… it's hard out here in LA. People already look at us funny and it’s not like we’ve had too much good representation on the big screen. But, we have to start somewhere"
    k "{color=#D2B9D3}{i}*Kyle nudges Daniella with his elbow*{/color=#D2B9D3}{/i} That’s where we come in. We could change history with this movie…"
    hide k_happy
    show d_normal
    d "Yeah… history…"
    hide d_normal
    show d_smile
    d "{color=#D2B9D3}{i}*says sarcastically*{/color=#D2B9D3}{/i} Hey Kyle, then remind me why the producers and your own manager are forcing you to date Isabel Adams for TWO YEARS?"
    hide d_smile
    show k_n
    k "WOAH I said we “COULD change history”... I didn’t say who would HELP us change history"
    hide k_n
    show d_normal
    d "Since the filming schedule “isn’t dumb”, it is dumb we need help promoting OUR movie. It’s ridiculous how we “need” some other person who we don’t even know."
    hide d_normal
    show k_n
    k "Dani… I hate to say it but let’s just be glad we’re even in this film."
    hide k_n
    show d_dontcare
    d "{color=#D2B9D3}{i}*hangs her head in sadness yet understanding*"
    hide d_dontcare

    show k_happy
    k "For once, you AREN’T one-dimensional. You actually HAVE a story. Go ahead, tell me your characters story"
    hide k_happy
    show d_smile
    d "I’m a ~gorgeous ~ spy for the Japanese government who is in America to avenge her fathers death."
    "{color=#D2B9D3}{i}*Her tone gets more excited as she goes on…*"
    hide d_smile
    show d_laugh
    d "I am stronger than 10 American soldiers combined, all from my exceptional martial arts training I’ve received since I was born."
    d "At the same time, I’m struggling with coming to terms with who I am - will I continue to stay in America and conform to a new life in the states with the knowledge of my fathers killer living among me? Or go back to Japan where the people who control my life want me dead…"
    hide d_laugh
    show k_happy
    k "See! So much more than some Asian woman who is OVERLY sexualized"
    hide k_happy
    show d_smile
    d "And you! You aren’t a “scary Asian man”. You’re a kind hearted soul who isn’t afraid to do whatever it takes to protect the ones he loves. "
    hide d_smile
    show k_happy
    k "This movie could really change how people see us…"
    k "Two Asian leads in a Hollywood movie?? Come on now… it’s groundbreaking"
    hide k_happy
    show k_upset
    k "{color=#D2B9D3}{i}(Being Asian American is already hard here in the film industry, how would people react if they knew WHO I was really in love with.. )"
    k "{color=#D2B9D3}{i}*Kyle’s big smile quickly turns into one of frustration*"
    hide k_upset
    show d_smile
    d "Your turn… what’s got YOU all riled up?"
    hide d_smile

    menu:
        "{color=#2E8B57}I have a secret I need to tell you":
            call k3
        "{color=#2E8B57}Nervous, nervous for filming":
            call k4


    show k_u
    k "I think… I think I’m in love with someone"
    hide k_u
    show d_lilsup
    d "WHO??? "
    hide d_lilsup
    show k_u
    k "John"
    "{color=#D2B9D3}{i}*he stares at Daniella to see her reaction*"
    hide k_u

    show d_sup
    with hpunch
    d "John? YOUR MANAGER??"
    hide d_sup
    show k_u
    k "{color=#D2B9D3}{i}(Why is the first thing she thought about is that he’s my manager… not that he’s a… man?)"
    k "Yes, my manager"
    hide k_u
    show d_sup
    d "wow… so… you’re gay"
    hide d_sup
    show k_upset
    k "Yes. Please, please don’t let this change how you see me. I’m still capable of doing my job, I’ll play a convincing partner for you on the big screen."
    hide k_upset
    show d_normal
    d "So… the real reason I’m extremely bothered is because… you’re going to be “dating” Isabel Adams."
    hide d_normal
    show k_laugh
    k "Really? Why? Do YOU want to date her?"
    k "{color=#D2B9D3}{i}*Kyle lets out a loud laugh*"
    hide k_laugh
    show d_red
    d "{color=#D2B9D3}{i}*purses her lips and furrows her brows as she does not break eye contact with Kyle*"
    hide d_red
    show k_sup
    with hpunch
    k "HOLD ON…"
    hide k_sup
    show k_happy
    k "I meant that as a joke but Dani… DO you want to date her?"
    hide k_happy
    show d_red
    d "I think I’m in love with the most beautiful girl in the world…"
    hide d_red

    show black
    centered "{size=+10}{color=#fff}THE NEXT WEEK, DOWNTOWN LA"
    scene picture_10
    with dissolve
    hide picture_5

    pause 1.0
    show k_angry
    with None
    show picture_9
    with dissolve
    k "One day, I’m getting my own star"
    hide k_angry
    hide picture_9
    show j_smile
    j "I see it."
    j "KYLE WANG. With a little film camera under your name."
    hide j_smile
    show k_lilupset
    k "{color=#D2B9D3}{i}*looks at John*{/color=#D2B9D3}{/i} MY name… among the stars"
    k "{color=#D2B9D3}{i}(But you’re the only star I want in my life… god that was way too cheesy)"
    k "Yeah, but I can only get there with YOUR help"
    hide k_lilupset
    show j_worried
    j "Listen, you could make it so far.. even without me."
    j "{color=#D2B9D3}{i}(But I hope I’m by your side the entire time…)"
    j "You look bothered, is everything okay?"
    hide j_worried

    menu:
        "{color=#2E8B57}I have something to tell you ":
            call k5
        "{color=#2E8B57}Nevermind":
            call k6
    show k_shy
    k "{color=#D2B9D3}{i}(*thinks in a mocking voice* Heyyy! Want to get a romantic dinner with me while the whole world judges how I’m in love with a man?)"
    k "Umm, Do you want to get dinner? Tonight? Or or or whenever you’re free haha."
    hide k_shy
    show j_normal
    j "Aren’t we getting dinner later tonight?"
    hide j_normal
    show k_laugh
    k "OH! Oh yeah! We are haha."
    hide k_laugh
    show j_normal
    j "Okay, now I know something is definitely up. You never forget when we have plans. You can tell me anything, you know that right?"
    hide j_normal
    show k_shy
    k "{color=#D2B9D3}{i}(Just tell him. Come on. It shouldn't be that hard. You see the way he looks at you, Dani thinks he likes you back)"
    k "{color=#D2B9D3}{i}(Ok. It’s time, I’m going to tell him I have the biggest crush on him. Alright, deep breath)"
    k "{color=#D2B9D3}{i}(One…two… three)"
    hide k_shy
    show k_say
    with hpunch
    k "JOHN I THINK I -"
    hide k_say

    "*Suddenly a woman trips and spills her entire drink on Kyle*"
    
    show k_angry
    with hpunch
    k "THE HELL??"
    hide k_angry
    show i_sup
    i "Oh my goodness, I am so sorry! I did not see you there!"
    hide i_sup
    show pra
    "*Paparazzi with their cameras come running in from nowhere beginning to take photos of Kyle drenched in soda*"
    hide pra
    show k_angry
    k "What is your problem??"
    hide k_angry
    show k_sup
    k "{color=#D2B9D3}{i}(Oh crap- it’s Isabel Adams)"
    hide k_sup
    show g_angry
    with hpunch
    g "Hey man don’t talk to her like that! It was an accident!"
    hide g_angry
    show j_q
    j "Hey guys, the paparazzi is getting this all on camera. Mind if we all go somewhere a little more private than the Hollywood Walk of Fame??"
    hide j_q
    show i_natural
    i "Good call, let’s go"
    hide i_natural

    show black
    centered "{size=+10}{color=#fff}They all proceed to walk to the nearest mall and converse in a secluded hallway"

    scene hallway
    with dissolve
    hide picture_10
    pause 1.0
    show j_smile
    j "Uh, a little earlier than we anticipated and not the ideal method but uh, Kyle Wang, meet Isabel Adams. Isabel Adams, Kyle Wang."
    hide j_smile
    show k_angry
    k "She spilled soda on my new shirt."
    hide k_angry
    show j_q
    j "{color=#D2B9D3}{i}*Whispers into his ear*{/color=#D2B9D3}{/i} Will you stop acting like a child and get along?"
    hide j_q
    show k_angry
    k "I have a reputation to uphold and how do you think it looks when someone makes a fool of me in public??"
    hide k_angry

    show g_angry
    g "How do you think I feel? Isabel and I weren’t even supposed to be seen out together. This time tomorrow our photos will be all over the tabloids!"
    hide g_angry

    show k_grouch
    k "And who are you again?"
    hide k_grouch
    show j_smile
    j "This is George, my brother."
    hide j_smile
    show k_grouch
    k "There’s two of you?"
    hide k_grouch
    show g_smile
    g "I’m the more handsome one."
    hide g_smile
    show j_smile
    j "Sure, but I got all the brains"
    hide j_smile
    show k_grouch
    k "George… George Smith? The actor?"
    hide k_grouch
    show g_smile
    g "In the flesh! It’s okay if you want to ask for an autograph, I know I’m… kind of a big deal in this town"
    hide g_smile
    show j_normal
    j "You may be handsome, but you are one cocky son of a -"
    hide j_normal
    show i_smile
    i "ANYWAYS… Kyle! It is finally nice to meet you"
    "{color=#D2B9D3}{i}*shakes his hand hesitantly*"
    i "Sorry about the whole, soda situation"
    hide i_smile
    show k_grouch
    k "It’s fine, just a… $300 shirt… no big deal"
    hide k_grouch
    show i_sup
    with hpunch
    i "$300???"
    hide i_sup
    show g_sup
    with hpunch
    g "$300???"
    hide g_sup
    show j_suprised
    with hpunch
    j "$300???"
    j "Why the hell would you spend $300 on the shirt and proceed to wear that shirt when I said we would be walking around Downtown LA??"
    hide j_suprised
    show k_happy
    k "Just in case photographers or any fans wanted to come up to me…"
    k "They sure came to me, though. The shirt was pointless"
    hide k_happy
    show i_worried
    i "I will definitely pay for the dry cleaning, I am so sorry."
    hide i_worried
    show k_happy
    k "I will happily take that offer"
    k "Other than that, it is nice to finally meet you"
    k "But going back to what George said, why are you so concerned if you’re photographed together?"
    hide k_happy
    show g_smile
    g "Well, you see-"
    hide g_smile
    show i_worried
    i "BECAUSE! Becauseeee people will speculate we are together and I do not need that that information in the papers. I’m already dealing with bad press from bumping into Charles Manson on the street… I do not need another headline"
    hide i_worried
    show k_n
    k "Mhm"
    k "{color=#D2B9D3}{i}(Totally not suspicious){/i}"
    hide k_n
    show k_sup
    k "Anyways, I have to go meet my co-star, we’re going to go run some lines before we start training tomorrow"
    hide k_sup
    show j_normal
    j "What, since when? What about dinner?"
    hide j_normal
    show k_sup
    k "Raincheck? It slipped my mind how tomorrow’s the first day of training"
    hide k_sup
    show j_normal
    j "Yeah, of course"
    hide j_normal

    show k_natural
    show mic
    "*Kyle waves goodbye to George and Isabel and exits the hallway. Paparazzi immediately meet him outside the door and question him what had happened*"
    hide k_natural
    hide mic
    "*Back in the hallway, George, Isabel, and John are still discussing*"
    show i_angry
    i "{color=#D2B9D3}{i}*slaps George’s arm*"
    with hpunch
    i "COME ON!"
    hide i_angry
    show g_angry
    with hpunch
    g "WHAT DID I DO???"
    hide g_angry
    show i_angry
    i "What DIDN’T you do?"
    i "You buy me the drink, you decide to take a stroll on the Hollywood Walk of Fame, then proceed to nudge me hard enough where I spill the drink onto Kyle Wang, and almost tell him how we’re dating! What in the world are you on today???"
    hide i_angry

    show j_awkward
    j "Oh god… I’m in the middle of a lovers quarrel…"
    j "I think I’m going to step out"
    hide j_awkward


    show i_angry at left
    show g_angry at right
    with hpunch
    "DO NOT MOVE"
    hide i_angry
    hide g_angry
    show g_natural
    g "Isa, take a deep breath, my love. It was just a bad day."
    hide g_natural
    show i_ren
    i "{color=#D2B9D3}{i}*Closes her eyes, takes three deep breaths*"
    i "You’re right, you’re right. Everything’s okay"
    hide i_ren
    show j_relieved
    j "Worst case scenario, people think you two are dating. I feel like more people will be looking at Isabel spilling soda on Kyle. This is good, this is good. We can craft a story from this."
    hide j_relieved
    show g_cu
    g "So nothing has changed with you. Something happens and your immediate reaction is to fix it…"
    hide g_cu
    show j_annoyed
    j "As opposed to what? Stewing in defeat? Questioning when this plan is going to fail before it even starts?"
    j "Kyle pays me to do my job. That job just so happens to be ~fixing problems~ and getting him higher up in this industry where sooo many people want to see him FAIL."
    hide j_annoyed
    show j_sad
    j "So yes, my immediate reaction is to “fix it”… I… care about him… a lot."
    hide j_sad
    show i_worried
    i "{color=#D2B9D3}{i}(Why did he say “I care about him, a lot” like that. There’s something he’s not telling us…)"
    hide i_worried
    show g_nothing
    g "Alright, I see where you’re coming from. Just, please, make sure this is all okay?"
    hide g_nothing
    show j_natural
    j "I always do…"
    hide j_natural
    show j_smile
    j "Just remember, smile and wave. Smile and wave."
    hide j_smile

    "*ISA LEAVES THE HALLWAY FIRST, AVOIDING ANY FURTHER SUSPICION*"

    "*JOHN AND GEORGE FOLLOW OUT A FEW MINUTES LATER*"
    
    show black
    centered "{size=+10}{color=#fff}THANKS FOR PLAYING"
   
    return


label k1:
    show k_lilupset
    k "Fine, I’ll do it. But only if you’ll be by my side the entire time."
    hide k_lilupset
    show j_worried
    j " By your side in a conundrum like this? Kyle, I will be there the whole time. And I… I will always love yo-y- your ambition in this industry! It’ll be quick, two years will fly by. I promise. "
    hide j_worried
    show k_grouch
    k "AH! Thanks! Um, you’re the, uh,  best manager. Truly, Thank you. Thank you."
    hide k_grouch 
    show j_awkward
    j "{color=#D2B9D3}{i}*Voice starts to get nervous*"
    j "Yeah! Uh, of course. You pay me to do my job haha…ha. Okay! Well, I’ll catch you on the flip side"
    j "{color=#D2B9D3}{i}*awkward finger guns to Kyle*"
    hide j_awkward
    return
label k2:
    show k_angry
    k "No! I will not compromise my values for some silly charade!"
    hide k_angry
    show j_worried
    j "Kyle, you do not have a choice in this situation. I’m sorry but as your manager, you have to do this. It’ll be the best path for OUR success. "
    hide j_worried
    show k_grouch
    k "God, if it weren’t for how well you do your job… I don’t know if you’d still be my manager. "
    hide k_grouch
    show j_natural
    j "Alright. Well, I have to go to a meeting. We’ll speak more on this later. I have to tell the producers we’re all on the same page. "
    hide j_natural
    return
label i1:
    show i_ren
    i "Nonetheless, I guess I’ll “date” Kyle Wang for the time being."
    hide i_ren
    show g_natural
    g "Ok, I’ll tell John you’re good to go. It’ll be fuuuun!"
    hide g_natural
    return
label i2:
    show i_angry
    i "Nonetheless, I am not “dating” Kyle Wang - it’s my film and mine to promote."
    hide i_angry
    show g_natural
    g "Isa, I understand. But Kyle’s already agreed and it’s for the both of you. Think of it this way - it’s for the minority community. They’re just as American as we are, but so much is happening in the world right now we need to push for more."
    hide g_natural
    return
label k3:
    show k_upset
    k "I have a secret I need to tell you"
    hide k_upset
    show d_red
    d "Tell me, please. And I’ll tell you one as well"
    hide d_red
    show k_sup
    k "You have a secret too?"
    hide k_sup
    show k_upset
    k "It’s probably not as bad as mine. But alright… here I go…"
    hide k_upset
    return
label k4:
    show k_upset
    k "Nervous, nervous for filming"
    hide k_upset
    show d_normal
    d " yeahhhh, for “filming”. Can you tell me what’s REALLY going on?"
    hide d_normal
    show k_sup
    k "How do you know me so well?"
    hide k_sup
    show k_upset
    k "Fine… this is what’s really bothering me"
    hide k_upset
    return
label k5:
    show k_lilupset
    k "I have something to tell you"
    hide k_lilupset
    show j_smile
    j "What is it?"
    hide j_smile
    return
label k6:
    show k_lilupset
    k "Nevermind"
    hide k_lilupset
    show j_natural
    j "I can tell something is up, what is it?"
    hide j_natural
    return