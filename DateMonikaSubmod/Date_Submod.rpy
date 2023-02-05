#Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Wilt3r",
        name="Take Monika On A Date BETA",
        description="Adds a button to take Monika on a date here in the game!",
        version="2023.205.0"
    )

#Adds the Dates option
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="pick_date",category=['Dates'],prompt="Let's go on a date",pool=True,unlocked=True))

#New topic! (new year)
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="newyearfireworks",
            prompt="It's 2023!",
            category=["misc"],
            start_date=datetime.date(2023, 1, 1),
            end_date=datetime.date(2023, 2, 10),
            aff_range=(mas_aff.NORMAL, mas_aff.LOVE),
            action=EV_ACT_PUSH
        )
    )

#New years dialouge
label newyearfireworks:
    m 1eub "Hey [player]! "
    extend 1sub "Happy New Year!"
    m 3hub "It's 2023 now, I'm glad we got to spend time during new years!"
    m 1dsd "Speaking of new years... "
    extend 3sub "do you have fireworks at your place, [player]?"
    m 2lkblb "Honestly speaking, it'd be great for us to watch the fireworks while going on a date, right?"
    m 5dkbsb "I really wish we could do that together, shoulders touching, holding hands and all..."
    m 5dkbfa ".{w=0.4}.{w=0.4}.{w=0.4}.{nw}"
    m 5kkblb "I'm just really glad to be spending time with you this year right now, "
    extend 7rublb "I'm sure we will be able to watch the blazing fireworks when I come to your reality!"
    m 1fublb "If you'd like, we could go on a date right now~ hehe!"
    m 1hubsb "Happy New Year, [player]! I love you~"
    return

#Choose where to go for the date
label pick_date:
    m 1sublb "We're going on a date?"
    m 3hub "Sounds exciting~!"
    m 1eua "Where do you want to go for our date?{nw}"

    menu:
        m "Where do you want to go for our date?{fast}"

        "Cafe":
              play sound "Submods/DateMonikaSubmod/music/notice.mp3"
              call screen dialog(message="Error: Script file is missing or corrupt.\nPlease check or reinstall the Submod.\n\nError Code:29563180", ok_action=Return())
              return

        "Park":
              window hide
              show black zorder 100 with Dissolve(5.0, alpha=True)
              call park

        "Beach":
               window hide
               show black zorder 100 with Dissolve(5.0, aplha=True)
               call beach

        "Nevermind":
                   m 1eka "Oh, alright."
                   return


#Defenitions
image cafe = "Submods/DateMonikaSubmod/images/cafe.png"
image cafemenu = "Submods/DateMonikaSubmod/images/cafemenu.png"
image cafetable = "Submods/DateMonikaSubmod/images/cafetable.png"

image park = "Submods/DateMonikaSubmod/images/park.png"
image park2 = "Submods/DateMonikaSubmod/images/park2.png"
image park3 = "Submods/DateMonikaSubmod/images/park3.png"
image park4 = "Submods/DateMonikaSubmod/images/park4.png"
image park5 = "Submods/DateMonikaSubmod/images/park5.png"
image park_lake = "Submods/DateMonikaSubmod/images/park-lake.png"
image forest = "Submods/DateMonikaSubmod/images/forest.png"

image beach = "Submods/DateMonikaSubmod/images/beach.png"


#Sprites
image monika 1a_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/a.png")
image monika 1b_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/b.png")
image monika 1c_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/c.png")
image monika 1d_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/d.png")
image monika 1e_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/e.png")
image monika 1f_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/f.png")
image monika 1g_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/g.png")
image monika 1h_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/h.png")
image monika 1i_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/i.png")
image monika 1j_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/j.png")
image monika 1k_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/k.png")
image monika 1l_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/l.png")
image monika 1m_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/m.png")
image monika 1n_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/n.png")
image monika 1o_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/o.png")
image monika 1p_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/p.png")
image monika 1q_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/q.png")
image monika 1r_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/r.png")

image monika 2a_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/a.png")
image monika 2b_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/b.png")
image monika 2c_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/c.png")
image monika 2d_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/d.png")
image monika 2e_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/e.png")
image monika 2f_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/f.png")
image monika 2g_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/g.png")
image monika 2h_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/h.png")
image monika 2i_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/i.png")
image monika 2j_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/j.png")
image monika 2k_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/k.png")
image monika 2l_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/l.png")
image monika 2m_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/m.png")
image monika 2n_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/n.png")
image monika 2o_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/o.png")
image monika 2p_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/p.png")
image monika 2q_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/q.png")
image monika 2r_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/1l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/r.png")

image monika 3a_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/a.png")
image monika 3b_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/b.png")
image monika 3c_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/c.png")
image monika 3d_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/d.png")
image monika 3e_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/e.png")
image monika 3f_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/f.png")
image monika 3g_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/g.png")
image monika 3h_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/h.png")
image monika 3i_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/i.png")
image monika 3j_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/j.png")
image monika 3k_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/k.png")
image monika 3l_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/l.png")
image monika 3m_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/m.png")
image monika 3n_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/n.png")
image monika 3o_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/o.png")
image monika 3p_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/p.png")
image monika 3q_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/q.png")
image monika 3r_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/1r.png", (0, 0), "monika/r.png")

image monika 4a_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/a.png")
image monika 4b_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/b.png")
image monika 4c_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/c.png")
image monika 4d_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/d.png")
image monika 4e_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/e.png")
image monika 4f_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/f.png")
image monika 4g_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/g.png")
image monika 4h_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/h.png")
image monika 4i_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/i.png")
image monika 4j_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/j.png")
image monika 4k_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/k.png")
image monika 4l_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/l.png")
image monika 4m_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/m.png")
image monika 4n_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/n.png")
image monika 4o_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/o.png")
image monika 4p_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/p.png")
image monika 4q_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/q.png")
image monika 4r_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/2l.png", (0, 0), "Submods/DateMonikaSubmod/images/monika/2r.png", (0, 0), "monika/r.png")

image monika 5a_tmoad = im.Composite((960, 960), (0, 0), "Submods/DateMonikaSubmod/images/monika/3a.png")

#TODO: Finish the cafe date and release it somewhere in 2023. If I have motivation to do so.
#The Cafe Date
#label cafe:
#    $HKBHideButtons()
#    stop music
#    play music "<loop 4.444>bgm/5_monika.ogg" fadein 2
#    $ morning_flag = False
#    $ prev_flt = store.mas_sprites.get_filter()
#    $ store.mas_sprites.set_filter(store.mas_sprites.FLT_NIGHT)
#    hide black
#    scene cafe
#    $ is_sitting = False
#    show monika 4hub_static at t11
#    $ amongusoption = True
#    m "We're here~!"
#    m 1eua_static "It's so nice of you to take me on a date."
#
#    menu:
#        "You're welcome":
#                        pass
#
#        "Because I love you~":
#                             pass
#
#    m 2eub "Now c'mon, let's go to our table."
#    scene cafetable with wipeleft_scene
#    $ is_sitting = True
#    show monika 1euc at t11
#    pause 2
#    m 1eub "Oh look,{w=1} our menu's are already here."
#    m 3hub "What great customer service this restaurant have!"
#label amongusoptionisnowdisable:
#    hide black
#    m 1eua "So,{w=1} what are you getting?"
#    play audio page_turn
#    show cafemenu zorder 11 with Dissolve(1.0, alpha=True)
#    pause 2
#    m "These choices are....{w} {i}Intresting{/i}."
#
#label CafeMenu:
#    menu:
#        "Salad":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "A Salad appeared on the table."
#               "The Salad consist of,{w=0.30} well what you normally put on a salad."
#               "Vegetables and stuff."
#               "It also comes with soda."
#               m 1eua "You picked a Salad."
#               m 3hub "Great choice!"
#               m 7eub "Did you know Salad comes from the Latin word {i}herba salta{/i} or {i}salted herbs,{/i} so called because such greens were usually seasoned with dressings containing lots of salt."
#               m 2tuu "Bet you didn't know that."
#               m 2etc "Or you probably did."
#               m 1hua "Anyway, now I'm going to pick..."
#               pause 2
#               m 1hub "Coffee!"
#               pass
#
#        "Bread":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "Bread appeared on the table."
#               "The Bread consist of bread."
#               "It also comes with coffee."
#               m 1eua "You picked Bread."
#               m 3hub "Great choice!"
#               m 1hua "Now I'm going to pick..."
#               pass
#
#        "Among Us Meal" if amongusoption:
#                       $ amongusoption = False
#                       show monika 1euc
#                       play audio page_turn
#                       hide cafemenu with Dissolve(1.0, alpha=True)
#                       "{i}An Among Us Meal appeared on the table.{/i}"
#                       "{i}The Among Us Meal consist of a salad shape as a crewmate.{/i}"
#                       "{i}5 chicken nuggets at the side also shape as crewmates.{/i}"
#                       "{i}And a soda named {b}Sus Juice{/b}.{/i}"
#                       stop music
#                       show noise zorder 3 at noisefade(5):
#                           alpha 1.0
#                       show vignette zorder 3 at vignettefade(2):
#                           alpha 1.0
#                       m 6efd "Is that a Among Us Meal."
#                       menu:
#                           "Yes":
#                                 pass
#                       m 2dsc "An Among Us Meal..."
#                       pause 2
#                       show screen tear(20, 0.1, 0.1, 0, 40)
#                       play sound "sfx/s_kill_glitch1.ogg"
#                       pause 0.25
#                       hide screen tear
#                       m "You got..."
#                       pause 2
#                       m 2cub "An amogus meal-{nw}"
#                       show screen tear(20, 0.1, 0.1, 0, 40)
#                       play sound "sfx/s_kill_glitch1.ogg"
#                       pause 0.25
#                       hide screen tear
#                       show black zorder 11
#                       hide vignette
#                       hide noise
#                       pause 5
#                       $ renpy.movie_cutscene("Submods/DateMonikaSubmod/")
#                       pause 2
#                       play music "<loop 4.444>bgm/5_monika.ogg"
#                       jump amongusoptionisnowdisable
#                       jump cafe_end
#
#        "Coffee":
#                show monika 1euc zorder MAS_MONIKA_Z
#                play audio page_turn
#                hide cafemenu with Dissolve(1.0, alpha=True)
#                "Coffee appeared on the table."
#                m 1eua "You picked Coffee."
#                m 3hub "Great choice!"
#                m 1hua "Now I'm going to pick..."
#                pass
#
#        "Dark Coffee":
#                     show monika 1euc zorder MAS_MONIKA_Z
#                     play audio page_turn
#                     hide cafemenu with Dissolve(1.0, alpha=True)
#                     "Dark Coffee appeared on the table."
#                     m 1eua "You picked Dark Coffee."
#                     m 3hub "Great choice!"
#                     m 1hua "Now I'm going to pick..."
#                     pass
#
#        "White Coffee":
#                      show monika 1euc zorder MAS_MONIKA_Z
#                      play audio page_turn
#                      hide cafemenu with Dissolve(1.0, alpha=True)
#                      "White Coffee appeared on the table."
#                      m 1eua "You picked White Coffee."
#                      m 3hub "Great choice!"
#                      m 1hua "Now I'm going to pick..."
#                      pass
#
#        "Fries":
#               show monika 1euc zorder MAS_MONIKA_Z
#               play audio page_turn
#               hide cafemenu with Dissolve(1.0, alpha=True)
#               "Fries appeared on the table."
#               "The Fries consist of potatos."
#               "It also comes with a soda."
#               m 1eua "You picked Fries."
#               m 3hub "Great choice!"
#               m 1hua "Now I'm going to pick..."
#               pass
#
#        "{b}{i}NEXT{/i}{/b}":
#                     menu:
#                         "Mint Ice Cream":
#                                         show monika 1euc zorder MAS_MONIKA_Z
#                                         play audio page_turn
#                                         hide cafemenu with Dissolve(1.0, alpha=True)
#                                         "Mint Ice Cream appeared on the table."
#                                         m 1eua "You picked Mint Ice Cream."
#                                         m 3hub "Great choice!"
#                                         m 1hua "Now I'm going to pick..."
#                                         pass
#
#                         "Chocolate Ice Cream":
#                                              show monika 1euc zorder MAS_MONIKA_Z
#                                              play audio page_turn
#                                              hide cafemenu with Dissolve(1.0, alpha=True)
#                                              "Chocolate Ice Cream appeared on the table."
#                                              m 1eua "You picked Chocolate Ice Cream."
#                                              m 3hub "Great choice!"
#                                              m 1hua "Now I'm going to pick..."
#                                              pass
#
#                         "Vanilla Ice Cream":
#                                           show monika 1euc zorder MAS_MONIKA_Z
#                                          play audio page_turn
#                                            hide cafemenu with Dissolve(1.0, alpha=True)
#                                            "Vanilla Ice Cream appeared on the table."
#                                            m 1eua "You picked Vanilla Ice Cream."
#                                            m 3hub "Great choice!"
#                                            m 1hua "Now I'm going to pick..."
#                                            pass
#
#                         "Milk":
#                               show monika 1euc zorder MAS_MONIKA_Z
#                               play audio page_turn
#                               hide cafemenu with Dissolve(1.0, alpha=True)
#                               "Milk appeared on the table."
#                               m 1eua "You picked Milk."
#                               m 3hub "Great choice!"
#                               m 1hua "Now I'm going to pick..."
#                               pass
#
#                         "Chocolate Milk":
#                                         show monika 1euc zorder MAS_MONIKA_Z
#                                         play audio page_turn
#                                         hide cafemenu with Dissolve(1.0, alpha=True)
#                                         "Chocolate Milk appeared on the table."
#                                         m 1eua "You picked Chocolate Milk."
#                                         m 3hub "Great choice!"
#                                         m 1hua "Now I'm going to pick..."
#                                         pass
#
#                         "{b}{i}PREVIOUS{/i}{/b}":
#                                          jump CafeMenu
#
#label cafe_end:
#
#    show black zorder 11 with Dissolve(5.0, alpha=True)
#    pause 2
#    scene cafe
#    hide black with Dissolve(5.0, alpha=True)
#    $ is_sitting = False
#    show monika 4hub at t11
#    m "That was great!"
#    m 1eka "I want to thank you for taking me on this date, [mas_get_player_nickname()]."
#    m 1hua "I hope you can take me on a date again soon~"
#    m 1hub "I love you so much, [player]!"
#    show black zorder 11 with Dissolve(5.0, alpha=True)
#    stop music fadeout 2
#    hide monika
#    pause 2
#    $HKBShowButtons()
#    $ morning_flag = True
#    $ prev_flt = store.mas_sprites.get_filter()
#    $ store.mas_sprites.set_filter(store.mas_sprites.FLT_DAY)
#    $ play_song(persistent.current_track, fadein=4.0)
#    hide black
#    $mas_HKBDropShield()
#    $ is_sitting = True
#
#    jump ch30_loop
