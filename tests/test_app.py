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

def test_get_albums_by_id_with_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    release_year_element = page.locator(".release_year")
    album_artist_element = page.locator(".album-artist_name")

    expect(h1_tag).to_have_text("Mutter")
    expect(release_year_element).to_have_text("Release year: 2001")
    expect(album_artist_element).to_have_text("Artist: Rammstein")

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Add New Album")

    page.fill("input[name='title']", "Fleetwood Mac")
    page.fill("input[name='release_year']", "1975")

    page.click("text=Create Album")

    h1_tag = page.locator("h1")
    release_year_element = page.locator(".release_year")

    expect(h1_tag).to_have_text("Fleetwood Mac")
    expect(release_year_element).to_have_text("1975")
    




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

def test_artist_id_page(page,test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/artists/1")

    div_tag = page.locator("div")

    expect(div_tag).to_have_text("Artist: Rammstein\nGenre: Heavy Metal")
    