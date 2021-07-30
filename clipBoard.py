'''
FileName: clipBoard.py
Author: Chuncheng
Version: V0.0
Purpose: Control Clip Board
'''

# %%
import time
import pandas as pd

# %%
default_message = time.ctime()
default_message

# %%


def copy(message=default_message):
    '''
    Method: copy

    Copy [message] to the clipBoard,
    using the Pandas to copy into the clipBoard.

    Since the Pandas copies the dataFrame as csv format,
    we generate an empty dataFrame with the column as the [message],
    and ignore the index column of the dataFrame,
    to perform the copy.

    Args:
    - @message

    Outputs:
    - Success

    '''

    df = pd.DataFrame(columns=[message])
    df.to_clipboard(sep=',', index=False)
    print('D: Copy {} to clipboard'.format(message))

    # Add return value to prevent escape too early
    return 0


# %%
if __name__ == '__main__':
    msg = input('(Type to Copy) >>')
    copy(msg)
    print('I: ByeBye.')
