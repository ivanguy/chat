from lib import Conversation
import threading

def input_widget(msg):
    testchat.out_stream(msg)

def output_widget():
    print('barrier breaked')
    for msg in testchat.in_stream():
        print(msg)

nick = input('nick:')

testchat = Conversation(nick)
listener_thread = threading.Thread(target=output_widget, daemon=True)
listener_thread.start()

while True:
    try:
        print(*list(testchat.nicks.keys()), sep='\n')
        break
    except AttributeError:
        continue
friend = input('friend:\n')
testchat.out_connect(friend)
testchat.out_stream('!!!#!#!SAY HELLO WORLD BRO!!#!#@')

while True:
    msg = input()
    print(msg)
    print('sending {}'.format(msg))
    testchat.out_stream(msg)
