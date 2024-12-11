class Article:
    all = []  

    def __init__(self, author, magazine, title):
        if not isinstance(title, str)or not (5 <= len(title) <= 50):
            raise TypeError("Title must be a string")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        magazine._articles.append(self)
        author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ValueError("Title cannot be changed after initialization")


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author's name must be a string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise ValueError("Author's name cannot be changed once set")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")

        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Category cannot be empty")
        
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        
        result = [author for author, count in authors_count.items() if count > 2]
        return None if not result else result