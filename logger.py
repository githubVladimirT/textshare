import logging
import sys
import os
from settings import LOGS_DIR, LOG_LEVEL
from datetime import datetime
import argparse


def clientslogger(clientip: str, req: str, targetname: str):
    year_and_month = datetime.now().strftime("%Y-%m")
    
    try:
        os.mkdir(f'./{LOGS_DIR}/{year_and_month}/')
    except FileExistsError:
        pass

    time = datetime.now().strftime("%Y-%m-%d")
    #name = f"./{LOGS_DIR}/{year_and_month}/{time}.log"
    global name
    name = os.path.join(LOGS_DIR, year_and_month, f"{time}.log")

    log = logging.getLogger("2a6f906e-ca2b-11ed-a80e-7412b32f9ac7")
    handler = logging.FileHandler(name)
    formatter = logging.Formatter("[  %(levelname)s  ]  -  %(clientip)s %(asctime)s - %(message)s %(targetname)s")

    handler.setLevel(LOG_LEVEL)
    handler.setFormatter(formatter)
    log.addHandler(handler)

    data = {
        'clientip': clientip,
        'targetname': targetname,
    }

    match req:
        case "POST":
            log.info("created a file:", extra=data)
            return f"post request had written to ./{name}", name, None
        case "GET":
            log.info("requested to file:", extra=data)
            return f"get request had written to ./{name}", name, None
        case "DELETE":
            log.info("requested to deleted file: ", extra=data)
            return f"request to deleted file had written to ./{name}", name, None
        case _:
            return "error: unknow request", name, True
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
