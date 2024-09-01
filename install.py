import distro
import os

url = 'https://github.com/TheRayanFikri/Launcher/'

#Getting The current Directory:
currentDirectory = os.getcwd()

#Prompt:
print("Welcome to Gnome Auto Theming Project.\nSo This will help you install the available themes on it.")

#Home Directory:
home = os.path.expanduser("~")

#Other Directory:
iconFolderPath = f"{home}/.icons"
themesFolderPath = f'{home}/.themes'

#Installation Permission:
print('Are you sure you want to download Gnome Auto-Theme Tweaker ? [y/n]')
installationPermission = input('-->')

if installationPermission == "y" or installationPermission == "yes" or installationPermission == '' or installationPermission == 'ye' or installationPermission == 'Yes' or installationPermission == 'yEs' or installationPermission == ' yeS' or installationPermission == "YES":
    #.icons and .themes files existance check:
    print('__________________________________________________')
    if os.path.exists(iconFolderPath):
        print('\n.icons folder already exists !')
    else:
        print(".icons folder doesn't exist creating a new one...")
        os.mkdir(iconFolderPath)
        print('.themes folder created succesfully !')

    if os.path.exists(themesFolderPath):
        print('.themes folder already exists !')
    else:
        print(".icons folder doesn't exist creating a new one...")
        os.mkdir(themesFolderPath)
        print('.themes folder created succesfully !')

    print('__________________________________________________')
    def installingRequirements():
        print("Downloading The other Requirements:")
        print('Tkinter..')
        if distro.id() == "manjaro" or distro.id() == "arch":
            os.system('sudo pacman -S tk')
        elif distro.id == 'Ubuntu' or distro.id() == "debian" or distro.id() == "linuxmint":
            os.system('sudo apt-get install python-tk')
        elif distro.id == 'centos' or distro.id == 'rhel' or distro.id == 'oracle':
            os.system('sudo yum install tkinter tk-devel')
        elif distro.id == 'fedora':
            os.system('sudo dnf install python3-tkinter')
        print('Tkinter Installation Finished successfully !')
        
        #Installing gnome Tweaks:
        print('__________________________________________________')
        print('Installing Gnome Tweaks...')
        if distro.id() == "manjaro" or distro.id() == "arch":
            os.system('sudo pacman -S gnome-tweaks')
        elif distro.id == 'Ubuntu' or distro.id() == "debian" or distro.id() == "linuxmint":
            os.system(' sudo apt install gnome-tweaks')
        elif distro.id == 'centos' or distro.id == 'rhel' or distro.id == 'oracle':
            os.system('sudo yum install gnome-tweaks')
        elif distro.id == 'fedora':
            os.system('sudo dnf install gnome-tweaks')
        print('Gnome Tweaks was succesfully installed on your system !')
        print('__________________________________________________')
        
        #Launcher.py Installation:
        if os.path.isdir('Launcher'):
            print('__________________________________________________')
            updateLauncher = input('The Launcher is Already installed !\nDo you want to update it in case of Update release ? [y/n]')
            if updateLauncher == "y" or updateLauncher == "yes" or updateLauncher == '' or updateLauncher == 'ye' or updateLauncher == 'Yes' or updateLauncher == 'yEs' or updateLauncher == 'yeS' or updateLauncher == "YES":
                print('__________________________________________________')
                print('reinstalling the launcher and searching for updates...')
                os.system(f'rm -rf Launcher && git clone {url}')
                
        else:
            print('__________________________________________________')
            print('Downloading the launcher...')
            os.system(f'git clone {url}')
            print('Download Finished successfully !')
        print('__________________________________________________')

    installingRequirements()

    #App Launch
    print('Wanna launch the app now (Default: Yes) ? [y/n]')
    applaunch = input("-->")

    def applauncher():
        print('Launching the app...')
        os.system("python3 Launcher/launcher.py")
        print('___________________________________________________')

    if applaunch == "y" or applaunch == "yes" or applaunch == '' or applaunch == 'ye' or applaunch == 'Yes' or applaunch == 'yEs' or applaunch == ' yeS' or applaunch == "YES":
        applauncher()
    else:
        print('Ok then :(')