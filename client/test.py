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

server_thread = threading.Thread(target=testchat.server, daemon=True)
server_thread.start()

listener_thread = threading.Thread(target=output_widget, daemon=True)
listener_thread.start()


print(*list(testchat.nicks.keys()), sep='\n')
friend = input('friend:\n')
print('friend:{}'.format(friend))
testchat.out_connect(friend)
testchat.out_stream('!!!#!#!SAY HELLO WORLD BRO!!#!#@')

while True:
    msg = input()
    print(msg)
    print('sending {}'.format(msg))
    testchat.out_stream(msg)
