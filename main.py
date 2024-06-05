import machine
import time

btn_amarelo = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP) # amarelo
btn_verde = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP) # verde
btn_azul = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP) # azul
btn_preto = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP) # preto

led_amarelo = machine.Pin(27, machine.Pin.OUT)
led_verde = machine.Pin(26, machine.Pin.OUT)
led_azul = machine.Pin(25, machine.Pin.OUT)

buzz = machine.Pin(4, machine.Pin.OUT)
buzzer = machine.PWM(buzz)
buzzer.freq(10)
buzzer.duty(512)
time.sleep(0.1)
buzzer.duty(0)

# Musica MarioBros
notes = [
    659, 659, 0, 659, 0, 523, 659, 0, 784, 0, 392, 0,
    523, 0, 392, 0, 330, 0, 440, 494, 466, 440, 392,
    659, 784, 880, 0, 698, 784, 659, 0, 523, 587, 494,
    0, 523, 392, 330, 440, 494, 466, 440, 392, 659, 784, 880,
    0, 698, 784, 659, 0, 523, 587, 494
]
durations = [
    150, 150, 150, 150, 150, 150, 150, 150, 300, 150, 150, 150,
    150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 300,
    150, 150, 150, 150, 150, 150, 300, 150, 150, 150,
    150, 150, 150, 150, 150, 150, 150, 150, 300, 150, 150, 150,
    150, 150, 150, 300, 150, 150, 150, 150
]

def musica_mario(buzzer, freq, duration):
    if freq == 0:
        buzzer.duty(0)
    else:
        buzzer.freq(freq)
        buzzer.duty(512)
    time.sleep(duration / 1000)
    buzzer.duty(0)
    time.sleep(0.05)

while True:
    if btn_amarelo.value() == 0:
        led_azul.value(0)
        led_verde.value(0)
        led_amarelo.value(1)

        buzzer.freq(900)
        buzzer.duty(512)
        time.sleep(0.2)
        buzzer.duty(0)
        print("ok - 1")

    if btn_verde.value() == 0:
        led_azul.value(0)
        led_verde.value(1)
        led_amarelo.value(0)

        buzzer.freq(600)
        buzzer.duty(512)
        time.sleep(0.2)
        buzzer.duty(0)
        print("ok - 2")

    if btn_azul.value() == 0:
        led_azul.value(1)
        led_verde.value(0)
        led_amarelo.value(0)

        buzzer.freq(300)
        buzzer.duty(512)
        time.sleep(0.2)
        buzzer.duty(0)
        print("ok - 3")
    
    if btn_preto.value() == 0:
        for i in range(len(notes)-1):
            musica_mario(buzzer, notes[i], durations[i])
            print("oi")
    
    time.sleep(0.1)
