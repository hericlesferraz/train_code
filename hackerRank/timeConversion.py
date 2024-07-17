
def timeConversion(s):
    #12:00:00AM

    h, m, sec, _ = f"{s[:-2]}:".split(":")
    if "AM" in s:
        if int(h) > 12:
            result = f"{12 - int(h)}:{m}:{sec}"

        elif h == 12:
            result = f"00:{m}:{sec}"

        else:   
            result = f"{h}:{m}:{sec}"

    elif "PM"in s:
        h = 12 + int(h)
        result = f"{h}:{m}:{sec}"

        if h == 24:
            result = f"00:{m}:{sec}"

    print(result)
    return result

if __name__ == '__main__':

    s = "12:01:00AM"
    s = timeConversion(s)
