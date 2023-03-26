from release_finder.release import latest_release, latest_release_date


def test_latest_release():
    results = latest_release("https://github.com/utmapp/UTM")
    assert results == "v4.1.6"


def test_latest_release_date():
    results = latest_release_date("https://github.com/utmapp/UTM")
    assert results == "2023-02-27T02:28:31Z"
