cricket=[ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
football=[ "PKM", "ALN","RMZ","CS", "MCS"]
badminton=[ "PKM", "ALN", "NV", "KM","RMV"]

print('Players who play all three games: ')
for name in cricket:
    if name in football and name in badminton:
        print(name)

print('Players who play exactly one game: ')
for name in cricket:
    if name not in football and name not in badminton:
     print(name)
for name in football:
    if name not in cricket and name not in badminton:
     print(name)
for name in badminton:
    if name not in cricket and name not in football:
     print(name)