import win32api as wapi
keyList = ["\b"]
for char in "WSJLKADP":
    keyList.append(char)
def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
 