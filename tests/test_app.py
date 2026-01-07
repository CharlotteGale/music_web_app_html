from playwright.sync_api import Page, expect
import pytest

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Title: Mutter\nReleased: 2001",
        "Title: Rammstein\nReleased: 2019",
        "Title: Hypnotize\nReleased: 2005",
        "Title: Rumors\nReleased: 1977",
        "Title: Toxicity\nReleased: 2001"
    ])

# @pytest.mark.skip(reason="Waiting for AlbumRepository")
def test_get_albums_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    div_tag = page.locator("div")

    expect(h1_tag).to_have_text("Mutter")
    expect(div_tag).to_have_text("Release year: 2001\nArtist: Rammstein")