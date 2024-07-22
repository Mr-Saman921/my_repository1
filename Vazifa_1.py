
import time

def weak():
    if int(time.strftime("%w")) > 3:
        return time.strftime("%A is %w th day in a weak")
    elif int(time.strftime("%w")) == 1:
        return time.strftime("%A is %w st day in a weak")
    elif int(time.strftime("%w")) == 2:
        return time.strftime("%A is %w nd day in a weak")
    elif int(time.strftime("%w")) == 3:
        return time.strftime("%A is %w rd day in a weak")

print(weak())