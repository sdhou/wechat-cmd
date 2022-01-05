import itchat
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from itchat.content import *
from prompt_toolkit import print_formatted_text


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print('{} {}:{}:{}'.format(msg.User.RemarkName, msg.User.NickName, msg.type, msg.text))


itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run(True, False)
friends = []
friends_get = itchat.get_friends()
for index, friend in enumerate(friends_get):
    a = '{}_{}{}'.format(index, friend.RemarkName, friend.NickName).strip()
    friends.append(a)


html_completer = WordCompleter(friends, match_middle=True)
while True:
    text = prompt('friends completer:', completer=html_completer)
    a = text.split('_')[0]
    msg = prompt('msg:')
    # if !msg:

    friends_get[int(a)].send(msg)
