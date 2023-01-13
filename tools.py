import os
import sys
from settings import POSTS_DIR, LOGS_DIR


def clean():
    posts_dir = POSTS_DIR
    logs_dir = LOGS_DIR
    try:
        for file in os.scandir(posts_dir):
            os.remove(file.path)
        for file in os.scandir(logs_dir):
            os.remove(file.path)
        return "successfully cleaned", None
    except Exception as err:
        return None, err


def init():
    try:
        os.mkdir("./posts/")
        os.mkdir("./logs/")
        env = open('.env', 'x')
        env.close()
    except FileExistsError:
        pass
    finally:
        print("successfully initialized")


def main():
    args = sys.argv[1::]

    match args:
        case ["init"]:
            init()

        case ["clean"]:
            stat, err = clean()
            if err != None:
                print(err)
                exit(-1)
            print(stat)

        case _:
            print("error: unknow command")
            exit(-1)


if __name__ == "__main__":
    main()
