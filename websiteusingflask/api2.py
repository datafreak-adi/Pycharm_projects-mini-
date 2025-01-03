import paralleldots
paralleldots.set_api_key("l5FfvHPnOjbNHimAflRTHBan0LnK0ZyIyG7AncK1cAs")

def sent(text):

    sentiment = paralleldots.sentiment(text)
    return sentiment
