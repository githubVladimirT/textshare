import logging
import sys
import os
from settings import LOGS_DIR, LOG_LEVEL
from datetime import datetime
import argparse


def flush(logfile):
    sys.stdout.flush()
    logfile.flush()



def clientslogger(clientip: str, req: str, targetname: str):
    try:
        year_and_month = datetime.now().strftime("%Y-%m")
    
        try:
            os.mkdir(f'{LOGS_DIR}/{year_and_month}/')
        except FileExistsError:
            pass

        global name
        name = os.path.join(LOGS_DIR, year_and_month, f'{datetime.now().strftime("%Y-%m-%d")}.log')

        logfile = open(name, 'a')
        formatter = "[  {}  ]  - ip: {} time: {} - msg: {} target: {}"

        match req:
            case "POST":
                logfile.write(formatter.format("INFO", clientip, datetime.now().strftime("%Y-%m-%d"), "created a file", targetname))
                flush(logfile)
                print(f"post request had written to /{name}")
                return f"post request had written to /{name}", name, None
            case "GET":
                logfile.write(formatter.format("INFO", clientip, datetime.now().strftime("%Y-%m-%d"), "requested to file", targetname))
                flush(logfile)
                print(f"get request had written to /{name}")
                return f"get request had written to /{name}", name, None
            case "DELETE":
                logfile.write(formatter.format("INFO", clientip, datetime.now().strftime("%Y-%m-%d"), "requested to deleted file", targetname))
                flush(logfile)
                print(f"request to deleted file had written to /{name}")
                return f"request to deleted file had written to /{name}", name, None
            case _:
                logfile.write(formatter.format("ERROR", "NUL", datetime.now().strftime("%Y-%m-%d"), "UNKNOWN REQUEST", "NUL"))
                flush(logfile)
                print("error: unknow request")
                return "error: unknow request", name, True

    except Exception as err:
        logfile.write(formatter.format("ERROR", "NUL", datetime.now().strftime("%Y-%m-%d"), f"ERROR: '{err}'", "NUL"))
        print(f"ERROR!\ntext: {err}")
      
        logfile.close()
        exit(-1)


if __name__ == "__main__":
    print("---testmode---")

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip')
    parser.add_argument('-r', '--request')
    parser.add_argument('-f', '--file')

    args = parser.parse_args(sys.argv[1:])

    clientip = args.ip
    request = args.request
    filename = args.file

    print(f"{clientip=}")
    print(f"{request=}")
    print(f"{filename=}")
    
    res, name, err = clientslogger(clientip, request, filename)
    if err != None:
        print("---failed---")
        print(res)
        sys.exit(-1)

    print("---success---")
    print(res)

    os.remove(name)
