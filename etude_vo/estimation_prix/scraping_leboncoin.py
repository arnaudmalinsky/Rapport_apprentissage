from datetime import datetime
import rpa


"""
Ce code prend en entrée un url dirigeant vers une page Leboncoin dans laquelle tous les filtres de recherche sont indiqués.

Le code arpente ensuite toutes les pages disponibles (max 100)

Pour chaque page il copie et sauvegarde un json contenant les informations relatives à toutes les annonces de la page

Le code est transposable à n'importe quelle recherche Lebconcoin

Limite : les captures d'écrans devront être refaites lorsque qu'on change d'écran
"""

SEARCH_PRODUCT = "renault-zoe"
NB_PAGES = 100
CATCHUP_URL = "https://www.leboncoin.fr/recherche?category=2&text=zoe%20intens&brand=Renault&model=Zoe&vehicle_type=berline%2Ccitadine&fuel=4&gearbox=2&doors=5&regdate=2016-max&price=1000-max"
CATCHUP_IDX = 1


def init():
    rpa.init(visual_automation=True, chrome_browser=False)


def start_chrome():
    rpa.keyboard("[win]")
    rpa.keyboard("chrome[enter]")
    rpa.wait(delay_in_seconds=2)
    rpa.keyboard("[ctrl][shift]i")


def lbc_catchup(start_url):
    rpa.click("images/google-search-box.PNG")
    copy_paste(CATCHUP_URL)
    rpa.click("images/clear-network.png")
    rpa.click("images/rechercher.png")


def copy_paste(any_text):
    rpa.clipboard(any_text)
    rpa.keyboard("[ctrl]v")
    rpa.keyboard("[enter]")


def display_response_from_network():
    if rpa.present("images/clear-search.png"):
        rpa.click("images/clear-search.png")
    rpa.click("images/search-box.PNG")
    rpa.keyboard("search")
    rpa.click("images/search-network.PNG")
    rpa.click("images/response-network.PNG")


def save_to_clipboard():
    rpa.keyboard("[ctrl]a")
    rpa.keyboard("[ctrl]c")
    rpa.click("images/clear-search.png")
    rpa.click("images/clear-network.png")


def save_notepad(product, page_idx):
    rpa.keyboard("[win]")
    rpa.wait(delay_in_seconds=2)
    rpa.keyboard("notepad[enter]")
    rpa.wait(delay_in_seconds=2)
    rpa.keyboard("[ctrl]v")
    rpa.keyboard("[ctrl]s")
    rpa.keyboard(
        f"{product.lower()}-{page_idx}-{datetime.timestamp(datetime.now())}.json[enter]"
    )
    rpa.keyboard("[alt][f4]")


def got_to_next_page():
    rpa.click("images/js-box-click.PNG")
    copy_paste(
        "document.querySelector('div[data-qa-id=\"cta-save_search-button\"]').scrollIntoView(); window.scrollBy(0, -100)"
    )
    rpa.click("images/clear-network.png")
    rpa.click("images/next-page.png")


def close():
    rpa.close()


if __name__ == "__main__":
    init()
    start_chrome()
    lbc_catchup(CATCHUP_URL)
    for page_idx in range(CATCHUP_IDX, NB_PAGES):
        display_response_from_network()
        save_to_clipboard()
        save_notepad(SEARCH_PRODUCT, page_idx)
        got_to_next_page()
    close()
