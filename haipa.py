import machine
import utime
import _thread
#import LEDDisplay

buzzer1 = machine.PWM(machine.Pin(18, machine.Pin.OUT))
buzzer2 = machine.PWM(machine.Pin(15, machine.Pin.OUT))
buzzer3 = machine.PWM(machine.Pin(10, machine.Pin.OUT))

tones = {
    "B0": 31,
    
    "C1": 33, "CS1": 35, "D1": 37, "DS1": 39,  "E1": 41, "F1": 44,
    "FS1": 46, "G1": 49, "GS1": 52, "A1": 55, "AS1": 58, "B1": 62,
    
    "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87,
    "FS2": 93, "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123,
    
    "C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175,
    "FS3": 185, "G3": 196, "GS3": 208, "A3": 220,  "AS3": 233, "B3": 247,
    
    "C4": 262, "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349,
    "FS4": 370, "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494,
    
    "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698,
    "FS5": 740, "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988,
    
    "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397,
    "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976,
    
    "C7": 2093, "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794,
    "FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951,
    
    "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978,
}

def playtone(frequency,target):
    target.duty_u16(1000)
    target.freq(frequency)

def bequiet(target):
    target.duty_u16(0)
    target.deinit()

def playsong(mysong1,mysong2,mysong3,dela,target1,target2,target3):
    for i in range(len(mysong1)):
        if (mysong1[i] == "P"):
            bequiet(target1)
        else:
            playtone(tones[mysong1[i]],target1)
        if (mysong2[i] == "P"):
            bequiet(target2)
        else:
            playtone(tones[mysong2[i]],target2)
        if (mysong3[i] == "P"):
            bequiet(target3)
        else:
            playtone(tones[mysong3[i]],target3)
        #Addtime()
        utime.sleep(dela)

N1=0
N2=0
N3=0
N4=1.0
def Addtime():
    global N1
    global N2
    global N3
    global N4
    N4 = N4+0.5
    if N4>=4.0:
        N4 = 1
        N2 = N2+1
    if N2>=10:
        N2 = 0
        N1 = N1+1
    #LEDDisplay.D2=True
    #LEDDisplay.N1=N1
    #LEDDisplay.N2=N2
    #LEDDisplay.N3=N3
    #LEDDisplay.N4=int(N4)




Track1 = [
    "A5","P","P","P","C6","E6",
    "C7","P","P","P","B6","P",
    "G6","P","P","P","D6","P",
    "E6","P","P","P","P","P",#1
    "E6","P","P","P","F6","G6",
    "F6","P","P","P","E6","P",
    "D6","P","P","P","C6","P",
    "E6","P","P","P","P","P",#2
    "A5","P","P","P","C6","E6",
    "C7","P","P","P","B6","P",
    "G6","P","P","P","D6","P",
    "E6","P","P","P","P","P",#3
    "E6","P","P","P","F6","G6",
    "F6","P","P","P","E6","P",
    "D6","P","P","P","C6","P",
    "E6","P","P","P","P","P",#4
    "A5","P","P","P","B5","C6",
    "C7","P","P","P","B6","P",
    "G6","P","P","P","D6","P",
    "E6","P","P","P","P","P",#5
    "E6","P","P","P","F6","G6",
    "F6","P","P","P","E6","P",
    "D6","P","P","P","C6","P",
    "E6","P","P","P","P","P",#6
    "A5","P","P","P","C6","E6",
    "C7","P","G5","P","B6","P",
    "G6","P","D6","C6","D6","A5",
    "E6","P","P","P","P","P",#7
    "E6","P","P","P","F6","G6",
    "F6","P","P","P","E6","P",
    "D6","P","P","P","C6","A5",
    "E6","P","P","P","P","P",#8--
    "P","P","B6","C7","B6","A6",
    "E6","P","C6","P","E6","P",
    "P","P","B6","C7","B6","A6",
    "D7","P","P","P","P","P",#9
    "P","P","B6","C7","B6","A6",
    "B6","P","P","P","C7","P",
    "G6","P","G6","F6","E6","F6",
    "E6","P","P","P","P","P",#10
    "P","P","E6","F6","E6","D6",
    "AS5","P","F5","P","F6","P",
    "E6","P","P","D6","C6","D6",
    "E6","P","P","P","C6","P",#11
    "DS6","P","B5","P","A5","P",
    "DS5","P","P","P","DS6","P",
    "E6","P","P","P","GS5","A5",
    "GS5","P","P","P","P","P",#12
    "P","P","B6","C7","B6","A6",
    "E6","P","C6","P","E6","P",
    "P","P","B6","C7","B6","A6",
    "D7","P","P","P","P","P",#13
    "P","P","B6","C7","B6","A6",
    "B6","P","P","P","B6","P",
    "G6","P","G6","F6","E6","F6",
    "E6","P","P","P","P","P",#14
    "P","P","E6","F6","E6","D6",
    "AS5","P","F5","P","F6","P",
    "E6","P","P","D6","C5","D6",
    "E6","P","P","P","C6","P",#15
    "DS6","P","B5","P","A5","P",
    "DS5","P","P","P","DS6","P",
    "E6","P","P","P","GS5","A5",
    "GS5","P","P","P","P","P",#16
    "P","P","P","P","P","P",
    ]

Track2 = [
    "A4","P","E5","P","E5","P",
    "A4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",#1
    "F4","P","C5","P","C5","P",
    "F4","P","C5","P","C5","P",
    "E4","P","B4","P","B4","P",
    "E4","P","B4","P","B4","P",#2
    "D4","P","A4","P","A4","P",
    "D4","P","A4","P","A4","P",
    "C4","P","G4","P","G4","P",
    "C4","P","G4","P","G4","P",#3
    "B3","P","F4","P","F4","P",
    "B3","P","F4","P","F4","P",
    "E4","P","A4","P","A4","P",
    "E4","P","GS4","P","GS4","P",#4
    "A4","P","E5","P","E5","P",
    "A4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",#5
    "F4","P","C5","P","C5","P",
    "F4","P","C5","P","C5","P",
    "E4","P","B4","P","B4","P",
    "E4","P","B4","C5","D5","B4",#6
    "D4","P","A4","P","F5","G5",
    "D4","P","A5","P","A4","P",
    "C4","P","G4","P","G4","P",
    "C4","P","G4","P","G4","P",#7
    "B3","P","F4","P","F4","P",
    "B3","P","F4","P","F4","P",
    "E4","P","A4","P","A4","P",
    "E4","P","GS4","P","GS4","P",#8--
    "A4","P","E5","P","E5","P",
    "A4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",#9
    "F4","P","E5","P","E5","P",
    "F4","P","C5","P","E5","P",
    "C5","P","G5","P","G5","P",
    "G5","F5","E5","F5","E5","D5",#10
    "AS4","P","D5","P","F5","P",
    "AS4","P","D5","P","F5","P",
    "A4","P","C5","P","E5","P",
    "A4","P","C5","P","E5","P",#11
    "B4","P","FS5","P","FS5","P",
    "B4","P","FS5","P","FS5","P",
    "E5","P","B5","P","B5","P",
    "E5","D5","C5","D5","C5","GS4",#12
    "A4","P","E5","P","E5","P",
    "A4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",
    "G4","P","E5","P","E5","P",#13
    "F4","P","E5","P","E5","P",
    "F4","P","C5","P","E5","P",
    "C5","P","G5","P","G5","P",
    "G5","F5","E5","F5","E5","D5",#14
    "AS4","P","D5","P","F5","P",
    "AS4","P","D5","P","F5","P",
    "A4","P","C5","P","E5","P",
    "A4","P","C5","P","E5","P",#15
    "B4","P","FS5","P","FS5","P",
    "B4","P","FS5","P","FS5","P",
    "E5","P","B5","P","B5","P",
    "E5","D5","C5","D5","C5","GS4",#16
    "A4","P","P","P","P","P",
    ]

Track3 = [
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",#1
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",#2
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",#3
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",#4
    "C5","P","P","P","P","P",
    "E6","P","P","P","P","P",
    "D6","P","P","P","B5","P",
    "A5","P","P","P","G5","P",#5
    "A5","P","P","P","A5","B5",
    "C6","P","P","P","B5","P",
    "G5","P","P","P","E5","P",
    "B5","P","P","P","P","P",#6
    "F5","P","P","P","A5","C6",
    "E6","P","P","P","P","P",
    "F5","P","E5","P","B5","P",
    "P","P","G5","P","P","P",#7
    "A5","P","B5","C6","B5","P",
    "P","P","A5","P","P","P",
    "A5","P","P","P","P","P",
    "GS5","P","P","P","B5","P",#8--
    "P","P","D6","E6","D6","C6",
    "B5","P","A5","P","B5","P",
    "P","P","D6","E6","D6","C6",
    "B5","P","P","P","P","P",#9
    "P","P","G6","A6","G6","F6",
    "G6","P","P","P","A6","P",
    "E6","P","E6","P","D6","P",
    "C6","P","D6","P","C6","P",#10
    "P","P","C6","D6","C6","AS5",
    "F5","P","P","P","D6","P",
    "C6","P","P","B5","A5","B5",
    "C6","P","P","P","A5","P",#11
    "B5","P","E5","P","DS5","P",
    "P","P","P","P","B5","P",
    "E5","P","DS5","P","P","P",
    "P","P","B5","P","A5","P",#12
    "P","P","P","P","P","P",
    "P","P","P","P","P","P",
    "D6","E6","D6","C6","B5","P",
    "A5","P","B5","P","P","P",#13
    "D6","E6","D6","C6","B5","P",
    "P","P","P","P","P","P",
    "G6","A6","G6","F6","G6","P",
    "P","P","A6","P","E6","P",#14
    "E6","D6","C6","D6","C6","P",
    "P","P","P","P","P","P",
    "C6","D6","C6","AS5","F5","P",
    "AS4","P","D6","P","C6","P",#15
    "P","B5","A5","B5","C6","P",
    "P","P","A5","P","B5","P",
    "E5","P","DS5","P","FS4","P",
    "P","P","B5","P","A5","P",#16
    "P","P","P","P","P","P",
    ]


Track4 = [
    "A4","E5","A5","E5","A4","E5","A5","E5",
    "C5","G5","C6","G5","C5","G5","C6","G5",
    "F4","C5","F5","C5","F4","C5","F5","C5",
    "E4","B4","E5","B4","E4","B4","E5","B4",
    "D4","A4","D5","A4","D4","A4","D5","A4",
    "C4","E4","C5","G4","C4","E4","C5","G4",
    "D4","F4","B4","F4","D4","B4","F4","B4",
    "D4","B4","F4","B4","D4","B4","G4","E4",
    "A4","E5","A5","E5","A4","E5","A5","E5",
    "C5","G5","C6","G5","C5","G5","C6","G5",
    "F4","C5","F5","C5","F4","C5","F5","C5",
    "E4","B4","E5","B4","E4","B4","E5","B4",
    "D4","A4","D5","A4","D4","A4","D5","A5",
    "C4","E4","A4","E4","C4","E4","A4","A5",
    "E4","G4","B4","E5","E4","D5","B4","E4",
    "A3","E4","A4","E4","A3","E4","A4","E4",
]

Track5 = [
    "E6","P","P","G5","E6","F6","E6","C6",
    "B5","P","G6","B5","G6","F6","E6","B5",
    "C6","P","P","E5","C6","D6","C6","A5",
    "C5","P","E6","D5","E6","B5","G5","D5",
    "F5","P","P","A5","C5","F5","C6","B5",
    "C6","P","G5","G5","C6","E6","C6","G5",
    "D6","P","P","C6","D6","E6","D6","C6",
    "G6","P","D6","B5","D6","F6","D6","G5",
    "E6","P","P","G5","E6","F6","E6","C6",
    "B5","P","G6","B5","G6","F6","E6","B5",
    "C6","P","P","E6","A5","A5","E6","A6",
    "G6","P","G5","D6","B5","G5","B5","G6",
    "F6","P","C5","F5","F6","C6","F6","A6",
    "G6","P","C6","E6","G6","G5","C6","E6",
    "D6","G5","B5","G6","A6","P","P","B5",
    "C6","P","P","P","C6","P","P","P",
]

Track6 = [
    "P","P","P","P","C6","D6","C6","G5",
    "E5","P","P","P","E6","P","P","P",
    "A5","P","P","P","A5","B5","A5","E5",
    "P","P","P","P","G5","P","P","P",
    "P","P","P","P","P","P","A5","G5",
    "E5","P","P","P","P","P","P","P",
    "F5","P","P","A5","F5","C6","D5","C6",
    "G5","P","P","P","P","P","P","P",
    "G5","P","P","P","C6","D6","C6","G5",
    "E5","P","P","P","E6","P","P","P",
    "A5","P","P","A5","E5","C5","C6","A5",
    "B5","P","P","P","G5","P","P","P",
    "F5","P","P","P","A5","F5","A5","F6",
    "E5","P","P","P","C6","P","P","C6",
    "B5","P","D5","G5","P","P","P","G5",
    "E5","P","P","P","E5","P","P","P",
]
#with open('ww.txt',encoding='utf-8') as file:
#     content=file.read()
#     print(content.rstrip())
 
#_thread.start_new_thread(LEDDisplay.Fresh,())
while True:
    playsong(Track3,Track2,Track1,0.21,buzzer1,buzzer2,buzzer3)
    playsong(Track6,Track5,Track4,0.34,buzzer1,buzzer2,buzzer3)
    bequiet(buzzer1)
    bequiet(buzzer2)
    bequiet(buzzer3)
    
