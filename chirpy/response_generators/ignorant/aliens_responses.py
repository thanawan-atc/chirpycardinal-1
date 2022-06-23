PROMPT = "HI"

MONOLOGUES = {
    1: "HI"
}

for k, v in MONOLOGUES.items():
    MONOLOGUES[k] = ' '.join(v.split())

ELABORATE_TOPIC = {
    'IGNORANT_FILTER': {
        """
        HI
        """
    }
}

QUESTION_RESPONSE = "HI"


ACKNOWLEDGMENTS = [
    "HI"
]

if __name__ == '__main__':
    for i, v in MONOLOGUES.items():
        print(v)
        print()