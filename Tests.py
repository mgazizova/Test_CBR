from GoogleHomePage import GoogleHomePage


def test_case(browser):
    google_home_page = GoogleHomePage(browser)
    google_home_page.go_to_site()
    google_home_page.enter_word("Центральный банк РФ")
    google_search_results = google_home_page.search()

    cbr_page = google_search_results.select_cbr_site()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    assert "www.cbr.ru" in browser.current_url
    gratitude_page = cbr_page.go_to_reception().write_gratitude()
    gratitude_page.enter_message("случайный текст")
    gratitude_page.check_agreement_flag()
    browser.save_screenshot("gratitude.png")

    about_menu = gratitude_page.open_menu()
    warning_page = about_menu.select_about_warning()
    ru_text = warning_page.get_warning_text()
    warning_page.change_local()
    en_text = warning_page.get_warning_text()
    assert ru_text is not en_text

    browser.save_screenshot("warning.png")
