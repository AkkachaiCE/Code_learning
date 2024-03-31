import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    match = re.search(r'(\d{1,2}(:\d{2})? (AM|PM)) to (\d{1,2}(:\d{2})? (AM|PM))', s, re.IGNORECASE)
    if match:
        times = [match.group(1), match.group(4)]
        new_times = []

        for _ in times:
            parts = _.split(":")
            hours = parts[0]
            if len(parts) > 1:
                minutes, am_pm = parts[1].split()
            else:
                minutes = "00"
                am_pm = hours[-2:]
                hours = hours[:-2].strip()
            if am_pm.upper() == "PM" and hours != "12":
                hours = str(int(hours) + 12)
            if am_pm.upper() == "AM" and hours == "12":
                hours = "00"
            if int(minutes) > 59:
                raise ValueError
            new_times.append(f"{int(hours):02}:{minutes}")
        return new_times[0] + " to " + new_times[1]
    else:
        raise ValueError




if __name__ == "__main__":
    main()
