/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 24 2024
 * This program mauseres the disance in sonar 
*/

// Setting the veribles 
let distanceToObject: number = 0
let distance = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)


// Setting the program
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Setting ligths 
distance.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
distance.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
distance.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
distance.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))

// Setting the sonar 
distanceToObject = sonar.ping(
    DigitalPin.P1
    ,DigitalPin.P2
    ,PingUnit.Centimeters
)

input.onButtonPressed(Button.A,function(){
    if (distanceToObject > 10){
        distance.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        distance.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
        distance.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
        distance.setPixelColor(3, neopixel.colors(NeoPixelColors.Red))
    }
    else {
        distanceToObject < 10
        distance.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
        distance.setPixelColor(1, neopixel.colors(NeoPixelColors.Green))
        distance.setPixelColor(2, neopixel.colors(NeoPixelColors.Green))
        distance.setPixelColor(3, neopixel.colors(NeoPixelColors.Green))

    }
})