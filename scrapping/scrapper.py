import sys
import time
from datetime import datetime

import pandas as pd

import requests

from bs4 import BeautifulSoup

from pymongo import MongoClient


def do_scrapping(scrap_stamp=None, mongohost="localhost"):
    pagesToGet = 1

    upperframe = []

    for page in range(1, pagesToGet + 1):
        print("processing page :", page)

        url = "https://www.politifact.com/factchecks/list/?page=" + str(page)

        print(url)

        # an exception might be thrown, so the code should be in a try-except block 15

        try:
            # use the browser to get the url. This is suspicious command that might blow up.

            page = requests.get(url)

            # this might throw an exception

        except Exception:  # this describes what to do if an e 10
            error_type, error_obj, error_info = (
                sys.exc_info()
            )  # get the exception information 11

            print("ERROR FOR LINK:", url)  # print the link that cause the pr 22

            print(error_type, "Line:", error_info.tb_lineno)

            # print error info and line that th 23

            continue  # ignore this page. Abandon this an 24

        time.sleep(2)

        soup = BeautifulSoup(page.text, "html.parser")

        frame = []

        links = soup.find_all("li", attrs={"class": "o-listicle__item"})

        print(len(links))

        for j in links:
            Statement = j.find(
                "div", attrs={"class": "m-statement__quote"}
            ).text.strip()

            Link = "https://www.politifact.com"

            Link += (
                j.find("div", attrs={"class": "m-statement__quote"})
                .find("a")["href"]
                .strip()
            )

            Date = (
                j.find("div", attrs={"class": "m-statement__body"})
                .find("footer")
                .text[-14:-1]
                .strip()
            )

            Source = (
                j.find("div", attrs={"class": "m-statement__author"})
                .find("a")
                .get("title")
                .strip()
            )

            Label = (
                j.find("div", attrs={"class": "m-statement__content"})
                .find("img", attrs={"class": "c-image__original"})
                .get("alt")
            )

            frame.append((Statement, Link, Date, Source, Label))

        upperframe.extend(frame)

        data = pd.DataFrame(
            upperframe, columns=["Statement", "Link", "Date", "Source", "Label"]
        )

        scrap_stamp = scrap_stamp or datetime.today().strftime("%Y-%m-%d")

        data["Scrapversion"] = scrap_stamp

        if not mongohost:
            data.to_csv("scrapped_data_folder/NEWS.csv", index=False)

        else:
            mongo_url = f"mongodb://root:example@{mongohost}"

            # Connect to MongoDB

            client = MongoClient(mongo_url)

            db = client["scrap_db"]

            collection = db["scrap_col"]

            documents_to_delete = {"Scrapversion": {"$eq": scrap_stamp}}

            collection.delete_many(documents_to_delete)

            data.reset_index(inplace=True)

            data_dict = data.to_dict("records")

            # Insert collection

            collection.insert_many(data_dict)
