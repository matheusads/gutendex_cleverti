from mongoengine import (DecimalField, Document, EmbeddedDocument,
                         EmbeddedDocumentListField, IntField, ListField,
                         StringField)


class Review(EmbeddedDocument):
    rating = IntField()
    review = StringField()


class Author(EmbeddedDocument):
    name = StringField()
    birth_year = IntField()
    death_year = IntField()


class Books(Document):
    id = IntField(primary_key=True)
    title = StringField(required=True)
    languages = ListField(StringField(), required=True)
    authors = EmbeddedDocumentListField(Author)
    reviews = EmbeddedDocumentListField(Review)
    download_count = IntField(required=False)
    average_rating = DecimalField(required=False)
