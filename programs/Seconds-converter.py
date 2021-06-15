# Covert seconds into :
# 1. Hours
# 2. Minutes
# 3. Remaining secodns 

# Ex. 3000 seconds means how many hours we have got. 

def conv_sec(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = conv_sec(8000)
print(hours, minutes, seconds)