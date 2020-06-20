
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
define uv = Character("Unknown Voice", color="#C69AF9")
define m = Character("Mom")


label start:
    stop music fadeout (3)
    scene roomd_dawn
    with slowfade
    play music "roomd_bgm.ogg" fadein (3)
    $ mood = 50
    $ menth = 0
    $ mem = 0
    $ trauma = 0
    $ guilt = False
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
    if sofiatalk2 == True and mood >= 55 or mood <= 45:
        """
        There's a garden in the reflection.

        It looks as if it's inviting you to enter.

        Do you go through the mirror?
        """
        menu:
            "Yes.":
                hide mirror
                with dissolve
                jump memories
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

        Maybe you still remember that song...
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
    "You can't get outside, it's tightly closed."
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

            In fact, I've been waiting for days, but...

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

label memories :
    if mood <= 45:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        play movie "trauma1.ogv" loop
        show movie with slowfade
        play music "trauma_bgm.ogg" fadein (3)
        $ trauma += 1
        $ menth += 1
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

        Asking yourself those questions won't solve anything, here.

        You deserve no love.

        No love at all.

        You always only cared about yourself.

        Is there even something you care about?
        """
        menu:
            "Sofia's gift." if toy:
                pass
                if allowrep_choice == False:
                    $ guilt = True
                    scm """
                    Her gift?

                    You didn't even fixed it.

                    If you can't even do something so little...

                    How could you live in the everyday world?

                    You don't even care about the presents your dear ones give to you.
                    """
                if allowrep_choice == True:
                    $ guilt = True
                    scm """
                    You took the time to fix it, sure.

                    But are you sure you've done it for her and not for yourself?

                    That you did it to honour the memories of her and not to gain some benefits from it?

                    Something like a positive ending.

                    Or the end of your solitude.

                    Is this the person you truly are or not?

                    You care about her?

                    Even though you don't remember anything about her?

                    That really is particular, you know?

                    Unexpected.

                    But understandable.

                    After all...

                    Who does not want to be loved?

                    Are there people who desire to be alone?

                    You've seen a safe spot in which to hide from your loneliness...

                    And, right away, you took the occasion and took advantage of it.

                    It's only human to do that.
                    """
            "That guitar..." if guit:
                pass
                if allowguit_choice == False:
                    scm """
                    You barely looked at it, didn't you?

                    It seems like you're avoiding the memories that tie you to me.

                    Neglecting your past, are you?

                    And not taking care of your present, neither.

                    But it's your choice, it's all up to you.

                    Do you feel good about it?

                    Is this how you want to confront the past?
                    """
                if allowguit_choice == True:
                    scm """
                    So you're starting to remember...

                    That's new of you.

                    But weren't you guided to do it?

                    Wasn't there someone that told you about that guitar?

                    And I bet you know who gave it to you, but you don't have the courage to say it.

                    That's typical.
                    """
        scm """
        Have you ever asked yourself...

        Who are you?

        Someone who has no memory is nobody.

        Who are you, without your past?

        Only a name stumbling in solitude and darkness.

        Looking for the lost past, desperate to find it.

        And are you even sure you can find what you are looking for?
        """
        """
        You feel scared.

        And the scene starts to disappear.
        """
        stop music fadeout (3)
        jump night1
    if mood >= 55:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene mem1
        with slowfade
        play music "mem_bgm.ogg" fadein (3)
        $ mem += 1
        $ sofiaknow = False
        $ melody = False
        $ place = False
        $ knowyou = False
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
            "I think I saw you in a memory." if guit:
                $ melody = True
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
            "Sofia was talking about you...?" if toy:
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
                        $ sofiaknow = True
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
        stm """
        You know...

        I understand how difficult it is to lose contact with the present.

        You start to wander between past and present with no precise direction.

        And everything is confused, everything is blurred.

        Nothing seems real anymore and all the people around us can't reach us in any way.

        We become blind and, then, we start loosing everything in our constant research of the past.

        We eventually lose ourselves in the past.

        So...be careful, ok?
        """
        menu:
            "What is this place?":
                $ place = True
                stm """
                This place...

                It's a place in which we used to spend our time.

                Talking, reading, discussing...

                Something like a refuge from everything and everyone.

                You know, when people feel attacked or trapped by the world around...

                All they can do is retiring in a safe place.

                Somewhere they know they won't be hurted.

                That is what this place has been.

                And maybe it still is.

                At least for me, but I don't know what it is for you.

                In this place we knew each other...and left each other.

                But what is it, now?

                Nothing more than a reverie, i guess.

                A place we both belong to and from which is hard to separate.

                But still, nothing more than a reverie.

                Oh, I'm sorry.

                It seems that seeing you makes me too much melancholic, right?

                But that's not important, now.
                """
            "How do you know me?":
                stm """
                I don't know how useful my answer could be, but...

                Let's say I was your teacher.

                I did, in fact teach you about the world that surrounds you.

                About what it hides from all of us.

                And how to survive to it, when possible.

                Who can you trust?

                What can you do to avoid the daily suffering?

                Even if these questions seem to have no answer at all...

                We used to find them in poetry and art.

                I know, it may seem ridiculus.

                And maybe, thinking about it now...it may be.

                But that's what we believed in.

                Of course, now things are different.
                """
        """
        As he talks, a tear starts to warm your left cheek.

        The entire landscape in front of you starts becoming paler.

        And then starts disappearing in the darkness, just as it appeared.
        """
        stop music fadeout (3)
        jump night1

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################                            F I R S T   N I G H T   P A S S A G E #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label night1:
    stop movie
    hide movie with slowfade
    scene roomd_night
    with slowfade
    play music "roomn_bgm.ogg" fadein (3)
    """
    Late night.

    You open your eyes in your apartment, as if you've fell asleep.

    Was it only a dream?

    Or was it, in fact, reality?
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
            stop music fadeout (3)
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
    "You can't get outside, it's tightly closed."
    jump roomdownscreenn1

label computern1:
    """
    She's sleeping.

    It's better to not disturb her.
    """
    jump roomdownscreenn1

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 2
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator:
    scene narrator
    with slowfade
    play music "narr_bgm.ogg" fadein (3)
    """
    And here it comes.

    Our first meeting.

    Were your memories delicate?

    Or were them painful?

    Don't worry.

    You're safe now, in your dreams.

    You may not be in your apartment.

    Or when you talk with someone.

    Or even when you try to recall what you have lost.

    But at least here nothing can hurt you.

    Only doubts, but are you sure you want to bring them with you along the dream?

    It wouldn't be a good idea.

    But the choice is yours.

    I'm just a spectator to all this.

    I always watch, and sometimes I ask questions.

    But not today, so worry not.

    And proceed until you reach tomorrow...
    """
    if guilt == False:
        jump day2
    if guilt == True:
        jump day2ghost

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################                S T A R T  D A Y 2  N O R M A L #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
label day2:
    stop music fadeout (3)
    scene roomd_aft
    with slowfade
    play music "rooma_bgm.ogg" fadein (3)
    $ mood = 50
    $ sofiatalk = False
    $ phans = False
    $ water = False
    """
    Early afternoon.

    You slowly wake up...

    But you don't know which day it is.

    How much time has passed?

    You have no idea.
    """
    jump roomdownscreen3

label sofiagoodfade3:
    scene sofiah_d
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3
label sofiasadfade3:
    scene sofias_d
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3
label sofianeutfade3:
    scene sofian_d
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3

label roomdown3:
    scene roomu_aft
    $ renpy.pause(0.5)
    scene roomd_aft
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3
label roomdownscreen3:
    if phans == False:
        stop music fadeout (1)
        play music "ringtone.ogg" fadein (2)
        scene roomd_aft
        call screen roomdownscreen3
    if phans == True:
        scene roomd_aft
        call screen roomdownscreen3

label roomup3:
    scene roomd_aft
    $ renpy.pause(0.5)
    scene roomu_aft
    with fade
    $ renpy.pause(1)
    jump roomupscreen3
label roomupscreen3:
    scene roomu_aft
    call screen roomupscreen3
label window3:
    """
    Outside the apartment the sun is high.

    It's so bright that you have difficulties at looking at the street below.

    Are the ones you see down there people?
    """
    jump roomdownscreen3
label bed3:
    """
    You are not tired, now.
    """
    jump roomupscreen3
label books3:
    """
    You take a book from the shelf.

    It's a collection of storyboard of animated movies.

    Each page is filled with notes...

    But they're all in Japanese so you can't understand them.
    """
    jump roomdownscreen3
label plant3:
    show plant
    with dissolve
    if water == False:
        """
        Flowers are taking their time to grow.

        And it seems to need some water...

        Do you water it?
        """
        menu:
            "Yes.":
                $ water = True
                "The leaves seem to be brighter, now."
            "Maybe later.":
                "You leave it as it is."
    if water == True:
        "Those little flowers cute, don't you think?"
    hide plant
    with dissolve
    jump roomdownscreen3
label trash3:
    show trash
    with dissolve
    """
    The usual trash bin.

    Nothing new from it.
    """
    hide trash
    with dissolve
    jump roomdownscreen3
label phone3:
    show phone
    with dissolve
    if phans == False:
        $ phans = True
        stop music fadeout (1)
        play music "rooma_bgm.ogg" fadein (2)
        """
        You lift the receiver.

        A feminine voice greets you softly.

        IIt recalls something from within you.

        Something distant and dear, but lost.
        """
        uv """
        Hi, dear...

        It's me, your mother.
        """
        m """
        I've been calling you for so long...

        And you've never answered.

        I left lots of messages, you know?

        Have you listened to them?
        """
        menu:
            "I did.":
                m """
                I'm glad...
                """
            "Of course...":
                m """
                You haven't, did you?

                But don't worry, I knew it already.
                """
        m """
        I'm sorry if I worry so much.

        Even if I know you have things to do...

        I can't help but be worried about you.

        But you never answer...and that hurts.
        """
        menu:
            "I'm sorry...":
                $ mood += 5
                m "I know you are."
            "I'm always busy.":
                $ mood -= 5
                m "Sure..."
        m """
        Anyway, how are things going?

        And what about Sofia?

        Do you still hear from her?

        She was such a gentle girl...

        It's a pity you two got separated.

        But I guess that's how life goes and we can't always be with who we want.
        """
        menu:
            "She helps a lot.":
                m """
                That makes me very happy, you know?

                I'm always happy when I know you two are together.
                """
            "She's ok, I guess.":
                m """
                You guess?

                So you two don't get along that well, anymore?

                Oh, sorry, sometimes I make my own conclusions, but that's not my business.
                """
        m """
        You know, I was looking at a photo of you two, yesterday.

        It reminded me so many things...

        It doesn't happen so often, for me, to remember the past.

        So I lose contact with it.

        But when I saw your faces...

        Something started to shine in my mind, you know?

        And I wanted to tell you about it so much...

        Oh and then I saw a photo of both of us with your uncle!

        He always reminded me of your father.

        Is he still teaching you at University?
        """
        menu:
            "I finished University...":
                m """
                Oh, really...?

                I...

                I didn't knew at all...

                I was sure this was your second year.

                Well, that's funny, it seems like my age is starting to show its effects!

                Don't worry, then.

                Maybe I'll call him now, you know?

                That would be wonderful!

                I haven't heard him for years.
                """
            "Uhmm...yes, of course.":
                m """
                Oh, that makes me so happy!

                He's always been such a good teacher...

                It was so funny when I discovered he was your teacher!

                I laughed for an entire day, remember?
                """
        m """
        Well, I think I'll call him, now...

        See you soon, ok?
        """
        menu:
            "Ok, see you.":
                m "And thank you..."
            "Bye.":
                m "Yes, bye."
    if phans == True:
        """
        There are no messages left.
        """
    hide phone
    with dissolve
    jump roomdownscreen3
label tv3:
    """
    On the screen there is a scene from a movie you barely remember.

    Three men are seated at a small table.

    They're discussing and laughing, lightly...

    Yet there's an aura of danger lingering around them.
    """
    jump roomdownscreen3
label cds3:
    """
    You take a CD from the pile.

    As you look at its cover you start to remember it.

    It was one of your favourites...

    But that was a long time ago.
    """
    jump roomdownscreen3
label toy3:
    if allowrep_choice == False:
        show teddybrok
        with dissolve
        """
        It just stays there, looking at you with a missing arm.
        """
        hide teddybrok
        with dissolve
    if allowrep_choice == True:
        show teddyrep
        with dissolve
        """
        It seems strangely happier now that its arm is fixed.
        """
        hide teddyrep
        with dissolve
    jump roomupscreen3
label mirror3:
    show mirror
    with dissolve
    if sofiatalk == False:
        """
        There's only you.
        """
        hide mirror
        with dissolve
        jump roomupscreen3
    if sofiatalk == True and mood >= 55 or mood <= 45:
        """
        The garden is waiting for you.

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
                jump roomupscreen3
label guit3:
    show guitar
    with dissolve
    """
    It stand silent in the corner.
    """
    if allowguit_choice == True:
        "Watching it reminds you of that melody..."
    hide guitar
    with dissolve
    jump roomupscreen3
label door3:
    "You can't get outside, it's tightly closed."
    jump roomdownscreen3

label computer3:
    if phans == False:
        "I should answer the phone."
        jump roomdownscreen3
    if phans == True and sofiatalk == False:
        jump sofianeut3
    if sofiatalk2 == True and mood >= 55:
        jump sofiagood3
    if sofiatalk2 == True and mood <= 45:
        jump sofiasad3

label sofiagood3:
    scene sofiah_a
    with slowfade
    """
    She's sleeping in front of the computer...

    She seems happy.
    """
    jump sofiagoodfade3
label sofiasad3:
    scene sofias_a
    with slowfade
    """
    She's sleeping in front of the computer...

    Looks like she's a little sad.
    """
    jump sofiasadfade3
label sofianeut3:
    scene sofian_a
    with slowfade
    $ sofiatalk = True
    $ nofeel = False
    """
    As you sit at the computer you notice that Sofia is there again, waiting for you.

    She's reading a book but you can't read the title.

    It surely is voluminous but she doesn't seem to mind that so much.
    """
    s """
    Oh, hi there!

    Sorry, I was just passing the time.

    How are you today?

    You seem so...sad.

    Did something happen?
    """
    menu:
        "My mother called...":
            """
            She seems surprised but happy.
            """
    s """
    Your mother?

    I haven't seen her in ages!

    How is she doing?

    Is everything alright?
    """
    menu:
        "I think she lost her memory.":
            s """
            Oh...

            Well, yeah...

            It's been quite some time since she started losing it.

            She suffers from an illness...

            I didn't know if it was alright to tell you this or not.

            I'm sorry...
            """
            menu:
                "Maybe I suffer from it too?":
                    $ mood += 5
                    s """
                    No, II don't think so...

                    She still remembers things, sometimes.

                    You're different...

                    You lost everything in the blink of an eye.

                    And you're slowly finding and putting the pieces together.

                    But she...

                    I think she won't be able to do that.
                    """
                "How...should I feel?":
                    $ mood -= 5
                    s """
                    W-what...do you mean?
                    """
                    menu:
                        "Should I hate myself...":
                            menu:
                                "For not feeling anything?":
                                    $ nofeel = True
                                    s """
                                    I don't think you should...

                                    It's not your fault if...

                                    If you can't remember her and if you can't feel anything about her.

                                    It really is not your fault.

                                    So don't blame yourself...

                                    Please...
                                    """
                        "I don't even remember her.":
                            s """
                            I imagined that...

                            But there's not so much you can do, for now.

                            You're locked in your own loss, so all you can do is trying to escape from it.

                            I think that when you'll get out of this everything will be better...
                            """
    s """
    Talking about memories...

    Did you managed to remember something?
    """
    menu:
        "I saw an...old friend.":
            """
            Wait!

            You mean...

            In your apartment, or...?
            """
    menu:
        "No, I saw him in my memories.":
            $ mood += 5
            s """
            In your memories...

            So they really are coming back, piece by piece!

            That makes me so happy...!
            """
        "No, it happened through the mirror.":
            $ mood -= 5
            s """
            Through the mirror?

            Do you mean that you...passed through the mirror?

            Doesn't that seem a little...impossible, to you?

            Do you really think something like that was real?
            """
            menu:
                "It's the only thing I can do.":
                    s """
                    Wait, what...

                    What do you mean by that?

                    That you have no other choice but to believe in something like that?

                    Something so absurd?

                    Do you think this is all a dream?

                    Something that is only happening in your head?

                    And then...

                    What am I?

                    Only a projection of yourself?

                    Or a ghost stucked in your head?

                    Is this what you...

                    Oh...

                    I-I'm sorry.

                    I didn't wanted to get so angry, it's just that I...
                    """
                    menu:
                        "Just believe in me...":
                            s """
                            I-I can do that, yes.
                            """
                        "It's understandable.":
                            s """
                            Thank you...
                            """
    s """
    And...well, what do you remember about him?
    """
    menu:
        "We spent time in a garden." if place:
            pass
            s """
            Well I don't know many gardens, but you often tolked about one.

            I remember it being very tiny, filled with different plants.

            You used to spend many time in there.

            It was nice hearing you talk about it.

            I always let my mind flew to imagine it.
            """
        "He spoke about a melody." if melody:
            pass
            s """
            A melody...

            You indeed used to sing a melody all the time, when we were together.

            So now you remember about it?

            it reminds me of so many things...

            Mostly of time passing too quickly and our laughs.
            """
        "It's still all blurred...":
            s """
            Well I guess that's the main topic in this story, huh?

            You must be tired of that...

            But after all we have just started, so don't worry!

            I'm sure things will get better!
            """
    s """
    Hmm but you know...

    I'm still not so sure about all this.

    So I think it's better to wait and see if you'll remember more!

    And sorry, but...now I'm a bit tired.

    We can talk more later, ok?

    Bye!
    """
    scene roomd_aft
    with slowfade
    jump roomdownscreen3

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################                S T A R T  D A Y 2  G H O S T S #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
label day2ghost:
    stop music fadeout (3)
    scene roomd_ghosts
    with slowfade
    play music "roomg_bgm.ogg" fadein (3)
    $ mood = 50
    $ sofiatalk = False
    $ sofiatalk2 = False
    $ sofia = 5
    """
    An unknown time of the day.

    You wake up, but...

    Is this still your apartment?

    It's identical.

    But what are those shadows on the walls?
    """
    jump roomdownscreen1g

label sofiagoodfade1g:
    scene sofiah_d
    $ renpy.pause(0.5)
    scene roomd_ghosts
    with fade
    $ renpy.pause(1)
    jump roomdownscreen1g
label sofiasadfade1g:
    scene sofias_d
    $ renpy.pause(0.5)
    scene roomd_ghosts
    with fade
    $ renpy.pause(1)
    jump roomdownscreen1g
label sofianeutfade1g:
    scene sofian_d
    $ renpy.pause(0.5)
    scene roomd_ghosts
    with fade
    $ renpy.pause(1)
    jump roomdownscreen1g

label roomdown1g:
    scene roomu_ghosts
    $ renpy.pause(0.5)
    scene roomd_ghosts
    with fade
    $ renpy.pause(1)
    jump roomdownscreen1g
label roomdownscreen1g:
    scene roomd_ghosts
    call screen roomdownscreen1g

label roomup1g:
    scene roomd_ghosts
    $ renpy.pause(0.5)
    scene roomu_ghosts
    with fade
    $ renpy.pause(1)
    jump roomupscreen1g
label roomupscreen1g:
    scene roomu_ghosts
    call screen roomupscreen1g
label window1g:
    """
    As you try to look outside the window...

    You can't see anything.

    Everything is surrounded by fog.
    """
    jump roomdownscreen1g
label bed1g:
    """
    You are not tired, now.
    """
    jump roomupscreen1g
label books1g:
    show books
    with dissolve
    """
    aaa
    """
    hide books
    with dissolve
    jump roomdownscreen1g
label plant1g:
    show plantb
    with dissolve
    """
    They look so...

    Colorless.
    """
    hide plantb
    with dissolve
    jump roomdownscreen1g
label trash1g:
    show trash
    with dissolve
    """
    The usual trash bin.
    """
    hide trash
    with dissolve
    jump roomdownscreen1g
label phone1g:
    show phone
    with dissolve
    """
    Nobody has called.
    """
    hide phone
    with dissolve
    jump roomdownscreen1g
label tv1g:
    """
    Only a pale screen.
    """
    jump roomdownscreen1g
label cds1g:
    """
    You don't feel like looking at the titles.
    """
    jump roomdownscreen1g
label toy1g:
    if allowrep_choice == False:
        show teddybrok
        with dissolve
        """
        Why haven't you fixed it?
        """
        hide teddybrok
        with dissolve
        jump roomupscreen1g
    if allowrep_choice == True:
        show teddyrep
        with dissolve
        """
        Is it watching at you?
        """
        hide teddyrep
        with dissolve
        jump roomupscreen1g
label mirror1g:
    show mirrorb
    with dissolve
    if sofiatalk == False:
        """
        There's a pale shadow on it.
        """
        hide mirrorb
        with dissolve
        jump roomupscreen1g
    if sofiatalk2 == True and mood >= 55 or mood <= 45:
        """
        The garden is inviting you.

        Do you go through the mirror?
        """
        menu:
            "Yes.":
                hide mirrorb
                with dissolve
                jump memories2
            "Not now.":
                hide mirrorb
                with dissolve
                jump roomupscreen1g
label guit1g:
    show guitarb
    with dissolve
    """
    You have no desire to play it.
    """
    hide guitarb
    with dissolve
    jump roomupscreen1g
label door1g:
    "You can't get outside, it's tightly closed."
    jump roomdownscreen1g

label computer1g:
    if sofiatalk == False:
        jump sofianeut1g
    if sofiatalk2 == True and mood >= 55:
        jump sofiagood1g
    if sofiatalk2 == True and mood <= 45:
        jump sofiasad1g
    if sofia >= 6 and guit == False:
        "Looks like she'll be occupied for some time."
        jump roomdownscreen1g
    if sofia <= 4 and toy == False:
        "Looks like she'll be occupied for some time."
        jump roomdownscreen1g

label sofiagood1g:
    scene sofiah_d
    with slowfade
    s """
    It's nice seeing you smiling like this, you know?
    """
    jump sofiagoodfade1g
label sofiasad1g:
    scene sofias_d
    with slowfade
    s """
    Is it me or you seem a little down?
    """
    jump sofiasadfade1g
label sofianeut1g:
    scene sofias_d
    with slowfade
    $ sofiatalk = True
    $ acceptance = False
    $ nolove = False
    """
    Sofia is right there, on the screen.

    She's waiting for you, as always.

    She's reading from a voluminous book which title you can't read.

    She lifts her head, watching you with a large smile.

    But she instantly becomes worried.
    """
    menu:
        "You're still here?":
            $ mood += 5
            s """
            Yes.

            I told you, didn't I?

            That I would always be here for you, no matter what.
            """
            menu:
                "I was afraid you'd leave me.":
                    $ mood += 5
                    s """
                    Oh...

                    I would never do that!

                    You're too much important form e to abandon you...

                    You're the only person I have left.

                    Without you I would...

                    I would be completely alone.

                    And loneliness makes everything so dark and sad.

                    All the colours fade away in an instant.

                    And then only darkness remains.
                    """
                "I'm still confused about this.":
                    $ mood -= 5
                    s """
                    I do understand that...

                    I know it's difficult to trust so simply a complete stranger.

                    Or, at least, someone that is now a complete stranger.

                    I do not know what I can do to convince you that I'm sincere, but...

                    For now I can wait for you to retrieve your memories, at least.

                    And I'll try to help you.
                    """
        "Don't you have things to do?":
            $ mood -= 5
            s """
            Oh...

            Well, normally I would.

            But not now, so...

            Waiting for you is the only thing I have to do.
            """
            menu:
                "I still don't get why.":
                    $ mood -= 5
                    s """
                    You don't?

                    Well...

                    How can I say that...

                    I think it's easy to understand why...if you think about it carefully.

                    Please just try to understand.

                    Because it's a little embarassing to say that.

                    For me, at least.

                    And especially now that you barely know who I am.
                    """
                "Am I so important?":
                    $ mood += 5
                    s """
                    Uhmm well...

                    Yes, you are.

                    Does it surprise you that much?

                    I know the feeling of not being so much important for anyone, but...

                    For me you are the most important person.

                    I wouldn't be able to do anything without you...
                    """
    s """
    I know this will sound stupid, but I want to be sincere.

    It's so difficult to say this, but...

    Normally I would be at the university, now.

    All this situation may seem creepy, I know.

    A girl you barely know talking to you through a computer...

    And all this thing about your memory.

    It's difficult to believe all this, right?

    But the thing is that I've been so in love with you, in the past...

    And I still am.

    That's why I'm here.

    That's why I've abandoned everything for you.

    Those feelings are so strong that I cry every time I think about this.

    And I can't help but asking myself why did we get in this situation.

    What have we done to deserve this...
    """
    menu:
        "I'm sorry for doubting.":
            $ mood += 5
            $ acceptance = True
            s """
            Thank you...

            That makes me feel a little better.
            """
        "I understand...":
            $ mood -= 5
            $ nolove = True
            s """
            You know...

            You have no obligations.

            At all.

            You don't have to love me.

            The only thing I want is for you to be happy and feel better.

            I don't want to see you get lost...
            """
    s """
    I'm sorry...

    I'm sorry for being like this.

    I know I'm not strong and I can't fake it.

    I tried but probably I've only made things worst.

    You probably thought I was a creepy and suspicious girl...

    The truth is that I wanted to show you a better side of me.

    A side that often doesn't exist.

    I'm so sorry...

    Anyway, this is taking too much from me, so...

    Let's change argument, ok?

    I'm sorry but I really can't go on with it.

    Not now, at least.

    So, I...

    I was waiting for you, but...

    You look so...strange?

    I mean, not for what I said, but...

    Even before.

    What happened?
    """
    menu:
        "I've seen a man...":
            s """
            A man?

            What do you mean?

            Someone entered in your apartment?
            """
            menu:
                "I think it was a memory.":
                    s """
                    A memory...?

                    Well, I guess it's possible...

                    Maybe you're getting flashes of your past?

                    And those flashes help you to retrieve your entire memory piece by piece.

                    Well, I think that's a good thing, isn't it?

                    And what have you remembered of him?
                    """
                    menu:
                        "He was scary...":
                            s """
                            Scary?

                            Well, I guess it wasn't a pleasant memory, then...

                            But whatever happened, I think it helped you, didn't it?

                            At least now you are more sure about what surrounds you.

                            And what happened in the past, even if only a little more than before.

                            So...

                            Well, I think it'd be better if I go rest for some time, ok?

                            I'm feeling tired, now.

                            Forgive me if I go away so suddenly but...

                            I think you'd agree on the fact that today has been a hard day.

                            We'll talk more later or tomorrow...bye.
                            """
                        "He said I'm nobody.":
                            menu:
                                "As I have no memory.":
                                    s """
                                    I do get the point, but...

                                    Your memories are not lost forever.

                                    You're slowly finding them.

                                    And as long as there is your apartment and all the people you had around...

                                    You are still someone.

                                    At least for me, you are still someone.

                                    Anyway, I...I feel a bit tired, now.

                                    Do you mind if I rest for a bit?

                                    We'll talk more later or...tomorrow.

                                    Bye.
                                    """
                "No, it was through the mirror.":
                    s """
                    The mirror...?

                    Are you...

                    Are you serious?

                    I mean, I know I told you to believe in me, so...

                    Of course I'll believe you, but this...

                    Don't you think it's a bit too much?

                    Are you playing with me?
                    """
                    menu:
                        "I would never!":
                            s """
                            Yeah, I...

                            I'm sorry, it's just difficult.

                            Can you give me some time to think?

                            I'm sorry, I tried to go on with the conversation, but this...

                            This is too difficult.

                            At least for now.

                            We'll talk more tomorrow, ok?

                            Il'' go rest a little, now...bye.
                            """
                        "So you don't believe me...":
                            s """
                            Listen, I...

                            I think we should both rest, now.

                            I think you're still tired and confused.

                            And I'm not capable of thinking straight, now.

                            We...

                            We'll talk more tomorrow.

                            Bye...
                            """
    scene roomd_ghosts
    with slowfade
    jump roomdownscreen1g

label memories2:
    if mood <= 45:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        play movie "trauma1.ogv" loop
        show movie with slowfade
        play music "trauma_bgm.ogg" fadein (3)
        $ trauma += 1
        $ menth += 1
        """
        bad memoryyyy
        """
        stop music fadeout (3)
        jump night1
    if mood >= 55:
        stop music fadeout (2)
        scene black
        with slowfade
        $ renpy.pause(1.5)
        scene mem1
        with slowfade
        play music "mem_bgm.ogg" fadein (3)
        $ mem += 1
        """
        good memoryyyy
        """
        stop music fadeout (3)
        jump night2

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################                            S E C O N D   N I G H T   P A S S A G E #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label night2:
    stop movie
    hide movie with slowfade
    scene roomd_night
    with slowfade
    play music "roomn_bgm.ogg" fadein (3)
    """
    aaa
    """
    jump roomdownscreenn2

label roomdownn2:
    scene roomu_night
    $ renpy.pause(0.5)
    scene roomd_night
    with fade
    $ renpy.pause(1)
    jump roomdownscreenn2
label roomdownscreenn2:
    scene roomd_night
    call screen nightscreendown2

label roomupn2:
    scene roomd_night
    $ renpy.pause(0.5)
    scene roomu_night
    with fade
    $ renpy.pause(1)
    jump roomupscreenn2
label roomupscreenn2:
    scene roomu_night
    call screen nightscreenup2
label windown2:
    """
    Outside the window the streets look solitary.

    There's no one around.

    And the moon is high and pale.

    It seems to be watching you.
    """
    jump roomdownscreenn2
label bedn2:
    """
    You feel so tired...

    Do you want to sleep?
    """
    menu:
        "Yes.":
            "As you get in the bed, your eyes instantly close."
            stop music fadeout (3)
            jump narrator2
        "No.":
            "Maybe later"
            jump roomupscreenn2
label booksn2:
    """
    You're too tired to read now.
    """
    jump roomdownscreenn2
label plantn2:
    show plant
    with dissolve
    """
    The plant seems melancholic with this light.
    """
    hide plant
    with dissolve
    jump roomdownscreenn2
label trashn2:
    show trash
    with dissolve
    """
    The usual trash bin.
    """
    hide trash
    with dissolve
    jump roomdownscreenn2
label phonen2:
    show phone
    with dissolve
    """
    No messages left on the answering service.
    """
    hide phone
    with dissolve
    jump roomdownscreenn2
label tvn2:
    """
    It's turned off.
    """
    jump roomdownscreenn2
label cdsn2:
    """
    Ever wandered what would happen if these CDs fell?
    """
    jump roomdownscreenn2
label toyn2:
    show teddybrok
    with dissolve
    """
    It's as if it is smiling at you.
    """
    hide teddybrok
    with dissolve
    jump roomupscreenn2
label mirrorn2:
    show mirror
    with dissolve
    """
    There is only you, now.
    """
    hide mirror
    with dissolve
    jump roomupscreenn2
label guitn2:
    show guitar
    with dissolve
    """
    It's too late to play it.
    """
    hide guitar
    with dissolve
    jump roomupscreenn2
label doorn2:
    "I can't get outside, it's tightly closed."
    jump roomdownscreenn2

label computern2:
    """
    She's sleeping.

    It's better to not disturb her.
    """
    jump roomdownscreenn2

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 3 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator2:
    scene narrator
    with slowfade
    play music "narr_bgm.ogg" fadein (3)
    """
    aaa
    """
    if guilt == False:
        jump day3
    if guilt == True:
        jump day3ghost

    stop music fadeout (3)
    scene black
    with slowfade
    return
