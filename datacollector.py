import argparse
from elasticsearch import Elasticsearch
import pandas as pd
import ast




def argumentParser():
    """Function for Parsing the arguments.
    """
    parser = argparse.ArgumentParser()
    rows = parser.add_argument("-r","--rows",type=int, default=50, help="Number of rows of data to be loaded.")
    index = parser.add_argument("-i","--index", type=str, default="instagram_profile", choices=[
        "instagram_profile", "youtube_profile", "tiktok_profile", "creator_db","twitch_profile"
    ], help="Select Index from the available indexes to be loaded.")
    fields = parser.add_argument("-f","--fields", type=str, default=None, help="Provide List of Fields to be loaded.")
    link = parser.add_argument("-l","--link", type=str, required=True, help="Host Url from where data should be loaded")
    username = parser.add_argument("-u", "--username", type=str, required=True, help="Username for the host provided.")
    password = parser.add_argument("-p", "--password", type=str, required=True, help="Password for the user in order to get authenticated.")
     
    return parser.parse_args()

def ApiCon(link, user, cred):
    """Function for establishing connection with ElasticSearch.
    """
    return Elasticsearch(link, basic_auth=(user, cred))


def main():
    """ Main Function that will actually load data.
    """

    #Calling the Argument Parser Function
    args = argumentParser()

    #Calling the ApiCon
    es_client = ApiCon(args.link, args.username, args.password)

    #query for elastic search
    doc = {
            "match_all":{}
        }

    #Checking whether fields are provide or not
    if args.fields:

        fields_list = ast.literal_eval(args.fields)
        res = es_client.search(index=args.index, query=doc, size=args.rows, _source=fields_list)

    else:
        res = es_client.search(index=args.index, query=doc, size=args.rows)

    hits = res["hits"]["hits"]
    data = [hit["_source"] for hit in hits]
    df = pd.DataFrame(data)
    print(df)




if __name__ == "__main__":
    """Calling the Main Function"""
    main()