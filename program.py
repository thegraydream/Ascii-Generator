cyan = "\033[38;2;0;117;127m"
reset = "\033[0m"

try:
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    from fake_headers import Headers
    import time
    import os
    import keyboard
    import subprocess
except:
    print(f'{cyan}Please download all requirements in requirements.txt')
    time.sleep(5)
    exit()

ascii = ""
page = 1
count = 0

# Ascii
def asciigenerator():
    print(f"\n\n{cyan}                           d8,  d8,                                                                                  ")
    print(f"{cyan}                          `8P  `8P                                                             d8P                   ")
    print(f"{cyan}                                                                                            d888888P                 ")
    print(f"{cyan} d888b8b   .d888b, d8888b  88b  88b     d888b8b   d8888b  88bd88b  d8888b  88bd88b d888b8b    ?88'   d8888b   88bd88b")
    print(f"{cyan}d8P' ?88   ?8b,   d8P' `P  88P  88P    d8P' ?88  d8b_,dP  88P' ?8bd8b_,dP  88P'  `d8P' ?88    88P   d8P' ?88  88P'  `")
    print(f"{cyan}88b  ,88b    `?8b 88b     d88  d88     88b  ,88b 88b     d88   88P88b     d88     88b  ,88b   88b   88b  d88 d88     ")
    print(f"{cyan}`?88P'`88b`?888P' `?888P'd88' d88'     `?88P'`88b`?888P'd88'   88b`?888P'd88'     `?88P'`88b  `?8b  `?8888P'd88'     ")
    print(f"{cyan}                                              )88                                                                    ")
    print(f"{cyan}                                             ,88P                                                                    ")
    print(f"{cyan}                                         `?8888P                                                                     \n")
    print(f"{cyan}                           {reset}By TheGrayDream {cyan}/{reset} Need help ? https://dsc.gg/tgdgithub\n\n")



# Clear Windows/Linux
def clear():
    try:os.system('cls')
    except:os.system('clear')

asciigenerator()

# Word to Ascii
word = input(f'{cyan}What do you want to convert to ascii > {reset}').replace(" ", "%20")
url = f"https://patorjk.com/software/taag/#p=testall&f=3D%20Diagonal&t={word}"

clear()
asciigenerator()
print(f'{cyan}Loading:{reset} 0%')

# Load Chrome Driver 
ua = Headers().generate()  
browser_option = ChromeOptions()
browser_option.add_experimental_option("excludeSwitches", ["enable-logging"])
browser_option.add_argument('--headless')
browser_option.add_argument('--disable-extensions')
browser_option.add_argument('--incognito')
browser_option.add_argument('--disable-gpu')
browser_option.add_argument('--log-level=3')
browser_option.add_argument(f'user-agent={ua}')
browser_option.add_argument('--disable-notifications')
browser_option.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=browser_option)

driver.get(url)

# Loading
while True:
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'html.parser')
    taag_div = soup.find('div', {'id': 'taagTestAllListLoaded'}).text.split()
    percent = round(int(taag_div[1])*100/int(taag_div[-1]))
    clear()
    asciigenerator()
    print(f'{cyan}Loading:{reset} {percent}% ({taag_div[1]}/{taag_div[-1]})')
    if int(taag_div[1]) == int(taag_div[-1]):break
    time.sleep(0.3)

for i in soup.find_all('div', {'class': 'fig'}) :
    count += 1
allascii = count

# Ascii choice
while True:
        count = 0
        print(f'({page}/{allascii})')
        for i in soup.find_all('div', {'class': 'fig'}) :
            count += 1
            if page == count:
                clear()
                print(f'{reset}[{cyan}{count}{reset}] Press space bar to select ASCII  <- Right Key - Left Key -> \n\n{i.text}\n')
                while True:
                    # Right Key add +1 Page
                    if keyboard.is_pressed('right'):
                        page+=1
                        if page > allascii:
                            page = 1
                        time.sleep(0.1)
                        break

                    # Right Key add -1 Page
                    if keyboard.is_pressed('left'):
                        page-=1
                        if page == 0:
                            page = allascii
                        time.sleep(0.1)
                        break

                    # Right Key get ASCII
                    if keyboard.is_pressed('space'):
                        ascii = i.text
                        break
        if not ascii == "":break
with open ('ascii.txt', 'w') as f:
    f.write(ascii)

defaultascii = ascii
printtype = -1
caracteree = ""
caractereb = ""

printtf = False

# Edit Ascii
while True:
    try:

        # Read ascii.txt
        with open ('ascii.txt', 'r') as f:
            ascii = f.read()
        clear()

        print(f"\n{reset}[{cyan}0{reset}] print()")
        print(f"{reset}[{cyan}1{reset}] add characters at the beginning")
        print(f"{reset}[{cyan}2{reset}] add characters at the end")
        print(f"{reset}[{cyan}3{reset}] clear")
        print(f'{reset}[{cyan}4{reset}] open')
        print(f'{reset}[{cyan}5{reset}] exit')
        print('\n')
        print(ascii)
        
        # Choice
        choice = int(input(f'\n\n{cyan}Select the number corresponding to the choice above > {reset}'))
        
        if choice == 5:
            break
        if choice == 4:
            subprocess.run(['start', 'notepad.exe', 'ascii.txt'], shell=True)


        # Print False/True
        elif choice == 0:
            while True:
                try:
                    printtf = True
                    clear()
                    print(f"\n{reset}[{cyan}0{reset}] print('')")
                    print(f'{reset}[{cyan}1{reset}] print("")')
                    print(f"{reset}[{cyan}2{reset}] print(f'')")
                    print(f'{reset}[{cyan}3{reset}] print(f"")')
                    print('\n')
                    print(ascii)

                    choice = int(input(f'\n\n{cyan}Select the number corresponding to the choice above > {reset}'))
                    
                    if not choice > 3 and not choice < 0:
                        printtype=choice
                        choice=0
                        break
                except:None


        elif choice == 1:
            choice = str(input(f'\n{cyan}Enter the character you want at the beginning > {reset}'))
            caractereb = choice

        elif choice == 2:
            choice = str(input(f'\n{cyan}Enter the character you want at the end > {reset}'))
            caracteree = choice

        # Create ascii file with 'defaultascii'
        with open ('ascii.txt', 'w') as f:
            f.write(defaultascii)
        
        # add caractere beginning
        with open("ascii.txt", "r") as f:
            line = f.read()
        line = line.splitlines()
        newline = []
        for lines in line:
            newlines = caractereb + lines + "\n"
            newline.append(newlines)
        with open("ascii.txt", "w") as f:
            f.writelines(newline)

        # add caractere end
        with open("ascii.txt", "r") as f:
            line = f.read()
        line = line.splitlines()
        newline = []
        for lines in line:
            newlines =  lines + f"{caracteree}\n"
            newline.append(newlines)
        with open("ascii.txt", "w") as f:
            f.writelines(newline)

        # add print
        if printtf == True:
            with open("ascii.txt", "r") as f:
                line = f.read()
            line = line.splitlines()
            newline = []
            print1 = ""
            print2 = ""
            for lines in line:
                if printtype == 0:
                    print1 = "print('"   
                    print2 = "')\n" 
                if printtype == 1:
                    print1 = 'print("'  
                    print2 = '")\n' 
                if printtype == 2:
                    print1 = "print(f'"   
                    print2 = "')\n" 
                if printtype == 3:
                    print1 = 'print(f"'  
                    print2 = '")\n' 
                newlines = print1 + lines + print2
                newline.append(newlines)
            with open("ascii.txt", "w") as f:
                f.writelines(newline)
        
        # clear
        if choice == 3:
            printtf = False
            caractereb = ""
            caracteree = ""
            printtype = -1
            with open("ascii.txt", "w") as f:
                f.write(defaultascii)
 
    except:None

print('See you soon!')
time.sleep(3)
exit()