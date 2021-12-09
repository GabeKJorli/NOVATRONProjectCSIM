def on_button_pressed_ab():
    for index in range(4):
        music.play_tone(988, music.beat(BeatFraction.HALF))
        basic.show_icon(IconNames.SQUARE)
        music.play_tone(988, music.beat(BeatFraction.HALF))
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play_tone(988, music.beat(BeatFraction.HALF))
        basic.show_icon(IconNames.SQUARE)
        music.play_tone(988, music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

basic.show_string("NOVATRON")

def on_forever():
    if input.light_level() <= 50:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    if input.light_level() >= 51:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
