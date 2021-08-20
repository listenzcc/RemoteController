'''
FileName: clipBoard.py
Author: Chuncheng
Version: V0.0
Purpose: Control Clip Board
'''

# %%
import time
import clipboard

# %%
default_message = time.ctime()
default_message

# %%


def copy(message=default_message):
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


# %%
if __name__ == '__main__':
    msg = input('(Type to Copy) >> ')
    copy(msg)
    print('I: ByeBye.')
