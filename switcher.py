'''
FileName: switcher.py
Author: Chuncheng
Version: V0.0
Purpose: Switch to WeChat Wnd in Windows OS
'''

# %%
import time
from clipBoard import copy
from keyBoard import press

# %%

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

    time.sleep(1)

    press('w', on_hold='ctrl+alt')
    time.sleep(0.5)

    press('v', on_hold='ctrl')
    time.sleep(0.5)

    press('enter')

    return 0


# %%
if __name__ == '__main__':
    print('I: --')

    send_message(time.ctime())

    print('I: ByeBye')
