from lib import Conversation
import threading

nick = input('nick:')

testchat = Conversation()

server_thread = threading.Thread(target=testchat.server, daemon=True)
server_thread.start()


connected = threading.Event()
def output_widget():
    connected.wait()
    for msg in testchat.in_stream():
        print(msg)

listener_thread = threading.Thread(target=output_widget, daemon=True)
listener_thread.start()

def input_widget(msg):
    testchat.out_stream(msg)

print(*list(testchat.nicks.keys()), sep='\n')
friend = input('friend:')
testchat.out_connect(friend)

connected.set()

while True:
    testchat.out_stream(input())
