big_referrers = (
            ('google.c', 'Google'),
            ('bing.com', 'Bing'),
            ('twitter.com', 'Twitter'),
            ('reddit.com', 'Reddit'),
            ('t.co', 'Twitter'),
            ('duckduckgo.com', 'DuckDuckGo')
        )


def normalize_referrer(referrer_url):
    for big_ref in big_referrers:
        if referrer_url.startswith(big_ref[0]):
            return big_ref[1]

    return referrer_url
