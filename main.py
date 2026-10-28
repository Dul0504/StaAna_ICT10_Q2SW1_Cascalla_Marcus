from pyscript import document


def candidate_checker(e):
    # list of club members, stored in "First Last" format
    club_members = [
        "Ramon Magsaysay",
        "Ryan Garcia",
        "Donya Victorina",
        "Dominic Torreto",
        "Peter Parker",
        "Otto Octavius",
        "Logan Howlett",
        "Yukio Tanaka",
        "Wade Wilson",
        "Finnick Odair",
        "Kat Stratford",
        "Patrick Verona",
        "Lucas Watanabe",
    ]

    # get the first and last name from the html inputs
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    # combine both into one full name, capitalized to match the list
    candidate_name = f"{f_name} {l_name}".title()

    # True if the full name is in the club members list, otherwise False
    checker = candidate_name in club_members

    # index 0 (False) = not on the list, index 1 (True) = member
    messages = (
        f"Sorry {candidate_name}, your name is not on the list.",
        f"Congratulations {candidate_name}! You are now part of the ICT club.",
    )

    # display the matching message in the result div
    document.getElementById("result_checker").innerHTML = messages[checker]