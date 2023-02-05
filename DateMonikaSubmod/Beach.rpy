#The Beach Date

init python:
    import webbrowser

label beach:
    $HKBHideButtons()
    stop music
    play music "Submods/DateMonikaSubmod/music/ddlcjazzimproved.ogg" #Temporary music lol
    hide black
    scene beach
    $ bench = True
    pause 0.75
    $ is_sitting = False
    show monika 3a_tmoad at t11

    #You can change this dialogue however you want, though please re-dialogue all of this as this is just temporary lol
    m "We're at the beach!"
    m 4b_tmoad "It's beautiful isn't it?"
    menu:
        "Yes it does.":
                       menu:
                            ":thumbsup:":
                                        pass

    m 4k_tmoad "How about we explore this place for a bit before we go for a swim hmmmm?"
    menu:
        ":thumbsup:":
                    pass
    
    jump beach_end


label beach_end:
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 2
    hide monika
    pause 2
    $HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $mas_HKBDropShield()
    $ is_sitting = True

    jump ch30_loop
