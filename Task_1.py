time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
values = time_str.split(',')

for val in values:
    val = val.replace(' ', '')
    if 'h' in val:
        h = int(val.split('h'))
        total_minutes += h * 60
        val = val.split('h')
    if 'm' in val:
        m = int(val.split('m'))
        total_minutes += m
        val = val.split('m')
    if 's' in val:
        s = int(val.split('s'))
        total_minutes += s // 60

print(total_minutes)