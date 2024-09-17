from query_builder import QueryBuilder, ParentPlaceType, ContributorRole

query_builder = QueryBuilder()

queries = [
    query_builder.country("United States"),
    query_builder.state("California", "United States"),
    query_builder.state("Texas", "United States"),
    query_builder.state("New York", "United States"),
    query_builder.state("New Jersey", "United States"),
    query_builder.state("Washington", "United States"),
    query_builder.state("Massachusetts", "United States"),
    query_builder.state("New Mexico", "United States"),
    query_builder.state("Missouri", "United States"),
    query_builder.city("Sacramento", ParentPlaceType.STATE, "California"),
    query_builder.city("Los Angeles", ParentPlaceType.STATE, "California"),
    query_builder.city("San Francisco", ParentPlaceType.STATE, "California"),
    query_builder.city("Sevastopol", ParentPlaceType.STATE, "California"),
    query_builder.city("Austin", ParentPlaceType.STATE, "Texas"),
    query_builder.city("Albany", ParentPlaceType.STATE, "New York"),
    query_builder.city("New York City", ParentPlaceType.STATE, "New York"),
    query_builder.city("Trenton", ParentPlaceType.STATE, "New Jersey"),
    query_builder.city("Newark", ParentPlaceType.STATE, "New Jersey"),
    query_builder.city("Seattle", ParentPlaceType.STATE, "Washington"),
    query_builder.city("Boston", ParentPlaceType.STATE, "Massachusetts"),
    query_builder.city("Santa Fe", ParentPlaceType.STATE, "New Mexico"),
    query_builder.city("Albuquerque", ParentPlaceType.STATE, "New Mexico"),
    query_builder.city("Kansas City", ParentPlaceType.STATE, "Missouri"),
    query_builder.country("United Kingdom"),
    query_builder.city("London", ParentPlaceType.COUNTRY, "United Kingdom"),
    query_builder.city("Bristol", ParentPlaceType.COUNTRY, "United Kingdom"),
    query_builder.city("Liverpool", ParentPlaceType.COUNTRY, "United Kingdom"),
    query_builder.country("Canada"),
    query_builder.state("Ontario", "Canada"),
    query_builder.state("Quebec", "Canada"),
    query_builder.city("Toronto", ParentPlaceType.STATE, "Ontario"),
    query_builder.city("Quebec City", ParentPlaceType.STATE, "Quebec"),
    query_builder.city("Montreal", ParentPlaceType.STATE, "Quebec"),
    query_builder.paperback(
        "9780195153446",
        "Classical Mythology",
        820,
        "34.98",
        ["nonfiction", "history"],
        [("Morford, Mark P. O.", ContributorRole.AUTHOR), ("Lenardon, Robert J.", ContributorRole.AUTHOR)],
        "Oxford University Press",
        2002,
        "New York City",
        "0195153448",
    ),
    query_builder.hardback(
        "9780679425601",
        "Under the Black Flag: The Romance and the Reality of Life Among the Pirates",
        296,
        "34.73",
        ["nonfiction", "history"],
        [("Cordingly, David", ContributorRole.AUTHOR)],
        "Random House",
        1996,
        "New York City",
        "0679425608",
    ),
    query_builder.paperback(
        "9780393045215",
        "The Mummies of Urumchi",
        240,
        "21.60",
        ["nonfiction", "history"],
        [("Barber, Elizabeth Wayland", ContributorRole.AUTHOR)],
        "W.W. Norton & Company",
        1999,
        "New York City",
        "0393045218",
    ),
    query_builder.paperback(
        "9798691153570",
        "Business Secrets of The Pharoahs",
        260,
        "11.99",
        ["nonfiction", "business"],
        [("Crorigan, Mark", ContributorRole.AUTHOR)],
        "British London Publishing",
        2020,
        "London",
    ),
    query_builder.paperback(
        "9780446310789",
        "To Kill a Mockingbird",
        281,
        "21.64",
        ["fiction", "historical fiction"],
        [("Harper Lee", ContributorRole.AUTHOR)],
        "Grand Central Publishing",
        1988,
        "New York City",
        "0446310786",
    ),
    query_builder.paperback(
        "9780553212150",
        "Pride and Prejudice",
        295,
        "17.99",
        ["fiction", "historical fiction"],
        [("Austen, Jane", ContributorRole.AUTHOR)],
        "Bantam Classics",
        1983,
        "New York City",
        "055321215X"
    ),
    query_builder.ebook(
        "9783319398778",
        "Physical Principles of Electron Microscopy: An Introduction to TEM, SEM, and AEM",
        196,
        "19.50",
        ["nonfiction", "technology"],
        [("Egerton, R.F.", ContributorRole.AUTHOR)],
        "Springer",
        2016,
        "London",
    ),
    query_builder.hardback(
        "9780387881355",
        "Electron Backscatter Diffraction in Materials Science",
        425,
        "230.37",
        ["nonfiction", "technology"],
        [("Schwartz, Adam J.", ContributorRole.EDITOR), ("Kumar, Mukul", ContributorRole.EDITOR), ("Adams, Brent L.", ContributorRole.EDITOR), ("Field, David P.", ContributorRole.EDITOR)],
        "Springer",
        2009,
        "New York City",
        "0387881352",
    ),
    query_builder.paperback(
        "9781489962287",
        "Interpretation of Electron Diffraction Patterns",
        199,
        "47.17",
        ["nonfiction", "technology"],
        [("Andrews, Kenneth William", ContributorRole.AUTHOR), ("Dyson, David John", ContributorRole.AUTHOR), ("Keown, Samuel Robert", ContributorRole.AUTHOR)],
        "Springer",
        1967,
        "New York City",
        "148996228X",
    ),
    query_builder.paperback(
        "9780500026557",
        "Hokusai's Fuji",
        416,
        "24.47",
        ["nonfiction", "art"],
        [("Wada, Kyoko", ContributorRole.AUTHOR), ("Katsushika, Hokusai", ContributorRole.ILLUSTRATOR)],
        "Thames & Hudson",
        2024,
        "London",
        "0500026556",
    ),
    query_builder.paperback(
        "9780500291221",
        "Great Discoveries in Medicine",
        352,
        "12.05",
        ["nonfiction", "history"],
        [("Bynum, William", ContributorRole.EDITOR), ("Bynum, Helen", ContributorRole.EDITOR)],
        "Thames & Hudson",
        2023,
        "London",
        "0500291225",
    ),
    query_builder.hardback(
        "9780740748479",
        "The Complete Calvin and Hobbes",
        1451,
        "128.71",
        ["fiction", "comics"],
        [("Watterson, Bill", ContributorRole.AUTHOR), ("Watterson, Bill", ContributorRole.ILLUSTRATOR)],
        "Andrews McMeel Publishing",
        2005,
        "Kansas City",
        "0740748475",
    ),
    query_builder.ebook(
        "9780375801679",
        "The Iron Giant",
        79,
        "33.97",
        ["fiction", "children's fiction"],
        [("Hughes, Ted", ContributorRole.AUTHOR), ("Davidson, Andrew", ContributorRole.ILLUSTRATOR)],
        "Knopf Books for Young Readers",
        1999,
        "New York City",
        "0375801677",
    ),
    query_builder.paperback(
        "9781859840665",
        "The Motorcycle Diaries: A Journey Around South America",
        160,
        "14.52",
        ["nonfiction", "biography"],
        [("Guevara, Ernesto", ContributorRole.AUTHOR), ("Wright, Ann", ContributorRole.CONTRIBUTOR)],
        "Verso",
        1996,
        "London",
        "1859840663",
    ),
    query_builder.paperback(
        "9780671461492",
        "The Hitchhiker's Guide to the Galaxy",
        215,
        "91.47",
        ["fiction", "science fiction"],
        [("Adams, Douglas", ContributorRole.AUTHOR)],
        "Pocket",
        1982,
        "New York City",
        "0671461494",
    ),
    query_builder.paperback(
        "9780060929794",
        "One Hundred Years of Solitude",
        458,
        "6.12",
        ["fiction", "historical fiction"],
        [("Garcia Marquez, Gabriel", ContributorRole.AUTHOR)],
        "Perennial",
        1998,
        "New York City",
        "0060929790",
    ),
    query_builder.ebook(
        "9781098108274",
        "Fundamentals of Data Engineering",
        450,
        "47.99",
        ["nonfiction", "technology", "children's fiction"],
        [("Reis, Joe", ContributorRole.AUTHOR), ("Housley, Matt", ContributorRole.AUTHOR)],
        "O'Reilly Media",
        2022,
        "Sevastopol",
        "1098108272",
    ),
    query_builder.ebook(
        "9780393634563",
        "The Odyssey",
        656,
        "13.99",
        ["fiction", "classics"],
        [("Homer", ContributorRole.AUTHOR), ("Wilson, Emily", ContributorRole.CONTRIBUTOR)],
        "W.W. Norton & Company",
        2017,
        "New York City",
        "0393634566",
    ),
    query_builder.ebook(
        "9780575104419",
        "Dune",
        624,
        "5.49",
        ["fiction", "science fiction"],
        [("Herbert, Frank", ContributorRole.AUTHOR)],
        "Hachette Book Group",
        2010,
        "New York City",
        "0575104414",
    ),
    query_builder.ebook(
        "9780008627843",
        "The Hobbit",
        310,
        "16.99",
        ["fiction", "fantasy"],
        [("J.R.R. Tolkien", ContributorRole.AUTHOR), ("J.R.R. Tolkien", ContributorRole.ILLUSTRATOR)],
        "Harper Collins",
        2023,
        "New York City",
        "0008627843",
    ),
    query_builder.user("Kevin Morrison", "San Francisco"),  # "u0001"
    query_builder.user("Cameron Osborne", "Austin"),  # "u0002"
    query_builder.user("Keyla Pineda", "Newark"),  # "u0003"
    query_builder.user("Lorenzo Nixon", "Seattle"),  # "u0004"
    query_builder.user("Xavier Martinez", "Boston"),  # "u0005"
    query_builder.user("Giovanni Beard", "Santa Fe"),  # "u0006"
    query_builder.user("Skyler Townsend", "Toronto"),  # "u0007"
    query_builder.user("Alia Hartman", "Bristol"),  # "u0008"
    query_builder.user("Isaac Winters", "Montreal"),  # "u0009"
    query_builder.user("Madison Everett", "Liverpool"),  # "u0010"
    query_builder.order("14 South Street", "San Francisco", [2, 1], user_id="u0001"),
    query_builder.order("14 South Street", "San Francisco", [1], user_id="u0001"),
    query_builder.order("14 South Street", "San Francisco", [1], user_id="u0001"),
    query_builder.order("55 Park Road", "Austin", [1], user_id="u0002"),
    query_builder.order("55 Park Road", "Austin", [2], user_id="u0002"),
    query_builder.order("55 Park Road", "Austin", [2], user_id="u0002"),
    query_builder.order("55 Park Road", "Austin", [1], user_id="u0002"),
    query_builder.order("23 Grove Road", "Newark", [1, 1], user_id="u0003"),
    query_builder.order("9735 Queensway", "Seattle", [1, 1, 1], user_id="u0004"),
    query_builder.order("9735 Queensway", "Seattle", [1], user_id="u0004"),
    query_builder.order("64 Fremont Street", "Boston", [2], user_id="u0005"),
    query_builder.order("9227 Lincoln Street", "Santa Fe", [3], user_id="u0006"),
    query_builder.order("9227 Lincoln Street", "Santa Fe", [1, 1], user_id="u0006"),
    query_builder.order("9227 Lincoln Street", "Santa Fe", [2, 1], user_id="u0006"),
    query_builder.order("464 Pilgrim Lane", "Toronto", [1], user_id="u0007"),
    query_builder.order("464 Pilgrim Lane", "Toronto", [1, 1], user_id="u0007"),
    query_builder.order("75 Fairway Court", "Bristol", [1, 1], user_id="u0008"),
    query_builder.order("75 Fairway Court", "Bristol", [1], user_id="u0008"),
    query_builder.order("86 East Drive", "Montreal", [1], user_id="u0009"),
    query_builder.order("86 East Drive", "Montreal", [1], user_id="u0009"),
    query_builder.order("86 East Drive", "Montreal", [2], user_id="u0009"),
    query_builder.order("75 Selby Street", "Liverpool", [1, 1], user_id="u0010"),
    query_builder.order("75 Selby Street", "Liverpool", [1, 1], user_id="u0010"),
    query_builder.order("75 Selby Street", "Liverpool", [1], user_id="u0010"),
    query_builder.order("786 Lake View Street", "Sacramento", [1], user_id="u0005"),
    query_builder.order("786 Lake View Street", "Sacramento", [1], user_id="u0005"),
    query_builder.order("786 Lake View Street", "Sacramento", [1], user_id="u0005"),
    query_builder.order("8503 Second Street", "New York City", [2], user_id="u0003"),
    query_builder.order("8503 Second Street", "New York City", [1], user_id="u0003"),
    query_builder.order("826 Vermont Avenue", "Kansas City", [1], user_id="u0004"),
    query_builder.order("984 Williams Street", "Los Angeles", [1], user_id="u0001"),
    query_builder.order("984 Williams Street", "Los Angeles", [1, 1], user_id="u0001"),
    query_builder.order("20 Ridge Lane", "Quebec City", [1], user_id="u0007"),
    query_builder.order("20 Ridge Lane", "Quebec City", [1, 1], user_id="u0007"),
    query_builder.order("20 Ridge Lane", "Quebec City", [1], user_id="u0007"),
    query_builder.order("20 Ridge Lane", "Quebec City", [2], user_id="u0007"),
    query_builder.order("112 Church Street", "Albany", [1], user_id="u0003"),
    query_builder.order("112 Church Street", "Albany", [1, 1], user_id="u0003"),
    query_builder.review(4),
    query_builder.review(5),
    query_builder.review(5),
    query_builder.review(5),
    query_builder.review(6),
    query_builder.review(6),
    query_builder.review(6),
    query_builder.review(6),
    query_builder.review(6),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(7),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(8),
    query_builder.review(9),
    query_builder.review(9),
    query_builder.review(9),
    query_builder.review(9),
    query_builder.review(9),
    query_builder.review(9),
    query_builder.review(10),
    query_builder.review(10),
    query_builder.review(10),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.login(),
    query_builder.promotion(
        "HOL23",
        "Holiday Sale 2023",
        "2023-12-01T00:00:00",
        "2023-12-31T23:59:59",
        [("9780575104419", "0.25"), ("9780060929794", "0.25"), ("9780375801679", "0.25"), ("9780008627843", "0.25"), ("9780500026557", "0.25")]
    ),
    query_builder.paperback(
        "9780451162076",
        "Pet Sematary",
        374,
        "93.22",
        ["fiction", "horror"],
        [("King, Stephen", ContributorRole.AUTHOR)],
        "Signet",
        1984,
        "New York City",
        "0451162072",
    ),
]

with open("resources/copyright_statement.txt", "r") as copyright_file:
    copyright_statement = copyright_file.read()

with open("bookstore/queries.tql", "w") as output_file:
    output_file.write(copyright_statement + "\n")

    for query in queries:
        output_file.write("\n")
        output_file.write(query)
