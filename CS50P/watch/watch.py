import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'src=["\']([^"\']*)["\']', s)
    if match:
        url = match.group(1)
        #return url
        if "youtube" in url:
            url = url.replace("https://www.youtube.com/embed", "https://youtu.be").replace("http://www.youtube.com/embed", "https://youtu.be")
            url = url.replace("https://youtube.com/embed", "https://youtu.be").replace("http://youtube.com/embed", "https://youtu.be")
            return url
        else:
            return None


if __name__ == "__main__":
    main()

