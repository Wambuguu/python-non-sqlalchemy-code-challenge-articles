from collections import Counter

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__._all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def articles(self):
        return [article for article in Article._all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mag_categories = [article.magazine.category for article in self.articles()]
        return list(set(mag_categories)) if mag_categories else None


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article._all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = Counter(article.author for article in self.articles())
        return [author for author, count in authors.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        top_magazine = max(cls._all_magazines, key=lambda mag: len(mag.articles()))
        return top_magazine if top_magazine.articles() else None
