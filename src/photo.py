from time import sleep, time
import requests
import random
import pathlib
import os

# Setup
apis = ["https://api.gumengya.com/Api/DmImgS?format=image", "https://api.gumengya.com/Api/FjImg?format=image", "https://api.yimian.xyz/img",
        "https://img.paulzzh.tech/touhou/random", "https://www.dmoe.cc/random.php", "https://api.paugram.com/wallpaper/"]
PATH = pathlib.Path(__file__).parents[1] / "photo.png"
HISTORY_PATH = pathlib.Path(__file__).parents[1] / "assets"

if (pathlib.Path(__file__).parents[1] / "block").exists():
    print("The current run has been blocked")
    exit(0)


def main():
    CONTINUE = True
    TIMES = 0
    print(f"We will choose 1 url to fetch new photo and write it to {PATH}")
    if int(time()) % random.randint(1, 10) in [random.randint(1, 10) for each in range(random.randint(1, 8))]:
        RUN_TIMES = random.randint(10, 100)
        print(
            f"Since the random condition holds, we will adjust the number of runs to {RUN_TIMES} times")
    else:
        RUN_TIMES = 1
        print("Since the random condition doesn't hold, we will adjust the number of runs to 1 time")
    print("The progress will be continued in 5s")
    print("="*36)
    sleep(5)
    if int(time()) % random.randint(1, 10) in [random.randint(1, 10) for each in range(random.randint(1, 10))]:
        print(
            f"Since the random condition holds, we will archive to {HISTORY_PATH}")
        Archive = True
        HISTORY = [int(pathlib.Path(each.replace("photo", "").replace(
            "-", "")).stem) for each in os.listdir(HISTORY_PATH)]
        HISTORY.sort()
        Archive_PATH = HISTORY_PATH / f"photo-{HISTORY[-1] + 1}.png"
        del HISTORY
    else:
        print(
            f"Since the random condition doesn't hold, we won't archive to {HISTORY_PATH}")
        Archive = False

    while CONTINUE:
        TIMES += 1
        try:
            while True:
                RUN_TIMES -= 1
                url = apis[random.randint(0, len(apis)-1)]
                print(
                    f"The {url} has been chosen, We're going to fetch photo from that")
                if RUN_TIMES <= 0:
                    print("The number of runs has been less than or equal to 0, break the loop\n" +
                          "The progress will be continued in 3s\n"+"="*36)
                    sleep(3)
                    break
                else:
                    print(f"The number of runs left {RUN_TIMES} times, skip the break loop\n" +
                          "The progress will be continued in 3s\n"+"="*36)
                    sleep(3)
            response = requests.get(url)
            CONTINUE = False
        except BaseException as e:
            print(
                f"We've got an error{f'(detail: {e})' if e.__str__() else ''}, We're going to Retry")
            print("The progress will be continued in 3s")
            print("="*36)
            sleep(3)
            CONTINUE = True

        if TIMES >= 10:
            error = Exception("The number of retries has exceeded the limit")
            raise error

    print(
        f"We have got the response( URL: {response.url} ), We're going to write-in")
    with open(PATH, "wb+") as f:
        f.write(response.content)
    if Archive:
        with open(Archive_PATH, "wb+") as f:
            f.write(response.content)
    print("The progress will be continued in 10s")
    print("="*37)
    sleep(10)
    print(f"The data has been written")


if __name__ == "__main__":
    Start = time()
    main()
    Stop = time()
    print(f"It spent {Stop - Start}s in total")
