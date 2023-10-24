adjectives = [
    "admiring",
    "adoring",
    "affectionate",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "blissful",
    "bold",
    "boring",
    "brave",
    "charming",
    "clever",
    "cocky",
    "compassionate",
    "competent",
    "condescending",
    "confident",
    "cool",
    "cranky",
    "crazy",
    "dazzling",
    "determined",
    "distracted",
    "dreamy",
    "eager",
    "ecstatic",
    "elastic",
    "elated",
    "elegant",
    "eloquent",
    "epic",
    "fervent",
    "festive",
    "flamboyant",
    "focused",
    "friendly",
    "frosty",
    "gallant",
    "gifted",
    "goofy",
    "gracious",
    "happy",
    "hardcore",
    "hopeful",
    "hungry",
    "infallible",
    "inspiring",
    "jolly",
    "jovial",
    "keen",
    "kind",
    "laughing",
    "loving",
    "lucid",
    "magical",
    "modest",
    "musing",
    "mystifying",
    "naughty",
    "nervous",
    "nifty",
    "nostalgic",
    "objective",
    "optimistic",
    "peaceful",
    "pedantic",
    "pensive",
    "practical",
    "priceless",
    "quirky",
    "quizzical",
    "recursing",
    "relaxed",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "silly",
    "sleepy",
    "stoic",
    "stupefied",
    "suspicious",
    "sweet",
    "tender",
    "thirsty",
    "trusting",
    "unruffled",
    "upbeat",
    "vibrant",
    "vigilant",
    "vigorous",
    "wizardly",
    "wonderful",
    "xenodochial",
    "youthful",
    "zealous",
    "zen",
]

animals = [
    "alligator",
    "alpaca",
    "ant",
    "antelope",
    "ape",
    "armadillo",
    "baboon",
    "badger",
    "bat",
    "bear",
    "beaver",
    "bee",
    "beetle",
    "bison",
    "burro",
    "butterfly",
    "camel",
    "caribou",
    "buffalo",
    "cat",
    "cattle",
    "cheetah",
    "chimpanzee",
    "chinchilla",
    "cicada",
    "clam",
    "cockroach",
    "cod",
    "coyote",
    "crab",
    "cricket",
    "crocodile",
    "crow",
    "deer",
    "dinosaur",
    "dog",
    "dolphin",
    "donkey",
    "duck",
    "eagle",
    "eel",
    "elephant",
    "elk",
    "ferret",
    "fish",
    "fly",
    "fox",
    "frog",
    "gerbil",
    "giraffe",
    "gnat",
    "gnu",
    "goat",
    "goldfish",
    "goose",
    "gorilla",
    "grasshopper",
    "hamster",
    "hare",
    "guineapig",
    "hedgehog",
    "herring",
    "hippopotamus",
    "hornet",
    "horse",
    "hound",
    "hyena",
    "impala",
    "jackal",
    "jellyfish",
    "kangaroo",
    "koala",
    "leopard",
    "lion",
    "lizard",
    "llama",
    "locust",
    "louse",
    "macaw",
    "mallard",
    "mammoth",
    "manatee",
    "marten",
    "mink",
    "minnow",
    "mole",
    "monkey",
    "moose",
    "mosquito",
    "mouse",
    "mule",
    "muskrat",
    "otter",
    "ox",
    "oyster",
    "panda",
    "pig",
    "platypus",
    "porcupine",
    "porpoise",
    "prairiedog",
    "pug",
    "rabbit",
    "raccoon",
    "rat",
    "raven",
    "salmon",
    "sardine",
    "scorpion",
    "sealion",
    "seal",
    "shark",
    "sheep",
    "skunk",
    "snail",
    "snake",
    "spider",
    "termite",
    "tiger",
    "turtle",
    "walrus",
    "wasp",
    "weasel",
    "whale",
    "wolf",
    "worm",
    "yak",
    "yellowjacket",
    "zebra",
]


def get_all_nicknames():
    permutations = []
    for adjective in adjectives:
        for animal in animals:
            permutations.append(f"{adjective} {animal}")

    return permutations
