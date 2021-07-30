'''
FileName: operator.py
Author: Chuncheng
Version: V0.0
Purpose: WeChat Operator
'''

import time
import clipboard
import keyboard


def send_message(message):
    '''
    Method: send_message

    Send [message] to WeChat and Send the Message

    Args:
    - @message

    Outputs:
    - Success

    '''

    copy(message)

    time.sleep(0.1)

    # press('w', on_hold='ctrl+alt')
    # time.sleep(0.5)

    press('v', on_hold='ctrl')
    time.sleep(0.1)

    press('enter')

    return 0


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


def copy(message):
    '''
    Method: copy

    Copy [message] to the clipBoard,

    Args:
    - @message

    Outputs:
    - Success

    '''
    clipboard.copy(message)
    print('D: Copy {} to clipboard'.format(clipboard.paste()))

    # Add return value to prevent escape too early
    return 0
