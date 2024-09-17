from query_builder import QueryBuilder
from enums import OrganisationType

query_builder = QueryBuilder()

queries = [
    query_builder.region("Americas", "plc-americas"),
    query_builder.region("North America", "plc-americas/northern-america", "plc-americas"),
    query_builder.country("United States", "plc-americas/northern-america/united-states", "plc-americas/northern-america", ["English"]),
    query_builder.state("California", "plc-americas/northern-america/united-states/california", "plc-americas/northern-america/united-states"),
    query_builder.state("Texas", "plc-americas/northern-america/united-states/texas", "plc-americas/northern-america/united-states"),
    query_builder.state("New York", "plc-americas/northern-america/united-states/new-york", "plc-americas/northern-america/united-states"),
    query_builder.state("New Jersey", "plc-americas/northern-america/united-states/new-jersey", "plc-americas/northern-america/united-states"),
    query_builder.state("Washington", "plc-americas/northern-america/united-states/washington", "plc-americas/northern-america/united-states"),
    query_builder.state("Massachusetts", "plc-americas/northern-america/united-states/massachusetts", "plc-americas/northern-america/united-states"),
    query_builder.state("New Mexico", "plc-americas/northern-america/united-states/new-mexico", "plc-americas/northern-america/united-states"),
    query_builder.state("Missouri", "plc-americas/northern-america/united-states/missouri", "plc-americas/northern-america/united-states"),
    query_builder.city("Sacramento", "plc-americas/northern-america/united-states/california/sacramento", "plc-americas/northern-america/united-states/california"),
    query_builder.city("Los Angeles", "plc-americas/northern-america/united-states/california/los-angeles", "plc-americas/northern-america/united-states/california"),
    query_builder.city("San Francisco", "plc-americas/northern-america/united-states/california/san-francisco", "plc-americas/northern-america/united-states/california"),
    query_builder.city("Sevastopol", "plc-americas/northern-america/united-states/california/sevastopol", "plc-americas/northern-america/united-states/california"),
    query_builder.city("Austin", "plc-americas/northern-america/united-states/texas/austin", "plc-americas/northern-america/united-states/texas"),
    query_builder.city("Albany", "plc-americas/northern-america/united-states/new-york/albany", "plc-americas/northern-america/united-states/new-york"),
    query_builder.city("New York City", "plc-americas/northern-america/united-states/new-york/new-york-city", "plc-americas/northern-america/united-states/new-york"),
    query_builder.city("Trenton", "plc-americas/northern-america/united-states/new-jersey/trenton", "plc-americas/northern-america/united-states/new-jersey"),
    query_builder.city("Newark", "plc-americas/northern-america/united-states/new-jersey/newark", "plc-americas/northern-america/united-states/new-jersey"),
    query_builder.city("Seattle", "plc-americas/northern-america/united-states/washington/seattle", "plc-americas/northern-america/united-states/washington"),
    query_builder.city("Boston", "plc-americas/northern-america/united-states/massachusetts/boston", "plc-americas/northern-america/united-states/massachusetts"),
    query_builder.city("Santa Fe", "plc-americas/northern-america/united-states/new-mexico/santa-fe", "plc-americas/northern-america/united-states/new-mexico"),
    query_builder.city("Albuquerque", "plc-americas/northern-america/united-states/new-mexico/albuquerque", "plc-americas/northern-america/united-states/new-mexico"),
    query_builder.city("Kansas City", "plc-americas/northern-america/united-states/missouri/kansas-city", "plc-americas/northern-america/united-states/missouri"),
    query_builder.region("Europe", "plc-europe"),
    query_builder.region("Northern Europe", "plc-europe/northern-europe", "plc-europe"),
    query_builder.country("United Kingdom", "plc-europe/northern-europe/united-kingdom", "plc-europe/northern-europe", ["English"]),
    query_builder.city("London", "plc-europe/northern-europe/united-kingdom/london", "plc-europe/northern-europe/united-kingdom"),
    query_builder.city("Bristol", "plc-europe/northern-europe/united-kingdom/bristol", "plc-europe/northern-europe/united-kingdom"),
    query_builder.city("Liverpool", "plc-europe/northern-europe/united-kingdom/liverpool", "plc-europe/northern-europe/united-kingdom"),
    query_builder.country("Canada", "plc-americas/northern-america/canada", "plc-americas/northern-america", ["English", "French"]),
    query_builder.state("Ontario", "plc-americas/northern-america/canada/ontario", "plc-americas/northern-america/canada"),
    query_builder.state("Quebec", "plc-americas/northern-america/canada/quebec", "plc-americas/northern-america/canada"),
    query_builder.city("Toronto", "plc-americas/northern-america/canada/ontario/toronto", "plc-americas/northern-america/canada/ontario"),
    query_builder.city("Quebec City", "plc-americas/northern-america/canada/quebec/quebec-city", "plc-americas/northern-america/canada/quebec"),
    query_builder.city("Montreal", "plc-americas/northern-america/canada/quebec/montreal", "plc-americas/northern-america/canada/quebec"),
    query_builder.landmark("The Rusty Mug Café"),
    query_builder.landmark("Evergreen Rooftop Bar"),
    query_builder.landmark("The Velvet Curtain Theatre"),
    query_builder.landmark("Maple & Pine Coffeehouse"),
    query_builder.landmark("The Broken Compass Pub"),
    query_builder.landmark("Crescent Bay Bistro"),
    query_builder.landmark("The Wishing Well Bar"),
    query_builder.landmark("Red Fern Park"),
    query_builder.landmark("The Silver Spoon Diner"),
    query_builder.landmark("Starlight Drive-In"),
    query_builder.landmark("Old Town Arcade"),
    query_builder.landmark("The Blue Finch Tavern"),
    query_builder.landmark("The Golden Hive Café"),
    query_builder.landmark("Oak & Lantern Inn"),
    query_builder.landmark("The Crystal Harbour Lounge"),
    query_builder.landmark("Eastwood Bowling Alley"),
    query_builder.landmark("The Foggy Pebble Pub"),
    query_builder.landmark("Lakeside Book Nook"),
    query_builder.landmark("The Hidden Gem Theatre"),
    query_builder.landmark("North Shore Surf Bar"),
    query_builder.landmark("The Walnut Grove Café"),
    query_builder.landmark("Blackbird Jazz Club"),
    query_builder.landmark("The Vintage Reel Cinema"),
    query_builder.landmark("The Fox & Whistle Tavern"),
    query_builder.landmark("The Lavender Room Café"),
    query_builder.landmark("Birchwood Bike Shop"),
    query_builder.landmark("The Shady Pines Grill"),
    query_builder.landmark("The Whistling Kettle Tearoom"),
    query_builder.landmark("Horizon Heights Bar"),
    query_builder.landmark("Pinecrest Playhouse"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.person("test bio"),
    query_builder.organisation(OrganisationType.COMPANY, "Quantum Synergy Solutions", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "BlueWave Analytics", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "Apex Global Enterprises", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "SilverLeaf Technologies", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "Horizon Innovations Group", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "Redwood Digital Labs", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "StellarVision Media", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "NorthStar Logistics Corp.", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "Pinnacle Ventures Ltd.", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COMPANY, "BrightPath Pharmaceuticals", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.CHARITY, "Bright Horizons Initiative", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.CHARITY, "Heartwell Relief Fund", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.CHARITY, "GreenSteps Environmental Trust", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COLLEGE, "Sterling Hills College", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.COLLEGE, "Northern Crest Academy", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.UNIVERSITY, "Westbridge University", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.UNIVERSITY, "Oakwood Institute of Technology", "test bio", ["test tag"]),
    query_builder.organisation(OrganisationType.UNIVERSITY, "Riverford University", "test bio", ["test tag"]),
    query_builder.group("The Urban Explorers Collective", "test bio", ["test tag"]),
    query_builder.group("Eco Warriors Network", "test bio", ["test tag"]),
    query_builder.group("The Coffee Connoisseurs Club", "test bio", ["test tag"]),
    query_builder.group("Digital Nomads Hub", "test bio", ["test tag"]),
    query_builder.group("Vintage Car Enthusiasts Society", "test bio", ["test tag"]),
]

for _ in range(30):
    queries.append(query_builder.education())
    queries.append(query_builder.employment())

for _ in range(50):
    queries.append(query_builder.group_membership())

for _ in range(200):
    queries.append(query_builder.social_relation())

with open("resources/copyright_statement.txt", "r") as copyright_file:
    copyright_statement = copyright_file.read()

with open("social_media/queries.tql", "w") as output_file:
    output_file.write(copyright_statement + "\n")

    for query in queries:
        output_file.write("\n")
        output_file.write(query)
