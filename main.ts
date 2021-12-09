input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        music.playTone(988, music.beat(BeatFraction.Half))
        basic.showIcon(IconNames.Square)
        music.playTone(988, music.beat(BeatFraction.Half))
        basic.showIcon(IconNames.SmallSquare)
        music.playTone(988, music.beat(BeatFraction.Half))
        basic.showIcon(IconNames.Square)
        music.playTone(988, music.beat(BeatFraction.Half))
    }
})
basic.showString("NOVATRON")
basic.forever(function () {
    if (input.lightLevel() <= 50) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (input.lightLevel() >= 51) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
