from scrapping import scrapper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrap news.")
    parser.add_argument(
        "-m",
        "--mongohost",
        action="store",
        dest="mongohost",
        default=None,
        help="Shall we use some mongo host or just crawl to scrapped_data_folder (file system)?",
    )
    args = parser.parse_args()
    scrapper.do_scrapping(mongohost=args.mongohost)
