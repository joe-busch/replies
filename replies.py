import clipboard
import json
import sys

SAVED_REPLIES = 'reply.json'

def save_replies(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def load_replies(file):
    try:
        with open(file, 'r') as f:
            replies = json.load(f)
            return replies
    except:
        return {}


def get_key():
    if len(sys.argv) > 2:
        key = sys.argv[2]
    else:
        key = input('Enter key: ')

    return key


replies = load_replies(SAVED_REPLIES)


if len(sys.argv) > 1:
    command = sys.argv[1]
    key = get_key()
    
    if command == 'save':
        replies[key] = clipboard.paste()
        save_replies(SAVED_REPLIES, replies)
        print(f'Reply saved under {key}.')

    elif command == 'load':
        if key in replies:
            clipboard.copy(replies[key])
            print('Reply copied to clipboard.')
        else:
            print(f'{key} not found in data file.')

    elif command == 'list':
        print(replies)

    elif command == 'delete':
        del replies[key]
        save_replies(SAVED_REPLIES, replies)

    else:
        print('Unknown command. Try save, load, or list.')

else:
    print(f'Usage: {sys.argv[0]} command [key]')
