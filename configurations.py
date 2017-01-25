def set_time():
    print "PLEASE ENTER TIME FOR THE CYCLES OF PRESS <ENTER> TO USE DEFAULT TIME"
  
    print
    
    time=raw_input("TIME FORMAT HH:MM:SS => ")

    if time == "":
        time = "00:25:00"
        print "DEFAULT TIME SET: %s" %time
        pomodoro_time = time.split(':')
        for i in [0,1,2]:
                pomodoro_time[i] = int(pomodoro_time[i])
        return time
        
    else:

        pomodoro_time = time.split(':')
        
        if len(pomodoro_time)!= 3:
            print "INVALID INPUT! use the correct format"
            print
            return set_time()  

        else:
            for i in [0,1,2]:
                pomodoro_time[i] = int(pomodoro_time[i])
            return time

def set_short_break():
    print "SET THE SHORT BREAK TIME"
    print
    short_break = raw_input("TIME FORMAT HH:MM:SS => ")
    if short_break=='':
        short_break = "00:05:00"
        print "DEFAULT SHORT BREAK TIME SET: %s"%short_break
        SB = short_break.split(':')

        for i in [0,1,2]:
            SB[i] = int(SB[i])

        return short_break

    else:
        SB = short_break.split(':')
        if len(SB) != 3:
            print "INVALID INPUT! use correct format"
            print
            return set_short_break()
        else:
            for i in [0,1,2]:
                SB[i] = int(SB[i])
            return short_break
    

def set_long_break():
    print "SET THE LONG BREAK TIME"
    print
    long_break = raw_input("TIME FORMAT: HH:MM:SS =>")

    if long_break == '':
        print
        long_break = "00:15:00"
        print "DEFAULT LONG BREAK TIME SET: " 
        LB = long_break.split(':')

        for i in [0,1,2]:
            LB[i] = int(LB[i])
            
        return long_break
    
    else:
        LB = long_break.split(':')
        if len(LB) != 3:
            print 'INVALID INPUT! use the correct format'
            print
            return set_long_break()
        else:
            for i in [0,1,2]:
                LB[i] = int(LB[i])

            return long_break

def set_sound():
    print "ENTER \'on\' or \'off\' TO SET SOUND ALERT OR PRESS <ENTER> TO USE THE DEFAULT SETTINGS"
    print
    sound = raw_input('=> ')
    sound = sound.lower()
    

    if sound =='':
        sound = True
        print "DEFAULT SOUND SET: \'SOUND ON\'"
        return sound
    else:
        if sound == 'on':
            sound = True
            return sound
        elif sound == 'off':
            sound = False
            return sound
        else:
            print "INVALID INPUT! enter \'on\' or \'off\'"
            print
            return set_sound()
        return sound

def set_total_taskTime():
    print "SET THE TOTAL TASK DURATION"
    print
    duration = raw_input("TIME FORMAT HH:MM:SS => ")

    if duration == '':
        duration = '01:00:00'
        print 'DEFAULT DURATION TIME SET: %s' %duration
        TT = duration.split(':')
        for i in [0,1,2]:
                TT[i] = int(TT[i])
        return duration
    
        
    else:
        TT = duration.split(':')

        if len(TT) != 3:
            print "INVALID INPUT! use the correct format"
            print
            return set_total_taskTime()

        else:
            for i in [0,1,2]:
                TT[i] = int(TT[i])

            return duration


        
            
            
    
                    

        
        
        
        

   

        
                    
        
        

    
