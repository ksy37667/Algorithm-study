import datetime 

def solution(play_time, adv_time, logs):

    d = datetime.datetime.strptime(play_time, "%H:%M:%S")
    a = datetime.datetime.strptime(adv_time, "%H:%M:%S")
    log = []
    x = [0] * 2 
    abc = []
    
    for i in logs:
        abc = i.split('-')
        for j in range(2):
            x[j] = datetime.datetime.strftime(abc[j], "%H:%M:%S")
        log.append(x)

    play_time = d.time()
    adv_time = a.time()
    
    
    print(adv_time)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution(play_time,adv_time,logs)