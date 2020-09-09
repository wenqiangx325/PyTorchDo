import requests
import os


def download_file(url: str, output: str = None):

    # test url
    if url == "" or url is None:
        raise OSError("url can't be empty.")

    # test and rebuild file name
    if os.path.isfile(output):
        raise OSError(f"{output} is exists as a file.")

    if output is None:
        output = os.path.join("data", url.split("/")[-1])

    output.split("/")[:-2]
    with requests.get(url) as r:
        pass
