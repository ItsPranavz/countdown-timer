# importing required modules
import tkinter as tk
# defining start function
def start():
    global clock_active, clock_pause
    if clock_active:
        pass
    else:
        clock_active = True
        clock_pause = False
        clock()
# defining stop function
def stop():
    global clock_pause
    clock_pause = True
# defining reset function
def reset():
    hours.set("00")
    mins.set("00")
    secs.set("00")
# defining a clock function
def clock():
    global clock_active
    hr = int(hours.get())
    mn = int(mins.get())
    sc = int(secs.get())
    time = 3600*hr + 60*mn + sc
    if time > 0 and clock_pause == False:
        time -= 1
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        hours.set(f"{h:02d}")
        mins.set(f"{m:02d}")
        secs.set(f"{s:02d}")
        window.after(1000,clock)
    else:
        clock_active = False
# setting up the window
window = tk.Tk()
window.title("Countdown Timer")
window.geometry("400x150")
# setting up the fomts
font1 = ('Times', 30)
font2 = ('Helvetica bold', 16)
# setting up global variables
clock_active = False
clock_pause = False
# setting up ui variables
hours = tk.StringVar()
mins = tk.StringVar()
secs = tk.StringVar()
# setting up the frames
timer_frame = tk.Frame(window)
control_frame = tk.Frame(window)
timer_frame.pack()
control_frame.pack()
# setting up the timer frame
hour_entry = tk.Entry(timer_frame,font=font1,textvariable=hours,width=2)
mins_entry = tk.Entry(timer_frame,font=font1,textvariable=mins,width=2)
secs_entry = tk.Entry(timer_frame,font=font1,textvariable=secs,width=2)
colon_one = tk.Label(timer_frame,text=":",font=font1)
colon_two = tk.Label(timer_frame,text=":",font=font1)
hour_entry.grid(row=0,column=0,padx=5,pady=5)
colon_one.grid(row=0,column=1,padx=5,pady=5)
mins_entry.grid(row=0,column=2,padx=5,pady=5)
colon_two.grid(row=0,column=3,padx=5,pady=5)
secs_entry.grid(row=0,column=4,padx=5,pady=5)
# setting values into entry boxes
hours.set("00")
mins.set("00")
secs.set("00")
# setting up the control frame
start_button = tk.Button(control_frame,text="Start",font=font2,width=5,command=start)
stop_button = tk.Button(control_frame,text="Stop",font=font2,width=5,command=stop)
reset_button = tk.Button(control_frame,text="Reset",font=font2,width=5,command=reset)
start_button.grid(row=0,column=0,padx=5,pady=25)
stop_button.grid(row=0,column=1,padx=5,pady=25)
reset_button.grid(row=0,column=2,padx=5,pady=25)
# starting the mainloop
window.mainloop()