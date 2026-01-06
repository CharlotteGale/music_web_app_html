from playwright.sync_api import Page, expect

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/web_music_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tag = page.locator("div")
    expect(div_tag).to_have_text([
        "Title: Du Hast\nReleased: 1997",
        "Title: Sonne\nReleased: 2001",
        "Title: B.Y.O.B\nReleased: 2005",
        "Title: The Chain\nReleased: 1977",
        "Title: Toxicity\nReleased: 2001"
    ])