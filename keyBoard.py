'''
FileName: keyBoard.py
Author: Chuncheng
Version: V0.0
Purpose: Key Board Simulation
'''

# %%
import time
import keyboard

# %%


def press(key, on_hold=''):
    '''
    Method: press

    Keyboard Simulation with [key] as [on_hold] key is pressed down.

    Args:
    - @key, on_hold=''

    Outputs:
    - success

    '''
    if on_hold:
        keyboard.press(on_hold)
        print('D: Hold {}'.format(on_hold))

    time.sleep(0.1)

    keyboard.press_and_release(key)
    print('D: Press and Release {}'.format(key))

    time.sleep(0.1)

    if on_hold:
        keyboard.release(on_hold)
        print('D: Release {}'.format(on_hold))

    return 0


# %%
if __name__ == '__main__':
    print('I: --')
    time.sleep(1)
    press('v', on_hold='ctrl')
    print('I: ByeBye')
