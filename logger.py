import logging
import sys
import os
from settings import LOGS_DIR, LOG_LEVEL
from datetime import datetime
import argparse


def clientslogger(clientip: str, req: str, targetname: str):
    time = datetime.now().strftime("%Y-%m-%d")
    name = f"{time}.log"

    logging.basicConfig(
        level=LOG_LEVEL,
        filename=f'./{LOGS_DIR}/{name}',
        filemode='a',
        format='[  %(levelname)s  ]  -  %(clientip)s %(asctime)s - %(message)s %(targetname)s'
    )

    data = {
        'clientip': clientip,
        'targetname': targetname,
    }

    match req:
        case "POST":
            logging.info("created a file:", extra=data)
            return f"post request had written to ./{LOGS_DIR}/{name}", name, None
        case "GET":
            logging.info("requested to file:", extra=data)
            return f"get request had written to ./{LOGS_DIR}/{name}", name, None
        case "DELETE":
            logging.info("requested to deleted file: ", extra=data)
            return f"request to deleted file had written to ./{LOGS_DIR}/{name}", name, None
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

    os.remove("./{LOGS_DIR}/{name}")
