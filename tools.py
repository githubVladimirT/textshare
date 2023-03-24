import os
import sys
from settings import POSTS_DIR, POSTS_OLD_DIR, LOGS_DIR


def clean():
    try:
        for file in os.scandir(POSTS_DIR):
            os.remove(file.path)
        for file in os.scandir(POSTS_OLD_DIR):
            os.remove(file.path)
        for file in os.scandir(LOGS_DIR):
            os.remove(file.path)
        return "successfully cleaned", None
    except Exception as err:
        return None, err


def init():
    try:
        os.mkdir("./posts/")
        os.mkdir("./posts.old/")
        os.mkdir("./logs/")
        env = open('.env', 'x')
        env.close()
    except FileExistsError:
        pass
    finally:
        print("successfully initialized")


def main():
    args = sys.argv[1::]

#    match args:
#        case ["init"]:
#            init()
#
#        case ["clean"]:
#            stat, err = clean()
#            if err != None:
#                print(err)
#                exit(-1)
#            print(stat)
#
#        case _:
#            print("error: unknow command")
#            exit(-1)

    if "init" in args:
        init()
    if "clean" in args:
        stat, err = clean()
        if err != None:
            print(err)
            exit(-1)
        print(stat)
    if ("init" not in args) and ("clean" not in args):
        print("error: unknow command")
        exit(-1)


if __name__ == "__main__":
    main()
