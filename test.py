import socket, netstream, random, time, multiprocessing

connected = False
sock = None

serialID = 0            #server向客户端发回的序列ID号
isSet = False

def get_send_data():
    send_data = {}
    send_data['sid'] = serialID
    return send_data

#向server请求公告
def request_notice():
    send_data = get_send_data()
    send_data['notice'] = 'request notice'
    netstream.send(sock, send_data)
def send_gaming_data(value):
    send_data=get_send_data()
    send_data['gaming_data']=value
    netstream.send(sock,send_data)
def send_game_over_data(value):
    send_data=get_send_data()
    send_data['game_over_data']=value
    netstream.send(sock,send_data)

host = "172.18.158.159"
port = 9234
sock = socket.socket()
sock.connect((host, port))

time.sleep(1)

recvData = netstream.read(sock)
if 'sid' in recvData:
    serialID = recvData['sid']

request_notice()

random.seed(time.time())

final_points = random.randint(0, 20)
current_game_time = 0
g_score = 0
player = 'visitor'

time.sleep(1)

for g_score in range(0, final_points):

    wait_time = random.uniform(0.5, 2)

    g_score = g_score + 1
    time_stamp = time.time() + g_score
    current_time = time.asctime(time.localtime(time_stamp))
    current_game_time = current_game_time + wait_time
    data_after_pass = player + ' has just passed ' + str(g_score)
    data_after_pass = data_after_pass + ' after playing ' + str(current_game_time) + ' seconds ' + 'in  ' + current_time +'\n'
    send_gaming_data(data_after_pass)
    time.sleep(wait_time)

game_over_score = g_score
game_time = current_game_time
data = player + ' passed '+ str(game_over_score) + ' pipe(s)' + ' with alive time ' + str(game_time) + ' seconds in this game'
send_game_over_data(data)