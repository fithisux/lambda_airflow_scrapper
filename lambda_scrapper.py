from scrapping import scrapper


def lambda_handler(event, context):
    scrapper.do_scrapping(event["scrap_stamp"], "mongo")

    return "Scraping Done"
