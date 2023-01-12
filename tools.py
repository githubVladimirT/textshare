#!/home/vladimir/vladimir/projects/copypaste/venv/bin/python
import os
import sys

def clean():
    posts_dir = "./posts/"
    try:
        for file in os.scandir(posts_dir):
            os.remove(file.path)
        return "successfully cleaned", None
    except Exception as err:
        return None, err

def init():
    try:
        os.mkdir("./posts/")
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
