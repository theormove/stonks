class Article:

    def __init__(self, title, link, image, text, tags, region):

        self.title = title
        self.link = link
        self.image = image
        self.text = text
        self.tags = tags
        self.region = region

    def __str__(self):

        rep = ""
        rep += "Title: " + self.title + "\n"
        rep += "Link : " + self.link + "\n"
        rep += "Image: " + self.image + "\n"
        rep += "Text: " + self.text[:50] + "... " + "\n"

        for tag in self.tags:
            rep += "Tags: " + tag + "\n"

        rep += "Region: " + self.region + "\n"

        return rep