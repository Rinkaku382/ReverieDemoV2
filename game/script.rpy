
define slowfade = Fade (1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)
define config.hard_rollback_limit = 0
define config.menu_include_disabled = True
init:
    image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

define s = Character("Sofia", color="#C69AF9")
define ug = Character("Unknown Girl", color="#C69AF9")
define stm = Character("Strange Man", color="#7BC2F4")
define scm = Character("Scary Man", color="#ED5259")


label start:
    stop music fadeout (3)
    scene roomd_dawn
    with slowfade
    play music "roomd_bgm.ogg" fadein (3)
    $ mood = 50
    $ menth = 0
    $ sofiatalk = False
    $ sofiatalk2 = False
    $ sofia = 5
    $ guit = False
    $ guitcheck = False
    $ toy = False
    $ toycheck = False
    $ strangeman = False
    $ scaryman = False
    $ teddyrep = False
    default allowm_choice = False
    default allowguit_choice = False
    default allowun_choice = False
    default allowrep_choice = False
    default allowsol_choice = False
    """
    Waking up, you feel a bittersweet sensation in your heart.

    It flows through your whole body towards your mind.

    It's a melancholic feeling.

    You're lost in time, nothing more than a pale figure in an apartment you don't remember.

    When you try to recall something about you...

    Nothing comes to your mind.

    As if everything has been deleted.

    But maybe in your apartment there is something that can help you?
    """
    jump roomdownscreen2

label sofiagoodfade2:
    scene sofiah_d
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofiasadfade2:
    scene sofias_d
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofianeutfade2:
    scene sofian_d
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2

label roomdown2:
    scene roomu_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label roomdownscreen2:
    scene roomd_dawn
    call screen roomdownscreen2

label roomup2:
    scene roomd_dawn
    $ renpy.pause(0.5)
    scene roomu_dawn
    with fade
    $ renpy.pause(1)
    jump roomupscreen2
label roomupscreen2:
    scene roomu_dawn
    call screen roomupscreen2
label window2:
    """
    Looks like a gloomy day outside.

    Everything seems strangely empty.

    And the grey sky does not make you feel better.
    """
    jump roomdownscreen2
label bed2:
    """
    You can't sleep now.

    There are things you have to do.
    """
    jump roomupscreen2
label books2:
    """
    A library filled with books.

    Now that you pay more attention to it...

    You realize there are plenty of books about art.

    You look at the titles, unable to choose which book read.

    You pick and old essay about cinema.

    You remember the author's name, but not the title.

    'It's a film about you, your father, your grandfather.'

    'About someone who will live after you and who is still 'you'.'

    You put the book back on the shelf.
    """
    jump roomdownscreen2
label plant2:
    show plant
    with dissolve
    """
    The leaves' green is brilliant...

    Yet there seems to be some dust on them.
    """
    hide plant
    with dissolve
    jump roomdownscreen2
label trash2:
    show trash
    with dissolve
    """
    Trash seems to be piling up...
    """
    hide trash
    with dissolve
    jump roomdownscreen2
label phone2:
    show phone
    with dissolve
    """
    The dust never disappear from this phone, huh?

    Someone left a message in the answering service.

    'Hi, it's mom.'

    'I just called to know how you're feeling, but...'

    'It seems like you don't want to talk.'

    'I hope that, at least, you get out of the apartment, sometimes.'

    'Well...bye.'
    """
    hide phone
    with dissolve
    jump roomdownscreen2
label tv2:
    """
    There's a french movie on the tv.

    A young woman is alone at home, doing absolutely nothing but smoking a cigarette.

    Someone starts to insistently knocking on the door.

    She's irritated by that.
    """
    jump roomdownscreen2
label cds2:
    """
    Whenever you watch at this pile of CDs...

    You think it's a shame you don't have a CD-player.
    """
    jump roomdownscreen2
label toy2:
    if toycheck == False:
        show teddybrok
        with dissolve
        """
        An old teddy bear.

        You're unable to toss it away.

        Even after all this time, you can't undestand why.

        Maybe you're sill connected with the person who gave it to you.
        """
        hide teddybrok
        with dissolve
        jump roomupscreen2
    if toy == True:
        if teddyrep == False:
            show teddybrok
            with dissolve
            """
            Whatever the state this teddy is in, it still is important for your memories.
            """
            hide teddybrok
            with dissolve
            jump roomupscreen2
        if teddyrep == True:
            show teddyrep
            with dissolve
            """
            Whatever the state this teddy is in, it still is important for your memories.
            """
            hide teddyrep
            with dissolve
            jump roomupscreen2
    if toycheck == True:
        show teddybrok
        with dissolve
        $ toy = True
        """
        This teddy seems to be old.

        One of the arms is ruined and almost falls off.

        You grab it and look at it closely.

        It gives you a deep sense of melancholy.

        You feel the pressure of its age on you and some imagese start to pop up.

        There is a girl, smiling at you.

        She's going away and both of you are...sad.

        Neither knows when you'll see each other again.

        So she opens her backpack and takes out that same teddy bear.

        That's the last scene you see.

        The teddy bear's arm falls to the ground.
        """
        menu:
            "Find something to repair it.":
                $ allowrep_choice = True
                $ teddyrep = True
                hide teddybrok
                with dissolve
                show teddyrep
                with dissolve
                $ mood += 5
                """
                Wandering through the entire house you've found a needle and a thread.

                As you're not used to it, you find difficulties in fixing the arm.

                But the result isn't that bad.
                """
                hide teddyrep
                with dissolve
                jump roomupscreen2
            "Leave it as it is.":
                $ mood -= 5
                """
                You put the teddy and the arm back on the shelf.
                """
                hide teddybrok
                with dissolve
                jump roomupscreen2
label mirror2:
    show mirror
    with dissolve
    if sofiatalk2 == False:
        """
        There's only you.
        """
        hide mirror
        with dissolve
        jump roomupscreen2
    if sofiatalk2 == True and mood == 55 or mood == 45:
        """
        There's a garden in the reflection.

        It looks as if it's inviting you to enter.

        Do you go through the mirror?
        """
        menu:
            "Yes.":
                hide mirror
                with dissolve
                jump memories2
            "Not now.":
                hide mirror
                with dissolve
                jump roomupscreen2
label guit2:
    show guitar
    with dissolve
    if guitcheck == False:
        """
        This guitar...

        As you watch it, you remember playing it sometimes.

        But how much time has passed since then?
        """
        hide guitar
        with dissolve
        jump roomupscreen2
    if guit == True:
        """
        It's a shame you never have the time to play it.
        """
        hide guitar
        with dissolve
        jump roomupscreen2
    if guitcheck == True:
        $ guit = True
        """
        The guitar is covered by dust.

        No one has even touched it in a long time.

        The strings are still in good condition, though.

        And when you touch it's strings, you seem to faintly remember something.

        Someone gives you a big cardboard box.

        You open it and discover that, inside, there's this same guitar.

        It's someone's present...but by whom?

        You start to think that maybe you could play it.
        """
        menu:
            "Just a little...":
                $ allowguit_choice = True
                $ mood += 5
                """
                As you start playing, slowly, something comes to your mind.

                Your fingers move on their own.

                They form a melody that recalls strange and blurred images.

                As if they are born from mist.

                But then...why are you crying?
                """
                hide guitar
                with dissolve
                jump roomupscreen2
            "Maybe another time.":
                $ mood -= 5
                """
                You just clean the dust off and leave it where it was.
                """
                hide guitar
                with dissolve
                jump roomupscreen2
label door2:
    "I can't get outside, it's tightly closed."
    jump roomdownscreen2

label computer2:
    if sofiatalk == False:
        jump sofianeut2
    if sofiatalk2 == True and mood >= 55:
        jump sofiagood2
    if sofiatalk2 == True and mood <= 45:
        jump sofiasad2
    if sofia >= 6 and guit == False:
        "Looks like she'll be occupied for some time."
        jump roomdownscreen2
    if sofia <= 4 and toy == False:
        "Looks like she'll be occupied for some time."
        jump roomdownscreen2
    if guit == True:
        jump sofiaguit
    if toy == True:
        jump sofiatoy

label sofiagood2:
    scene sofiah_d
    with slowfade
    s """
    It's nice seeing you smiling like this, you know?

    Uhm, looks like your hair is a little messy!

    Have you checked on yourself in the mirror, this morning?
    """
    jump sofiagoodfade2
label sofiasad2:
    scene sofias_d
    with slowfade
    s """
    Is it me or you seem a little down?

    You look so tired and messy, too!

    Have you checked on yourself in the mirror, this morning?
    """
    jump sofiasadfade2
label sofianeut2:
    scene sofias_d
    with slowfade
    $ sofiatalk = True
    """
    There's a girl on the computer screen.

    She seems sad and terribly tired.

    Even though you've never seen her, you have a strange feeling...
    """
    ug """
    You're finally back!

    Where were you?

    You could've warn me, I've waited for so much...
    """
    menu:
        "Is that...you?" if allowm_choice:
            pass
        "Sorry, but...who are you?":
            $ sofia += 1
            ug """
            Guess your memory still isn't alright, huh...?

            Well, anyway, my name is Sofia. I'm your...best friend.
            """
        "I don't remember...":
            $ sofia -= 1
            ug """
            I imagined you'd still not remember anything...

            Anyway, don't worry, I'm Sofia.

            We're best friends.
            """
    scene sofian_d
    with dissolve
    s """
    It's been a while since you lost your memory.

    But don't worry, I'm here to help.

    First of all, as you already know, this is your computer.

    By interacting with it, you'll be able to talk with me.

    Now, second...have you already tried opening the door?
    """
    menu:
        "Yes.":
            s """
            Very well. Then you should have noticed it's close.
            """
        "No.":
            s """
            Well, doesn't matter since it's closed.
            """
    s """
    It's been a while since it closed itself.

    I don't really know how to open it, and...

    In fact, you haven't been outside for a lot of time.

    Anyway, you want to ask me something, right?
    """
    menu:
        "Were you here all this time?":
            $ mood += 5
            scene sofian_d
            with dissolve
            $ sofia += 2
            s """
            Yes, since before you lost your memory.

            In fact, I waited for some days, but...

            You're here, now, so that's the important thing!

            Isn't it?
            """
        "Why have you waited for me?":
            $ mood -= 5
            scene sofias_d
            with dissolve
            $ sofia -= 2
            s """
            Uhm because we're friends...?

            Doesn't it make enough sense for you?

            Because for me it really does...
            """
    if sofia >= 6:
        scene sofian_d
        with dissolve
        $ guitcheck = True
        s """
        Well, going back to business!

        While I was waiting for you to come back I was thinking about something...

        Some time ago you told me about your guitar!

        Are you still playing it?

        I remember that someone gave it to you as a present...one year ago, maybe.

        Or something like that, anyway.

        So I was a little curious, you know?

        Oh, I'm sorry, someone is calling me, can we continue later?
        """
        scene roomd_dawn
        with slowfade
        jump roomdownscreen2
    if sofia <= 4:
        scene sofias_d
        with dissolve
        $ toycheck = True
        s """
        You're quite distant...

        I'm sorry, maybe you think I'm akward, since you don't remember anything about me.

        I'm really sorry about that.

        You know, I was looking at the teddy bear you gave me some time ago.

        It's really sad to think about this distance, now.

        I'd like to do more for you, but...

        Uhm sorry, someone is calling me, can we continue later?
        """
        scene roomd_dawn
        with slowfade
        jump roomdownscreen2
label sofiaguit:
    scene sofian_d
    with slowfade
    $ sofiatalk2 = True
    s """
    So, remembered something?
    """
    menu:
        "Some kind of strange melody..." if allowguit_choice:
            pass
            $ mood += 5
            s """
            A melody, huh...

            The only thing I know is that who gave that guitar to you was a man.

            During your first year at university, if I remember correctly.

            Maybe you remembered about him?

            That would be natural, after all.

            Unfortunately, though, I don't know much about him.

            But I'm glad that helped you!
            """
        "Only blurred scenes.":
            $ mood += 5
            s """
            Oh, that's a pity...

            But it's not that bad, right?

            Maybe next time will be better!

            It could only mean that the guitar does not means enough to you.

            But I don't know much more than that, sorry.

            But anyway!

            Your apartment has so many items that some of them certainly must be important, right?
            """
        "I'm not so sure...":
            $ mood -= 5
            s """
            That really is sad...

            I was hoping that, perhaps, the items in your house could help you remember.

            Maybe it just wasn't the right one?

            It could only mean that the guitar does not have any meaning to you.

            But anyway!

            Your apartment has so many items that some of them certainly must be important, right?
            """
    s """
    Oh, your apartment is so full of interesting things!

    I admire so much your collections.

    I totally envy you!

    In any case, you should really take a good look around, now.

    Try to get acquainted with your apartment, if you don't remember about it so well.

    If you need something I'm here!
    """
    scene roomd_dawn
    with slowfade
    jump roomdownscreen2
label sofiatoy:
    scene sofian_d
    with slowfade
    $ sofiatalk2 = True
    s """
    There you are!

    How did it go?

    So, do you want to know who gave that teddy bear to you?
    """
    menu:
        "Tell me about it.":
            $ allowsol_choice = True
            $ mood += 15
            $ sofia += 2
            s """
            Very good!

            Well, then...

            We met each other before university, and got separated during that period.

            I transferred to another place and you didn't, so...

            So we always spent time talking like this, through internet.

            It happened at the same time you decided to live by your own.

            You were alone and not at all used to live in a place so empty and new.

            I guess it's normal, though.

            Most people feel like that when they start something new.

            It looks dark and scary, but with time...everyone gets used to everything, right?

            So anyway, before leaving I decided to give that teddy bear with you, as a memento.

            And you gave one to me, too!

            TGo be sincere...those teddies were not enough to ease the solitude.

            For neither of us.

            But then you knew this person, at your university.

            A teacher, I think...

            Well, I'm sure he was a very dear friend to you, anyway.

            And you often said that it was strange, but...

            The teddy I gave you started to remind me and him as well, to you.

            And I'm glad it's been helpful!
            """
            menu:
                "It was broken, but I repaired it." if allowrep_choice:
                    pass
                    scene sofiah_d
                    with dissolve
                    s """
                    I was wandering if it was!

                    After all it's very old...

                    Thank you for repairing it!
                    """
                "It really was.":
                    s "So..."
        "Was it you?":
            $ mood -= 15
            scene sofias_d
            with dissolve
            $ sofia -= 2
            s """
            Uh, well, yeah.

            I thought it could be useful.

            Well, sorry, maybe I'm just saying things you already know.
            """
    s """
    In any case, you should really take a good look around, now.

    Try to get acquainted with your apartment, if you don't remember about it so well.

    If you need something I'm here!
    """
    scene roomd_dawn
    with slowfade
    jump roomdownscreen2

label memories2:
    if mood <= 45:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        play movie "trauma.ogv" loop
        show movie with slowfade
        play music "trauma_bgm.ogg" fadein (3)
        """
        You find yourself in a dark place, ruled by sad and heavy feelings.

        It's the garden you saw in the mirror, but somehow different.

        The entire place seems to be falling apart.

        In front of you there is a man.

        He's looking at you, his eyes glittering in the darkness.

        Suddenly, you feel a stabbing pain hitting you.

        You feel alone, somehow, and that black shadow seem to be connected to that feeling.
        """
        scm """
        You don't remember...

        Or you don't want to remember?

        Who are you?

        Who am I?

        Asking yourself those questions won't solve anything.

        You deserve no love.

        No love at all.
        """
        if toy == True:
            scm """
            If you don't even care about a teddy bear's arm...

            How could you even live in the everyday world?

            You don't even care about the presents your dear one give to you.
            """
        if guit == True:
            scm """
            It seems like you're avoiding the memories of me.

            Neglecting your past.

            And not taking care of your present.

            But it's your choice, it's all up to you.
            """
        """
        You're scared.

        You know that shadow comes from your memories, but...

        You try to remember.

        Hard.

        Harder.

        But nothing comes to your mind.

        Absolutely nothing.

        And the scene starts to disappear.
        """
        show black
        with fadehold
        stop music fadeout (3)
        return
    if mood >= 55:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene mem1
        with slowfade
        play music "mem_bgm.ogg" fadein (3)
        default allowuniq_choice = False
        default allowfriend_choice = False
        default allow_choice = False
        $ peaceful = False
        $ confused = False
        """
        A foggy and pale garden.

        Everything seem confused.

        Your memory is trying to recall this place but it's all blurred...

        And the man seated in front of you
        """
        stm """
        Bolder, lighter than a bird's wing,

        You hurtled like vertigo

        Down the stairs, leading

        Through moist lilac to your realm

        Beyond the mirror.
        """
        """
        You look at the mysterious man in front of you.

        He just finished reading a passage from the book he's holding.
        """
        stm """
        Do you remember this poem?

        It's by Tarkovskij.

        It brings back so many memories...

        Yet, you don't seem to recall any of them...

        That makes me sad.

        So sad...
        """
        """
        A pause of silence.

        You don't know what to say, as you don't recognize that man at all.

        At the same time, he seems to be lost in his thoughts.
        """
        stm """
        You know, it's difficult...

        To find something to talk about with you.

        Would it be useful to say who I am?

        Or what I know about you?

        Here I am, a pale figure in your memories, and the only one who could help you.

        And yet, I don't have the slightest idea of what to say.
        """
        menu:
            "I think I saw you in a memory." if allowguit_choice:
                pass
                stm """
                You saw me?

                That means you're slowly remembering, maybe.

                Hmm, let's see...

                In times like this, when I know that there's distance between us...

                I try to remember an old melody.

                And as soon as I recall even few words from it, I instantly feel better.

                It was...
                """
                menu:
                    "My melody...":
                        stm """
                        Yes...your melody.

                        You used to whisper it often.

                        Especially when you were alone or in this garden.
                        """
                    "Our melody...":
                        stm """
                        It's nice to see you remembering about it.

                        Maybe, with time...

                        You'll remember about this place.

                        And about me, too.
                        """
            "Sofia was talking about you...?" if allowrep_choice:
                pass
                stm """
                Hmm.

                You know...

                I often observed you, through the mirror.

                Your apartment still seems to be filled with old presents.

                Like gentle poems, they stumble into your universe.

                Some for a short period of time, others for a little longer.

                It's nice seeing you taking care of them.

                That girl must be truly happy.

                As well as the teddy ear, if only it could live, right?
                """
                menu:
                    "You know her?":
                        stm """
                        I know you, so of course I know her.

                        You used to talk a lot about that girl.

                        Sofia, right?

                        I don't know much about her, just as well as I imagine she does not know much about me, either.

                        Hm? Is there something you want to tell me about her?
                        """
                        menu:
                            "She's just strange...a little.":
                                stm """
                                Strange?

                                Well, by the situation I gues everyone wouldn't feel at ease.

                                So I guess it's normal for her to look strange.

                                More so if you don't remember anything about her.
                                """
                            "She's funny.":
                                stm """
                                When you told me about her you said she was.

                                And that she was totally afraid of leaving you alone.

                                But, in time, both of you got acquainted with the distance.
                                """
                    "You saw me?":
                        stm """
                        It may sound strange but it's simpler than it may seem.

                        That mirror is a window on your solitary life.

                        And as mirrors are a reflection of our lives, that one is for me the perfect reflection.

                        Do you get what I mean?
                        """
                    "You're changing the subject.":
                        stm """
                        Well, there's nothing much I can say about that.

                        I knew you and you told everything about me to her.

                        There's nothing more than that.

                        Apart from what you told me, I don't even know that much about her.

                        Only that you two are dear friends, even more than how we were.
                        """
            "What is this place?":
                stm """
                This place...

                It's a place in which we used to spend our time.

                Talking, reading, discussing...

                Something like a refuge from everything and everyone.

                In this place we knew each other...and left each other.

                But that's not important, now.
                """
            "How do you know me?":
                stm """
                I don't know how useful my answer could be, but...

                Let's say I was your teacher.

                I did, in fact teach you about the world that surrounds you.

                About what it hides from all of us.

                And how to survive to it, when possible.
                """
        

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################                            F I R S T   N I G H T   P A S S A G E #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label night1:
    stop music fadeout (3)
    scene roomd_night
    with slowfade
    play music "roomn_bgm.ogg" fadein (3)
    """
    aaa
    """
    jump roomdownscreenn1

label roomdownn1:
    scene roomu_night
    $ renpy.pause(0.5)
    scene roomd_night
    with fade
    $ renpy.pause(1)
    jump roomdownscreenn1
label roomdownscreenn1:
    scene roomd_night
    call screen nightscreendown1

label roomupn1:
    scene roomd_night
    $ renpy.pause(0.5)
    scene roomu_night
    with fade
    $ renpy.pause(1)
    jump roomupscreenn1
label roomupscreenn1:
    scene roomu_night
    call screen nightscreenup1
label windown1:
    """
    Outside the window the streets look solitary.

    There's no one around.

    And the moon is high and pale.

    It seems to be watching you.
    """
    jump roomdownscreenn1
label bedn1:
    """
    You feel so tired...

    Do you want to sleep?
    """
    menu:
        "Yes.":
            "As you get in the bed, your eyes instantly close."
            jump narrator
        "No.":
            "Maybe later"
            jump roomupscreenn1
label booksn1:
    """
    You're too tired to read now.
    """
    jump roomdownscreenn1
label plantn1:
    show plant
    with dissolve
    """
    The plant seems melancholic with this light.
    """
    hide plant
    with dissolve
    jump roomdownscreenn1
label trashn1:
    show trash
    with dissolve
    """
    The usual trash bin.
    """
    hide trash
    with dissolve
    jump roomdownscreenn1
label phonen1:
    show phone
    with dissolve
    """
    No messages left on the answering service.
    """
    hide phone
    with dissolve
    jump roomdownscreenn1
label tvn1:
    """
    It's turned off.
    """
    jump roomdownscreenn1
label cdsn1:
    """
    Ever wandered what would happen if these CDs fell?
    """
    jump roomdownscreenn1
label toyn1:
    show teddybrok
    with dissolve
    """
    It's as if it is smiling at you.
    """
    hide teddybrok
    with dissolve
    jump roomupscreenn1
label mirrorn1:
    show mirror
    with dissolve
    """
    There is only you, now.
    """
    hide mirror
    with dissolve
    jump roomupscreenn1
label guitn1:
    show guitar
    with dissolve
    """
    It's too late to play it.
    """
    hide guitar
    with dissolve
    jump roomupscreenn1
label doorn1:
    "I can't get outside, it's tightly closed."
    jump roomdownscreenn1

label computern1:
    scene aaa
    with slowfade
    """
    She's sleeping.

    It's better to not disturb her.
    """
    scene roomd_night
    with slowfade
    jump roomdownscreenn1

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 3 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator:
