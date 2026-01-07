from playwright.sync_api import Page, expect

# ========================================================= #
# ==================     ALBUMS     ======================= #
# ========================================================= #

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tag = page.locator("h1")
    para_tag = page.locator("p")

    expect(h1_tag).to_have_text("Choose an Album")
    expect(para_tag).to_have_text([
        "Mutter",
        "Rammstein",
        "Hypnotize",
        "Rumors",
        "Toxicity"
    ], use_inner_text=True)

def test_show_albums_with_link_to_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    links = page.locator("a")

    expect(links.nth(0)).to_have_attribute("href", "/albums/1")
    expect(links.nth(1)).to_have_attribute("href", "/albums/2")
    expect(links.nth(2)).to_have_attribute("href", "/albums/3")
    expect(links.nth(3)).to_have_attribute("href", "/albums/4")
    expect(links.nth(4)).to_have_attribute("href", "/albums/5")


def test_get_albums_by_id_with_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    div_tag = page.locator("div")

    expect(h1_tag).to_have_text("Mutter")
    expect(div_tag).to_have_text("Release year: 2001\nArtist: Rammstein")

# ========================================================= #
# ===================    ARTISTS     ====================== #
# ========================================================= #
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    para_tag = page.locator("p")

    expect(h1_tag).to_have_text("Artists")
    expect(para_tag).to_have_text([
        "Rammstein",
        "System of a Down",
        "Fleetwood Mac"
    ], use_inner_text=True)

def test_show_artists_with_link_to_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    links = page.locator("a")

    expect(links.nth(0)).to_have_attribute("href", "/artists/1")
    expect(links.nth(1)).to_have_attribute("href", "/artists/2")
    expect(links.nth(2)).to_have_attribute("href", "/artists/3")

def test_artist_id_page(page,test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    div_tag = page.locator("div")

    expect(div_tag).to_have_text("Artist: Rammstein\nGenre: Heavy Metal")
    