# ElasticSearchClient
This Repository contain script for loading data from ElasticSearch Client in python. The script utilizes ArgsParser to get various arguments.


### Version
1.0

### Requirement
Following are the requirements for this script is listed.
`
elasticsearch==8.8.2
pandas==2.0.3
`
These reqirements are listed in the requirements.txt file, and can be installed with the below commands
`pip3 install requirements.txt`


### Usage

1. Help:
    `python3 datacollector.py --help`

2. Execution with required parameter only
    `python3 datacollector.py -l="http://135.181.112.125:9315" -u="khurram_elastic" -p="3CePkTeu7s7&wiiKH"`

    `-l or --link, -u or --username, -p or --password  are the required parameters`

3. Several other arguments can also be passed and these are:
    ```optional arguments:
    -h, --help            show this help message and exit
    -r ROWS, --rows ROWS  Number of rows of data to be loaded.
    -i {instagram_profile,youtube_profile,tiktok_profile,creator_db,twitch_profile}, --index {instagram_profile,youtube_profile,tiktok_profile,creator_db,twitch_profile}
                            Select Index from the available indexes to be loaded.
    -f FIELDS, --fields FIELDS
                            Provide List of Fields to be loaded.
    -l LINK, --link LINK  Host Url from where data should be loaded
    -u USERNAME, --username USERNAME
                            Username for the host provided.
    -p PASSWORD, --password PASSWORD
                            Password for the user in order to get authenticated.```
