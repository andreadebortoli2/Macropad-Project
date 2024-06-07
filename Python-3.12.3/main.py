from pynput import keyboard
from pynput.keyboard import Key, Controller
import subprocess
import time
import username

keyboard = Controller()

user_name = username.user_name
vs_code_path = "C:/Users/{}/AppData/Local/Programs/Microsoft VS Code/bin/Code.cmd".format(user_name)


def start_shortcut_program():
    
    # choose project
    project_type = input('Project type: (O) old, (N) new => ')
    
    if project_type.upper() == 'O':
        print('OPEN Old PROJECT')
        
    elif project_type.upper() == 'N':
        print('create NEW project')
    
    else:
        #re-start
        start_shortcut_program()

    if project_type.upper() == 'O':
        
        # choose old project type
        print("It's an old (L)aravel project or (E)lse?")
        old_project_type = input()
        
        if old_project_type.upper() == 'L':

            # open vs code
            subprocess.run(vs_code_path)
            # open terminal
            keyboard.press(Key.ctrl)
            keyboard.tap(key='ò')
            keyboard.release(Key.ctrl)
            # open folder
            keyboard.press(Key.ctrl)
            keyboard.tap(key='k')
            keyboard.tap(key='o')
            keyboard.release(Key.ctrl)
            # open mamp and close pop-up page
            time.sleep(1)
            subprocess.run("C:/MAMP/MAMP.exe")
            time.sleep(3)
            keyboard.press(Key.ctrl)
            keyboard.tap(key='w')
            keyboard.release(Key.ctrl)
            
        elif old_project_type.upper() == 'E':
        
            # open vs code
            subprocess.run(vs_code_path)
            # open folder
            keyboard.press(Key.ctrl)
            keyboard.tap(key='k')
            keyboard.tap(key='o')
            keyboard.release(Key.ctrl)
            
        else:
            # re-start
            start_shortcut_program()

    elif project_type.upper() == 'N':
        
        print('Which type of project you want to start? (L)aravel or (V)vue + vite')
        new_project_type = input()
        
        if new_project_type.upper() == 'V':
            print('NEW VUE3 + VITE PROJECT')

        elif new_project_type.upper() == 'L':
            print('NEW Laravel PROJECT')
            
        else:
            # re-start
            start_shortcut_program()    
        
        # write repository title
        repository_title = input('Write repository title: ')
            
        # confirm project
        print('Are you shure? Y/n')
        new_project_confirm = input()

        if new_project_confirm.upper() == 'Y':
            
            if new_project_type.upper() == 'V':
                # open vs code
                subprocess.run(vs_code_path)
                # open terminal
                keyboard.press(Key.ctrl)
                keyboard.tap(key='ò')
                keyboard.release(Key.ctrl)
                # navigate to folder
                time.sleep(3)
                keyboard.type('cd "C:\\Users\\{}\\OneDrive\\Desktop\\Coding\\Boolean\\JS"'.format(user_name))
                keyboard.tap(Key.enter)
                # start installation vue vite projects with repository_title
                time.sleep(1)
                create_command_vue = 'npm create vite@latest {} -- --template vue'.format(repository_title)
                keyboard.type(create_command_vue)
                keyboard.tap(Key.enter)
                    
            elif new_project_type.upper() == 'L':
                # open vs code
                subprocess.run(vs_code_path)
                # open terminal
                keyboard.press(Key.ctrl)
                keyboard.tap(key='ò')
                keyboard.release(Key.ctrl)
                # navigate to folder
                time.sleep(3)
                keyboard.type('cd "C:\\MAMP\\htdocs\\laravel"')
                keyboard.tap(Key.enter)
                # start installation laravel projects with repository_title
                time.sleep(1)
                create_command_laravel = 'composer create-project laravel/laravel:^10.0 ' + repository_title
                keyboard.type(create_command_laravel)
                keyboard.tap(Key.enter)
                # open laravel-notes.txt
                time.sleep(1)
                subprocess.Popen(["C:/Program Files/WindowsApps/Microsoft.WindowsNotepad_11.2402.22.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe", "C:\\Users\\{}\\OneDrive\\Desktop\\Coding\\appunti\\laravel-notes.txt".format(user_name)])
                # open mamp and close pop-up page
                time.sleep(1)
                subprocess.Popen("C:/MAMP/MAMP.exe")
                time.sleep(3)
                keyboard.press(Key.ctrl)
                keyboard.tap(key='w')
                keyboard.release(Key.ctrl)
                    
            else:
                # re-start
                start_shortcut_program()
                    
        else:
            # re-start
            start_shortcut_program()
            
    else:
        # re-start
        start_shortcut_program()
        
        
if __name__ == '__main__':
    start_shortcut_program()