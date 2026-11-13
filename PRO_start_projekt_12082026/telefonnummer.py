import pytest


def valider_telefonnummer(nummer, laengde=8, fjern_mellemrum=True):
    """
    Validerer et dansk telefonnummer.

    Et gyldigt telefonnummer:
    - består kun af cifre
    - er præcis 8 cifre langt
    - må gerne skrives med mellemrum, fx "12 34 56 78"

    Returnerer en tuple: (ok, besked, nummer)
    - ok:     True hvis nummeret er gyldigt, ellers False
    - besked: en fejlbesked, eller "" hvis nummeret er gyldigt
    - nummer: nummeret uden mellemrum, eller None hvis det er ugyldigt
    """
    if fjern_mellemrum:
        nummer = "".join(nummer.split())

    if nummer == "":
        return False, "Telefonnummeret er tomt", None
    if not nummer.isdigit():
        return False, "Telefonnummeret må kun indeholde cifre", None
    if len(nummer) < laengde:
        return (
            False,
            f"Telefonnummeret skal være {laengde} cifre (fik {len(nummer)})",
            None,
        )

    return True, "", nummer

@pytest.mark.parametrize(
    "nummber, forventet",
    [
        ("12121212",True),
        ("12 12 12 12",True),
        ("12h12121",False),
        ("121212", False),
        ("1212121212", False),
        ("True", False),
        ("None", False),
        (None, False),
        (True, False),
        ("", False),
    ],
)

def test_længde(nummber, forventet):
    status, msg, phonenumber = valider_telefonnummer(nummber)
    assert status == forventet