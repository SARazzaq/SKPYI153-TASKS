# Create a countdown timer using Python

import time

def countdown_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        duration -= 1
    
    print('Countdown complete!')

def main():
    try:
        duration = int(input("Enter the countdown duration in seconds: "))
        countdown_timer(duration)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == '__main__':
    main()
