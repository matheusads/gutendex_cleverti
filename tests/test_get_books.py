from unittest.mock import Mock, patch

from app.main import app
from fastapi.testclient import TestClient
from requests.exceptions import HTTPError

client = TestClient(app)


def success_returned_value():
    return {
        "count":
        68800,
        "next":
        "https://gutendex.com/books/?page=2",
        "previous":
        None,
        "results": [{
            "id":
            1342,
            "title":
            "Pride and Prejudice",
            "authors": [{
                "name": "Austen, Jane",
                "birth_year": 1775,
                "death_year": 1817
            }],
            "translators": [],
            "subjects": [
                "Courtship -- Fiction", "Domestic fiction",
                "England -- Fiction", "Love stories", "Sisters -- Fiction",
                "Social classes -- Fiction", "Young women -- Fiction"
            ],
            "bookshelves": ["Best Books Ever Listings", "Harvard Classics"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1342.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1342.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1342.rdf",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm",
                "application/zip":
                "https://www.gutenberg.org/files/1342/1342-h.zip",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1342/1342-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1342/pg1342.cover.medium.jpg",
                "text/html":
                "https://www.gutenberg.org/ebooks/1342.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            1661,
            "title":
            "The Adventures of Sherlock Holmes",
            "authors": [{
                "name": "Doyle, Arthur Conan",
                "birth_year": 1859,
                "death_year": 1930
            }],
            "translators": [],
            "subjects": [
                "Detective and mystery stories, English",
                "Holmes, Sherlock (Fictitious character) -- Fiction",
                "Private investigators -- England -- Fiction"
            ],
            "bookshelves": [
                "Banned Books from Anne Haight's list", "Contemporary Reviews",
                "Detective Fiction"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1661.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1661.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1661.kindle.images",
                "application/zip":
                "https://www.gutenberg.org/files/1661/1661-h.zip",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1661/pg1661.cover.medium.jpg",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1661/1661-0.txt",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1661/1661-h/1661-h.htm",
                "text/html":
                "https://www.gutenberg.org/ebooks/1661.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            11,
            "title":
            "Alice's Adventures in Wonderland",
            "authors": [{
                "name": "Carroll, Lewis",
                "birth_year": 1832,
                "death_year": 1898
            }],
            "translators": [],
            "subjects": [
                "Alice (Fictitious character from Carroll) -- Juvenile fiction",
                "Children's stories", "Fantasy fiction",
                "Imaginary places -- Juvenile fiction"
            ],
            "bookshelves": ["Children's Literature"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/11.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/11.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/11.kindle.images",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/11/11-h/11-h.htm",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/11/11-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/11/pg11.cover.medium.jpg",
                "text/html": "https://www.gutenberg.org/ebooks/11.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            84,
            "title":
            "Frankenstein; Or, The Modern Prometheus",
            "authors": [{
                "name": "Shelley, Mary Wollstonecraft",
                "birth_year": 1797,
                "death_year": 1851
            }],
            "translators": [],
            "subjects": [
                "Frankenstein's monster (Fictitious character) -- Fiction",
                "Frankenstein, Victor (Fictitious character) -- Fiction",
                "Gothic fiction", "Horror tales", "Monsters -- Fiction",
                "Science fiction", "Scientists -- Fiction"
            ],
            "bookshelves": [
                "Gothic Fiction", "Movie Books",
                "Precursors of Science Fiction", "Science Fiction by Women"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/84.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/84.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/84.kindle.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/84/84-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/84/84-h/84-h.htm",
                "text/html": "https://www.gutenberg.org/ebooks/84.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            505,
            "title":
            "History of the Warfare of Science with Theology in Christendom",
            "authors": [{
                "name": "White, Andrew Dickson",
                "birth_year": 1832,
                "death_year": 1918
            }],
            "translators": [],
            "subjects": ["Religion and science -- History"],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/505.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/505.rdf",
                "text/plain": "https://www.gutenberg.org/ebooks/505.txt.utf-8",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/505.kindle.images",
                "text/html; charset=us-ascii":
                "https://www.gutenberg.org/files/505/505-h/505-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/505/pg505.cover.medium.jpg",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/505/505.txt",
                "text/html": "https://www.gutenberg.org/ebooks/505.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            27107,
            "title":
            "金雲翹傳",
            "authors": [{
                "name": "Qingxincairen",
                "birth_year": None,
                "death_year": None
            }],
            "translators": [],
            "subjects": [],
            "bookshelves": [],
            "languages": ["zh"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/27107.epub.images",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/27107.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/27107.rdf",
                "text/html":
                "https://www.gutenberg.org/ebooks/27107.html.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/27107/27107-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/27107/pg27107.cover.small.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            345,
            "title":
            "Dracula",
            "authors": [{
                "name": "Stoker, Bram",
                "birth_year": 1847,
                "death_year": 1912
            }],
            "translators": [],
            "subjects": [
                "Dracula, Count (Fictitious character) -- Fiction",
                "Epistolary fiction", "Gothic fiction", "Horror tales",
                "Transylvania (Romania) -- Fiction", "Vampires -- Fiction",
                "Whitby (England) -- Fiction"
            ],
            "bookshelves":
            ["Gothic Fiction", "Horror", "Movie Books", "Mystery Fiction"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/plain":
                "https://www.gutenberg.org/ebooks/345.txt.utf-8",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/345.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/345.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/345.kindle.images",
                "text/html":
                "https://www.gutenberg.org/files/345/345-h/345-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/345/pg345.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/345/345-0.zip",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/345/345-0.txt"
            },
            "download_count":
            1000
        }, {
            "id":
            2701,
            "title":
            "Moby Dick; Or, The Whale",
            "authors": [{
                "name": "Melville, Herman",
                "birth_year": 1819,
                "death_year": 1891
            }],
            "translators": [],
            "subjects": [
                "Adventure stories",
                "Ahab, Captain (Fictitious character) -- Fiction",
                "Mentally ill -- Fiction", "Psychological fiction",
                "Sea stories", "Ship captains -- Fiction", "Whales -- Fiction",
                "Whaling -- Fiction", "Whaling ships -- Fiction"
            ],
            "bookshelves": ["Best Books Ever Listings"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/2701/2701-h/2701-h.htm",
                "application/zip":
                "https://www.gutenberg.org/files/2701/2701-0.zip",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/2701.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/2701.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/2701.epub.images",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/2701/pg2701.cover.medium.jpg",
                "text/html":
                "https://www.gutenberg.org/ebooks/2701.html.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/2701/2701-0.txt"
            },
            "download_count":
            1000
        }, {
            "id":
            174,
            "title":
            "The Picture of Dorian Gray",
            "authors": [{
                "name": "Wilde, Oscar",
                "birth_year": 1854,
                "death_year": 1900
            }],
            "translators": [],
            "subjects": [
                "Appearance (Philosophy) -- Fiction",
                "Conduct of life -- Fiction", "Didactic fiction",
                "Great Britain -- History -- Victoria, 1837-1901 -- Fiction",
                "London (England) -- History -- 1800-1950 -- Fiction",
                "Paranormal fiction", "Portraits -- Fiction",
                "Supernatural -- Fiction"
            ],
            "bookshelves": ["Gothic Fiction", "Movie Books"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/174.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/174.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/174.kindle.images",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/174/pg174.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/174/174-0.zip",
                "text/html":
                "https://www.gutenberg.org/files/174/174-h/174-h.htm",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/174/174-0.txt",
                "text/plain": "https://www.gutenberg.org/ebooks/174.txt.utf-8"
            },
            "download_count":
            1000
        }, {
            "id":
            98,
            "title":
            "A Tale of Two Cities",
            "authors": [{
                "name": "Dickens, Charles",
                "birth_year": 1812,
                "death_year": 1870
            }],
            "translators": [],
            "subjects": [
                "British -- France -- Paris -- Fiction",
                "Executions and executioners -- Fiction",
                "France -- History -- Revolution, 1789-1799 -- Fiction",
                "French -- England -- London -- Fiction", "Historical fiction",
                "London (England) -- History -- 18th century -- Fiction",
                "Lookalikes -- Fiction",
                "Paris (France) -- History -- 1789-1799 -- Fiction",
                "War stories"
            ],
            "bookshelves": ["Historical Fiction"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/98.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/98.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/98.kindle.images",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/98/98-h/98-h.htm",
                "text/html":
                "https://www.gutenberg.org/ebooks/98.html.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/98/98-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/98/pg98.cover.medium.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            33283,
            "title":
            "Calculus Made Easy: Being a very-simplest introduction to those beautiful methods which are generally "
            "called by the terrifying names of the Differential Calculus and the Integral Calculus",
            "authors": [{
                "name": "Thompson, Silvanus P. (Silvanus Phillips)",
                "birth_year": 1851,
                "death_year": 1916
            }],
            "translators": [],
            "subjects": ["Calculus"],
            "bookshelves": ["Mathematics"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/prs.tex":
                "https://www.gutenberg.org/files/33283/33283-t/33283-t.tex",
                "application/octet-stream":
                "https://www.gutenberg.org/files/33283/33283-pdf.zip",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/33283/pg33283.cover.medium.jpg",
                "application/pdf":
                "https://www.gutenberg.org/files/33283/33283-pdf.pdf",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/33283.rdf"
            },
            "download_count":
            1000
        }, {
            "id":
            4300,
            "title":
            "Ulysses",
            "authors": [{
                "name": "Joyce, James",
                "birth_year": 1882,
                "death_year": 1941
            }],
            "translators": [],
            "subjects": [
                "Alienation (Social psychology) -- Fiction",
                "Artists -- Fiction", "City and town life -- Fiction",
                "Domestic fiction", "Dublin (Ireland) -- Fiction",
                "Epic literature", "Jewish men -- Fiction",
                "Male friendship -- Fiction", "Married people -- Fiction",
                "Psychological fiction"
            ],
            "bookshelves": [
                "Banned Books List from the American Library Association",
                "Banned Books from Anne Haight's list",
                "Best Books Ever Listings", "Erotic Fiction"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/4300/pg4300.cover.medium.jpg",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/4300.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/4300.epub.images",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/4300.kindle.images",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/4300/4300-h.zip",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/4300/4300-0.txt",
                "application/zip":
                "https://www.gutenberg.org/files/4300/4300-0.zip",
                "text/html":
                "https://www.gutenberg.org/ebooks/4300.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            1952,
            "title":
            "The Yellow Wallpaper",
            "authors": [{
                "name": "Gilman, Charlotte Perkins",
                "birth_year": 1860,
                "death_year": 1935
            }],
            "translators": [],
            "subjects": [
                "Feminist fiction", "Married women -- Psychology -- Fiction",
                "Mentally ill women -- Fiction", "Psychological fiction",
                "Sex role -- Fiction"
            ],
            "bookshelves": ["Gothic Fiction"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1952/1952-0.txt",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1952.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1952.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1952.epub.images",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1952/1952-h/1952-h.htm",
                "application/zip":
                "https://www.gutenberg.org/files/1952/1952-h.zip",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1952/pg1952.cover.medium.jpg",
                "text/html":
                "https://www.gutenberg.org/ebooks/1952.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            1184,
            "title":
            "The Count of Monte Cristo, Illustrated",
            "authors": [{
                "name": "Dumas, Alexandre",
                "birth_year": 1802,
                "death_year": 1870
            }],
            "translators": [],
            "subjects": [
                "Adventure stories",
                "Dantès, Edmond (Fictitious character) -- Fiction",
                "France -- History -- 19th century -- Fiction",
                "Historical fiction", "Pirates -- Fiction",
                "Prisoners -- Fiction", "Revenge -- Fiction"
            ],
            "bookshelves": ["Adventure", "Movie Books"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html":
                "https://www.gutenberg.org/files/1184/1184-h/1184-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1184/pg1184.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/1184/1184-0.zip",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1184.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1184.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1184.rdf",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/1184/1184-0.txt",
                "text/plain": "https://www.gutenberg.org/ebooks/1184.txt.utf-8"
            },
            "download_count":
            1000
        }, {
            "id":
            105,
            "title":
            "Persuasion",
            "authors": [{
                "name": "Austen, Jane",
                "birth_year": 1775,
                "death_year": 1817
            }],
            "translators": [],
            "subjects": [
                "Dysfunctional families -- Fiction",
                "England -- Social life and customs -- 19th century -- Fiction",
                "First loves -- Fiction", "Love stories",
                "Motherless families -- Fiction", "Psychological fiction",
                "Regency fiction", "Rejection (Psychology) -- Fiction",
                "Ship captains -- Fiction", "Young women -- Fiction"
            ],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/105.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/105.rdf",
                "text/plain":
                "https://www.gutenberg.org/ebooks/105.txt.utf-8",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/105.kindle.images",
                "text/html; charset=iso-8859-1":
                "https://www.gutenberg.org/3/1/1/0/31100/31100-h.zip",
                "text/html":
                "https://www.gutenberg.org/files/105/105-h/105-h.htm",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/105/105-0.txt",
                "application/octet-stream":
                "https://www.gutenberg.org/files/105/105-0.zip",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/105/pg105.cover.medium.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            1232,
            "title":
            "The Prince",
            "authors": [{
                "name": "Machiavelli, Niccolò",
                "birth_year": 1469,
                "death_year": 1527
            }],
            "translators": [{
                "name": "Marriott, W. K. (William Kenaz)",
                "birth_year": None,
                "death_year": 1927
            }],
            "subjects": [
                "Political ethics -- Early works to 1800",
                "Political science -- Philosophy -- Early works to 1800",
                "State, The -- Early works to 1800"
            ],
            "bookshelves": [
                "Banned Books from Anne Haight's list", "Harvard Classics",
                "Philosophy", "Politics"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/octet-stream":
                "https://www.gutenberg.org/files/1232/1232-0.zip",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1232.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1232.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1232.rdf",
                "text/html":
                "https://www.gutenberg.org/files/1232/1232-h/1232-h.htm",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/1232/1232-0.txt",
                "text/plain":
                "https://www.gutenberg.org/ebooks/1232.txt.utf-8",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1232/pg1232.cover.medium.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            64317,
            "title":
            "The Great Gatsby",
            "authors": [{
                "name": "Fitzgerald, F. Scott (Francis Scott)",
                "birth_year": 1896,
                "death_year": 1940
            }],
            "translators": [],
            "subjects": [
                "First loves -- Fiction", "Long Island (N.Y.) -- Fiction",
                "Married women -- Fiction", "Psychological fiction",
                "Rich people -- Fiction"
            ],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/64317.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/64317.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/64317.epub.images",
                "text/html":
                "https://www.gutenberg.org/files/64317/64317-h/64317-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/64317/pg64317.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/64317/64317-0.zip",
                "text/plain":
                "https://www.gutenberg.org/ebooks/64317.txt.utf-8",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/64317/64317-0.txt"
            },
            "download_count":
            1000
        }, {
            "id":
            2600,
            "title":
            "War and Peace",
            "authors": [{
                "name": "Tolstoy, Leo, graf",
                "birth_year": 1828,
                "death_year": 1910
            }],
            "translators": [{
                "name": "Maude, Aylmer",
                "birth_year": 1858,
                "death_year": 1938
            }, {
                "name": "Maude, Louise",
                "birth_year": 1855,
                "death_year": 1939
            }],
            "subjects": [
                "Aristocracy (Social class) -- Russia -- Fiction",
                "Historical fiction",
                "Napoleonic Wars, 1800-1815 -- Campaigns -- Russia -- Fiction",
                "Russia -- History -- Alexander I, 1801-1825 -- Fiction",
                "War stories"
            ],
            "bookshelves": [
                "Best Books Ever Listings", "Historical Fiction",
                "Movie Books", "Napoleonic(Bookshelf)", "Opera"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/2600/pg2600.cover.medium.jpg",
                "text/plain":
                "https://www.gutenberg.org/ebooks/2600.txt.utf-8",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/2600.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/2600.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/2600.rdf",
                "text/html":
                "https://www.gutenberg.org/files/2600/2600-h/2600-h.htm",
                "application/octet-stream":
                "https://www.gutenberg.org/files/2600/2600-0.zip",
                "application/zip":
                "https://www.gutenberg.org/files/2600/2600-h.zip",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/2600/2600-0.txt"
            },
            "download_count":
            1000
        }, {
            "id":
            2554,
            "title":
            "Crime and Punishment",
            "authors": [{
                "name": "Dostoyevsky, Fyodor",
                "birth_year": 1821,
                "death_year": 1881
            }],
            "translators": [{
                "name": "Garnett, Constance",
                "birth_year": 1861,
                "death_year": 1946
            }],
            "subjects": [
                "Crime -- Psychological aspects -- Fiction",
                "Detective and mystery stories", "Murder -- Fiction",
                "Psychological fiction", "Saint Petersburg (Russia) -- Fiction"
            ],
            "bookshelves":
            ["Best Books Ever Listings", "Crime Fiction", "Harvard Classics"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/2554.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/2554.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/2554.rdf",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/2554/pg2554.cover.small.jpg",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/2554/2554-0.zip",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/2554/2554-h/2554-h.htm",
                "text/html":
                "https://www.gutenberg.org/ebooks/2554.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            2591,
            "title":
            "Grimms' Fairy Tales",
            "authors": [{
                "name": "Grimm, Wilhelm",
                "birth_year": 1786,
                "death_year": 1859
            }, {
                "name": "Grimm, Jacob",
                "birth_year": 1785,
                "death_year": 1863
            }],
            "translators": [],
            "subjects": ["Fairy tales -- Germany"],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/2591/2591-h/2591-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/2591/pg2591.cover.small.jpg",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/2591/2591-0.zip",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/2591.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/2591.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/2591.rdf",
                "text/html":
                "https://www.gutenberg.org/ebooks/2591.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            30254,
            "title":
            "The Romance of Lust: A classic Victorian erotic novel",
            "authors": [{
                "name": "Anonymous",
                "birth_year": None,
                "death_year": None
            }],
            "translators": [],
            "subjects": [
                "Corporal punishment -- Fiction", "Erotic stories",
                "Incest -- Fiction", "Pornography", "Rape -- Fiction",
                "Sexual dominance and submission -- Fiction"
            ],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/30254/30254-h/30254-h.htm",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/30254.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/30254.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/30254.epub.images",
                "application/zip":
                "https://www.gutenberg.org/files/30254/30254-h.zip",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/30254/30254-0.txt",
                "text/html":
                "https://www.gutenberg.org/ebooks/30254.html.images",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/30254/pg30254.cover.medium.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            1260,
            "title":
            "Jane Eyre: An Autobiography",
            "authors": [{
                "name": "Brontë, Charlotte",
                "birth_year": 1816,
                "death_year": 1855
            }],
            "translators": [],
            "subjects": [
                "Bildungsromans", "Charity-schools -- Fiction",
                "Country homes -- Fiction", "England -- Fiction",
                "Fathers and daughters -- Fiction", "Governesses -- Fiction",
                "Love stories", "Married people -- Fiction",
                "Mentally ill women -- Fiction", "Orphans -- Fiction",
                "Young women -- Fiction"
            ],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1260/1260-h/1260-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1260/pg1260.cover.medium.jpg",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1260.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1260.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1260.epub.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1260/1260-0.txt",
                "text/html":
                "https://www.gutenberg.org/ebooks/1260.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            6130,
            "title":
            "The Iliad",
            "authors": [{
                "name": "Homer",
                "birth_year": -750,
                "death_year": -650
            }],
            "translators": [{
                "name": "Pope, Alexander",
                "birth_year": 1688,
                "death_year": 1744
            }],
            "subjects": [
                "Achilles (Mythological character) -- Poetry",
                "Classical literature",
                "Epic poetry, Greek -- Translations into English",
                "Trojan War -- Poetry"
            ],
            "bookshelves": ["Classical Antiquity"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/6130/6130-0.txt",
                "text/plain":
                "https://www.gutenberg.org/ebooks/6130.txt.utf-8",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/6130.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/6130.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/6130.rdf",
                "text/html":
                "https://www.gutenberg.org/files/6130/6130-h/6130-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/6130/pg6130.cover.small.jpg",
                "application/zip":
                "https://www.gutenberg.org/files/6130/6130-h.zip"
            },
            "download_count":
            1000
        }, {
            "id":
            1400,
            "title":
            "Great Expectations",
            "authors": [{
                "name": "Dickens, Charles",
                "birth_year": 1812,
                "death_year": 1870
            }],
            "translators": [],
            "subjects": [
                "Benefactors -- Fiction", "Bildungsromans",
                "England -- Fiction", "Ex-convicts -- Fiction",
                "Man-woman relationships -- Fiction", "Orphans -- Fiction",
                "Revenge -- Fiction", "Young men -- Fiction"
            ],
            "bookshelves": ["Best Books Ever Listings"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1400.kindle.images",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1400.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1400.rdf",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1400/1400-0.zip",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1400/pg1400.cover.small.jpg",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1400/1400-h/1400-h.htm",
                "text/html":
                "https://www.gutenberg.org/ebooks/1400.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            43,
            "title":
            "The Strange Case of Dr. Jekyll and Mr. Hyde",
            "authors": [{
                "name": "Stevenson, Robert Louis",
                "birth_year": 1850,
                "death_year": 1894
            }],
            "translators": [],
            "subjects": [
                "Horror tales", "London (England) -- Fiction",
                "Multiple personality -- Fiction", "Physicians -- Fiction",
                "Psychological fiction", "Science fiction",
                "Self-experimentation in medicine -- Fiction"
            ],
            "bookshelves":
            ["Horror", "Movie Books", "Precursors of Science Fiction"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/43/43-h/43-h.htm",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/43.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/43.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/43.kindle.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/43/43-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/43/pg43.cover.medium.jpg",
                "text/html": "https://www.gutenberg.org/ebooks/43.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            5200,
            "title":
            "Metamorphosis",
            "authors": [{
                "name": "Kafka, Franz",
                "birth_year": 1883,
                "death_year": 1924
            }],
            "translators": [{
                "name": "Wyllie, David (Translator)",
                "birth_year": None,
                "death_year": None
            }],
            "subjects": ["Metamorphosis -- Fiction", "Psychological fiction"],
            "bookshelves": ["Horror"],
            "languages": ["en"],
            "copyright":
            True,
            "media_type":
            "Text",
            "formats": {
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/5200/pg5200.cover.medium.jpg",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/5200/5200-0.txt",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/5200.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/5200.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/5200.kindle.images",
                "text/html; charset=iso-8859-1":
                "https://www.gutenberg.org/files/5200/5200-h/5200-h.htm",
                "application/zip":
                "https://www.gutenberg.org/files/5200/5200-0.zip",
                "text/html":
                "https://www.gutenberg.org/ebooks/5200.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            1080,
            "title":
            "A Modest Proposal: For preventing the children of poor people in Ireland, from being a burden on their "
            "parents or country, and for making them beneficial to the publick",
            "authors": [{
                "name": "Swift, Jonathan",
                "birth_year": 1667,
                "death_year": 1745
            }],
            "translators": [],
            "subjects": [
                "Ireland -- Politics and government -- 18th century -- Humor",
                "Political satire, English", "Religious satire, English"
            ],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/1080/1080-h/1080-h.htm",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/1080.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/1080.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/1080.epub.images",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/1080/pg1080.cover.medium.jpg",
                "text/html":
                "https://www.gutenberg.org/ebooks/1080.html.images",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/1080/1080-0.txt"
            },
            "download_count":
            1000
        }, {
            "id":
            74,
            "title":
            "The Adventures of Tom Sawyer, Complete",
            "authors": [{
                "name": "Twain, Mark",
                "birth_year": 1835,
                "death_year": 1910
            }],
            "translators": [],
            "subjects": [
                "Adventure stories", "Bildungsromans", "Boys -- Fiction",
                "Child witnesses -- Fiction", "Humorous stories",
                "Male friendship -- Fiction",
                "Mississippi River Valley -- Fiction", "Missouri -- Fiction",
                "Runaway children -- Fiction",
                "Sawyer, Tom (Fictitious character) -- Fiction"
            ],
            "bookshelves": [
                "Banned Books List from the American Library Association",
                "Banned Books from Anne Haight's list"
            ],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/74.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/74.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/74.kindle.images",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/74/74-h/74-h.htm",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/74/74-0.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/74/pg74.cover.medium.jpg",
                "text/html": "https://www.gutenberg.org/ebooks/74.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            58585,
            "title":
            "The Prophet",
            "authors": [{
                "name": "Gibran, Kahlil",
                "birth_year": 1883,
                "death_year": 1931
            }],
            "translators": [],
            "subjects": ["Mysticism -- Poetry", "Prose poems, American"],
            "bookshelves": [],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "text/html":
                "https://www.gutenberg.org/files/58585/58585-h/58585-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/58585/pg58585.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/58585/58585-0.zip",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/58585.epub.images",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/58585.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/58585.rdf",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/58585/58585-0.txt",
                "text/plain":
                "https://www.gutenberg.org/ebooks/58585.txt.utf-8"
            },
            "download_count":
            1000
        }, {
            "id":
            13790,
            "title":
            "Life And Letters Of John Gay (1685-1732), Author of \"The Beggar's Opera\"",
            "authors": [{
                "name": "Melville, Lewis",
                "birth_year": 1874,
                "death_year": 1932
            }],
            "translators": [],
            "subjects": [
                "Authors, English -- 18th century -- Biography",
                "Gay, John, 1685-1732"
            ],
            "bookshelves": ["Opera"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/13790.kindle.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/13790.rdf",
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/13790.epub.images",
                "text/plain":
                "https://www.gutenberg.org/ebooks/13790.txt.utf-8",
                "text/html":
                "https://www.gutenberg.org/ebooks/13790.html.images",
                "text/html; charset=iso-8859-1":
                "https://www.gutenberg.org/files/13790/13790-h/13790-h.htm",
                "application/zip":
                "https://www.gutenberg.org/files/13790/13790-8.zip",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/13790/13790.txt",
                "text/plain; charset=iso-8859-1":
                "https://www.gutenberg.org/files/13790/13790-8.txt",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/13790/pg13790.cover.small.jpg"
            },
            "download_count":
            1000
        }, {
            "id":
            35,
            "title":
            "The Time Machine",
            "authors": [{
                "name": "Wells, H. G. (Herbert George)",
                "birth_year": 1866,
                "death_year": 1946
            }],
            "translators": [],
            "subjects": [
                "Dystopias -- Fiction", "Science fiction",
                "Time travel -- Fiction"
            ],
            "bookshelves": ["Movie Books", "Science Fiction"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/35.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/35.rdf",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/35.kindle.images",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/35/pg35.cover.medium.jpg",
                "text/plain; charset=utf-8":
                "https://www.gutenberg.org/files/35/35-0.txt",
                "text/html; charset=utf-8":
                "https://www.gutenberg.org/files/35/35-h/35-h.htm",
                "text/html": "https://www.gutenberg.org/ebooks/35.html.images"
            },
            "download_count":
            1000
        }, {
            "id":
            514,
            "title":
            "Little Women",
            "authors": [{
                "name": "Alcott, Louisa May",
                "birth_year": 1832,
                "death_year": 1888
            }],
            "translators": [],
            "subjects": [
                "Autobiographical fiction", "Bildungsromans",
                "Domestic fiction", "Family life -- New England -- Fiction",
                "March family (Fictitious characters) -- Fiction",
                "Mothers and daughters -- Fiction", "New England -- Fiction",
                "Sisters -- Fiction", "Young women -- Fiction"
            ],
            "bookshelves": ["Children's Literature"],
            "languages": ["en"],
            "copyright":
            False,
            "media_type":
            "Text",
            "formats": {
                "application/epub+zip":
                "https://www.gutenberg.org/ebooks/514.epub.images",
                "application/rdf+xml":
                "https://www.gutenberg.org/ebooks/514.rdf",
                "text/plain":
                "https://www.gutenberg.org/ebooks/514.txt.utf-8",
                "application/x-mobipocket-ebook":
                "https://www.gutenberg.org/ebooks/514.kindle.images",
                "text/html":
                "https://www.gutenberg.org/files/514/514-h/514-h.htm",
                "image/jpeg":
                "https://www.gutenberg.org/cache/epub/514/pg514.cover.medium.jpg",
                "application/octet-stream":
                "https://www.gutenberg.org/files/514/514-0.zip",
                "text/plain; charset=us-ascii":
                "https://www.gutenberg.org/files/514/514-0.txt"
            },
            "download_count":
            1000
        }]
    }


def success_returned_value_book_id_80():
    return {
        'count':
        1,
        'next':
        None,
        'previous':
        None,
        'results': [{
            'id':
            80,
            'title':
            'The Online World',
            'authors': [{
                'name': 'De Presno, Odd',
                'birth_year': 1944,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Internet'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            True,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/80.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/80.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/80.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/80.kindle.images',
                'text/html':
                'https://www.gutenberg.org/ebooks/80.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/80/pg80.cover.medium.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/80/80.txt'
            },
            'download_count':
            31
        }]
    }


def book_not_found():
    return {'count': 0, 'next': None, 'previous': None, 'results': []}


def success_book_by_title():
    return {
        'count':
        22,
        'next':
        None,
        'previous':
        None,
        'results': [{
            'id':
            22739,
            'title':
            'The Human Aura: Astral Colors and Thought Forms',
            'authors': [{
                'name': 'Atkinson, William Walker',
                'birth_year': 1862,
                'death_year': 1932
            }],
            'translators': [],
            'subjects': ['Occultism'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/22739/22739.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/22739/22739-h/22739-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/22739.html.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/22739.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/22739.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/22739.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/22739.txt.utf-8',
                'application/zip':
                'https://www.gutenberg.org/files/22739/22739-h.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/22739/pg22739.cover.medium.jpg'
            },
            'download_count':
            232
        }, {
            'id':
            20796,
            'title':
            'The Colors of Space',
            'authors': [{
                'name': 'Bradley, Marion Zimmer',
                'birth_year': 1930,
                'death_year': 1999
            }],
            'translators': [],
            'subjects': ['Science fiction'],
            'bookshelves': ['Science Fiction', 'Science Fiction by Women'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/20796.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/20796.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/20796.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/20796.rdf',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20796/20796-8.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20796/20796-h/20796-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/20796/pg20796.cover.small.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/20796.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/20796/20796.txt',
                'application/zip':
                'https://www.gutenberg.org/files/20796/20796.zip'
            },
            'download_count':
            145
        }, {
            'id':
            30000,
            'title':
            'The Bird Book: Illustrating in natural colors more than seven hundred North American birds; also several '
            'hundred photographs of their nests and eggs.',
            'authors': [{
                'name': 'Reed, Chester A. (Chester Albert)',
                'birth_year': 1876,
                'death_year': 1912
            }],
            'translators': [],
            'subjects': ['Birds -- North America'],
            'bookshelves': ['Animal', 'Animals-Wild-Birds'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/30000/30000-8.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/30000/pg30000.cover.small.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/30000.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/30000.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/30000.epub.images',
                'text/html':
                'https://www.gutenberg.org/ebooks/30000.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/30000/30000.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/30000/30000.txt',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/30000/30000-h.zip',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/30000/30000-0.txt'
            },
            'download_count':
            97
        }, {
            'id':
            30877,
            'title':
            'The Painter in Oil: A complete treatise on the principles and technique necessary to the painting of '
            'pictures in oil colors',
            'authors': [{
                'name': 'Parkhurst, Daniel Burleigh',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Painting -- Technique'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/30877/30877.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/30877.html.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/30877.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/30877.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/30877.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/30877.kindle.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/30877/30877-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/30877/pg30877.cover.medium.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/30877/30877.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/30877/30877-h/30877-h.htm'
            },
            'download_count':
            82
        }, {
            'id':
            53647,
            'title':
            'Texas Flowers in Natural Colors',
            'authors': [{
                'name': 'Whitehouse, Eula',
                'birth_year': 1892,
                'death_year': 1974
            }],
            'translators': [],
            'subjects':
            ['Wild flowers -- Southwestern States', 'Wild flowers -- Texas'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/53647/53647-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/53647/pg53647.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/53647/53647-h.zip',
                'text/html':
                'https://www.gutenberg.org/files/53647/53647-h/53647-h.htm',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/53647.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/53647.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/53647.rdf'
            },
            'download_count':
            51
        }, {
            'id':
            23085,
            'title':
            'The Colors of Space',
            'authors': [{
                'name': 'Bradley, Marion Zimmer',
                'birth_year': 1930,
                'death_year': 1999
            }],
            'translators': [],
            'subjects': ['Science fiction'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Sound',
            'formats': {
                'audio/mpeg':
                'http://www.gutenberg.org/files/23085/mp3/23085-11.mp3',
                'audio/mp4':
                'http://www.gutenberg.org/files/23085/m4b/23085-09.m4b',
                'audio/ogg':
                'http://www.gutenberg.org/files/23085/spx/23085-05.spx',
                'text/html':
                'http://www.gutenberg.org/files/23085/23085-index.html',
                'application/rdf+xml':
                'http://www.gutenberg.org/ebooks/23085.rdf',
                'text/plain':
                'http://www.gutenberg.org/files/23085/23085-readme.txt'
            },
            'download_count':
            42
        }, {
            'id':
            27016,
            'title':
            'Eight dwelling places of Buddhist immortals',
            'authors': [{
                'name': 'Five colors stone',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': [],
            'bookshelves': [],
            'languages': ['zh'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/27016.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/27016.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/27016.rdf',
                'text/html':
                'https://www.gutenberg.org/ebooks/27016.html.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/27016/27016-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/27016/pg27016.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/27016/27016-0.zip'
            },
            'download_count':
            40
        }, {
            'id':
            28328,
            'title':
            'Americanism Contrasted with Foreignism, Romanism, and Bogus Democracy in the Light of Reason, History, '
            'and Scripture;: In which Certain Demagogues in Tennessee, and Elsewhere,; are Shown Up in Their '
            'True Colors',
            'authors': [{
                'name': 'Brownlow, William Gannaway',
                'birth_year': 1805,
                'death_year': 1877
            }],
            'translators': [],
            'subjects': [
                'American Party', 'Campaign literature, 1865 -- American',
                'Tennessee -- Politics and government',
                'United States -- Politics and government -- 1853-1857'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/28328/28328-8.txt',
                'text/plain':
                'https://www.gutenberg.org/ebooks/28328.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/28328.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/28328.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/28328.rdf',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/28328/28328-h/28328-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/28328.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/28328/pg28328.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/28328/28328-h.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/28328/28328.txt'
            },
            'download_count':
            40
        }, {
            'id':
            52800,
            'title':
            "Lowney's Cook Book: Illustrated in Colors",
            'authors': [{
                'name': 'Howard, Maria Willett',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Cooking', 'Cooking, American'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/52800/52800-0.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/52800.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/52800/pg52800.cover.medium.jpg',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/52800/52800-h/52800-h.htm',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/52800.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/52800.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/52800.epub.images'
            },
            'download_count':
            36
        }, {
            'id':
            32173,
            'title':
            'Under Boy Scout Colors',
            'authors': [{
                'name': 'Ames, Joseph Bushnell',
                'birth_year': 1878,
                'death_year': 1928
            }],
            'translators': [],
            'subjects': ['Boy Scouts of America -- Juvenile fiction'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/32173/32173.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/32173.html.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/32173.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/32173.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/32173.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/32173.txt.utf-8',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/32173/32173-h.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/32173/pg32173.cover.small.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/32173/32173-8.txt',
                'application/zip':
                'https://www.gutenberg.org/files/32173/32173.zip'
            },
            'download_count':
            32
        }, {
            'id':
            43500,
            'title':
            "Graining and Marbling: A Series of Practical Treatises on Material, Tools and Appliances Used; General "
            "Operations; Preparing Oil Graining Colors; Mixing; Rubbing; Applying Distemper Colors; Wiping Out; "
            "Penciling; The Use of Crayons; Review of Woods; The Graining of Oak, Ash, Cherry, Satinwood, Mahogany, "
            "Maple, Bird's Eye Maple, Sycamore, Walnut, Etc.; Marbling in All Shades.",
            'authors': [{
                'name': 'Maire, F. (Frederick)',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Graining', 'Marbling'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/43500/43500-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/43500/pg43500.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/43500.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/43500.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/43500.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/43500.kindle.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/43500/43500.txt',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/43500/43500-h/43500-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/43500.html.images'
            },
            'download_count':
            32
        }, {
            'id':
            20986,
            'title':
            'Tom Slade with the Colors',
            'authors': [{
                'name': 'Fitzhugh, Percy Keese',
                'birth_year': 1876,
                'death_year': 1950
            }],
            'translators': [],
            'subjects': ['Boy Scouts of America -- Juvenile fiction'],
            'bookshelves': ["Children's Book Series"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/20986.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/20986.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/20986.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/20986.kindle.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20986/20986-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/20986/pg20986.cover.medium.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/20986/20986-h.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20986/20986-h/20986-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/20986.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/20986/20986.txt'
            },
            'download_count':
            29
        }, {
            'id':
            63087,
            'title':
            'Color Standards and Color Nomenclature: With fifty-three colored plates and eleven hundred and '
            'fifteen named colors',
            'authors': [{
                'name': 'Ridgway, Robert',
                'birth_year': 1850,
                'death_year': 1929
            }],
            'translators': [],
            'subjects': ['Colors'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/63087.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/63087.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/63087.epub.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/63087/63087-h/63087-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/63087.html.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/63087/63087-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/63087/pg63087.cover.medium.jpg'
            },
            'download_count':
            29
        }, {
            'id':
            36051,
            'title':
            'Colors of Life: Poems and Songs and Sonnets',
            'authors': [{
                'name': 'Eastman, Max',
                'birth_year': 1883,
                'death_year': 1969
            }],
            'translators': [],
            'subjects': ['American poetry -- 20th century'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/36051.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/36051.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/36051.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/36051.epub.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/36051/36051.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/36051/36051-8.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/36051.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/36051/pg36051.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/36051/36051-h.zip'
            },
            'download_count':
            20
        }, {
            'id':
            41749,
            'title':
            'Practical Graining, with Description of Colors Employed and Tools Used',
            'authors': [{
                'name': 'Wall, William E. (William Edmund)',
                'birth_year': 1858,
                'death_year': 1934
            }],
            'translators': [],
            'subjects': ['Graining'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/files/41749/41749-h/41749-h.htm',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/41749/41749-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/41749/pg41749.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/41749.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/41749.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/41749.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/41749.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/41749/41749.txt'
            },
            'download_count':
            20
        }, {
            'id':
            62275,
            'title':
            'West Point Colors',
            'authors': [{
                'name': 'Warner, Anna Bartlett',
                'birth_year': 1824,
                'death_year': 1915
            }],
            'translators': [],
            'subjects': ['United States Military Academy -- Fiction'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/62275.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/62275.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/62275.epub.images',
                'text/html':
                'https://www.gutenberg.org/files/62275/62275-h/62275-h.htm',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/62275/62275-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/62275/pg62275.cover.medium.jpg'
            },
            'download_count':
            13
        }, {
            'id':
            20072,
            'title':
            'With the Colors: Songs of the American Service',
            'authors': [{
                'name': 'Appleton, Everard Jack',
                'birth_year': 1872,
                'death_year': 1931
            }],
            'translators': [],
            'subjects': ['World War, 1914-1918 -- Poetry'],
            'bookshelves': ['Bestsellers, American, 1895-1923'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/20072/pg20072.cover.small.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/20072.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/20072/20072.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20072/20072-h.zip',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/20072.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/20072.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/20072.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/20072.txt.utf-8'
            },
            'download_count':
            10
        }, {
            'id':
            48141,
            'title':
            'Birds and All Nature, Vol. 6, No. 4, November 1899: In Natural Colors',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects':
            ['Birds -- Periodicals', 'Natural history -- Periodicals'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/48141.html.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/48141/48141-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/48141/pg48141.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/48141/48141-h/48141-h.htm',
                'text/plain':
                'https://www.gutenberg.org/ebooks/48141.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/48141.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/48141.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/48141.epub.images'
            },
            'download_count':
            9
        }, {
            'id':
            48503,
            'title':
            'Birds and Nature, Vol. 08, No. 1, June 1900: In Natural Colors',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects':
            ['Birds -- Periodicals', 'Natural history -- Periodicals'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/48503.html.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/48503/48503-h/48503-h.htm',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/48503/48503-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/48503/pg48503.cover.medium.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/48503.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/48503.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/48503.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/48503.epub.images'
            },
            'download_count':
            8
        }, {
            'id':
            15179,
            'title':
            'The Inner Sisterhood: A Social Study in High Colors',
            'authors': [{
                'name': 'Sherley, Douglass',
                'birth_year': 1857,
                'death_year': 1917
            }],
            'translators': [],
            'subjects': ['Fiction'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/15179.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/15179.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/15179.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/15179.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/15179.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/15179/15179.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/15179/pg15179.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15179/15179-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/15179/15179-8.zip',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15179/15179-8.txt'
            },
            'download_count':
            7
        }, {
            'id':
            45079,
            'title':
            'The Art of Graining: How Acquired and How Produced.: With the description of colors and their '
            'applications.',
            'authors': [{
                'name': 'Pickert, Charles',
                'birth_year': None,
                'death_year': None
            }, {
                'name': 'Metcalf, A.',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Graining'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/45079.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/45079/45079.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/45079/pg45079.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/45079/45079-h/45079-h.htm',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/45079.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/45079.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/45079.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/45079.kindle.images'
            },
            'download_count':
            6
        }, {
            'id':
            28391,
            'title':
            'True To His Colors',
            'authors': [{
                'name': 'Castlemon, Harry',
                'birth_year': 1842,
                'death_year': 1915
            }],
            'translators': [],
            'subjects':
            ['United States -- History -- Civil War, 1861-1865 -- Fiction'],
            'bookshelves': ['US Civil War'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/28391.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/28391.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/28391.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/28391.rdf',
                'text/html':
                'https://www.gutenberg.org/ebooks/28391.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/28391/28391.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/28391/pg28391.cover.small.jpg'
            },
            'download_count':
            3
        }]
    }


def success_return_page_10():
    return {
        'count':
        68800,
        'next':
        'https://gutendex.com/books/?page=11',
        'previous':
        'https://gutendex.com/books/?page=9',
        'results': [{
            'id':
            68283,
            'title':
            'The call of Cthulhu',
            'authors': [{
                'name': 'Lovecraft, H. P. (Howard Phillips)',
                'birth_year': 1890,
                'death_year': 1937
            }],
            'translators': [],
            'subjects':
            ['Cthulhu (Fictitious character) -- Fiction', 'Horror tales'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/octet-stream':
                'https://www.gutenberg.org/files/68283/68283-0.zip',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68283.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68283.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68283.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68283.txt.utf-8',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68283/pg68283.cover.medium.jpg',
                'text/html':
                'https://www.gutenberg.org/files/68283/68283-h/68283-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68283/68283-0.txt'
            },
            'download_count':
            1494
        }, {
            'id':
            13415,
            'title':
            'The Lady with the Dog and Other Stories',
            'authors': [{
                'name': 'Chekhov, Anton Pavlovich',
                'birth_year': 1860,
                'death_year': 1904
            }],
            'translators': [{
                'name': 'Garnett, Constance',
                'birth_year': 1861,
                'death_year': 1946
            }],
            'subjects': [
                'Chekhov, Anton Pavlovich, 1860-1904 -- Translations into English',
                'Russia -- Social life and customs -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/13415.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/13415.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/13415.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/13415.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/13415.html.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/13415/13415-h/13415-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/13415/pg13415.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/13415/13415-8.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/13415/13415.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/13415/13415-8.txt'
            },
            'download_count':
            1491
        }, {
            'id':
            22381,
            'title':
            'Myths and Legends of Ancient Greece and Rome',
            'authors': [{
                'name': 'Berens, E. M.',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Mythology, Classical'],
            'bookshelves': ['Greece', 'Mythology'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/22381.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/22381.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/22381.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/22381.txt.utf-8',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/22381/22381-h/22381-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/22381.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/22381/22381.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/22381/pg22381.cover.medium.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/22381/22381-8.zip',
                'application/zip':
                'https://www.gutenberg.org/files/22381/22381-h.zip'
            },
            'download_count':
            1487
        }, {
            'id':
            27805,
            'title':
            'The Wind in the Willows',
            'authors': [{
                'name': 'Grahame, Kenneth',
                'birth_year': 1859,
                'death_year': 1932
            }],
            'translators': [],
            'subjects': [
                'Animals -- Fiction', 'Country life -- Fiction',
                'England -- Fiction', 'Fantasy fiction',
                'Friendship -- Fiction', 'Humorous stories',
                'Pastoral fiction', 'River life -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/27805.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/27805.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/27805.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/27805.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/27805/27805.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/27805/27805-8.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/27805.html.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/27805/27805-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/27805/27805.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/27805/pg27805.cover.small.jpg'
            },
            'download_count':
            1487
        }, {
            'id':
            38769,
            'title':
            'A Course of Pure Mathematics: Third Edition',
            'authors': [{
                'name': 'Hardy, G. H. (Godfrey Harold)',
                'birth_year': 1877,
                'death_year': 1947
            }],
            'translators': [],
            'subjects': ['Calculus', 'Functions'],
            'bookshelves': ['Mathematics'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/38769.rdf',
                'application/prs.tex':
                'https://www.gutenberg.org/files/38769/38769-t.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/38769/pg38769.cover.medium.jpg',
                'application/pdf':
                'https://www.gutenberg.org/files/38769/38769-pdf.pdf'
            },
            'download_count':
            1487
        }, {
            'id':
            61168,
            'title':
            'The Man in the Brown Suit',
            'authors': [{
                'name': 'Christie, Agatha',
                'birth_year': 1890,
                'death_year': 1976
            }],
            'translators': [],
            'subjects': [
                'Detective and mystery stories', 'London (England) -- Fiction',
                'Murder -- Investigation -- Fiction',
                'South Africa -- Fiction', 'Women adventurers -- Fiction'
            ],
            'bookshelves': ['Detective Fiction'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/files/61168/61168-h/61168-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/61168/pg61168.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/61168/61168-0.zip',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/61168.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/61168.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/61168.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/61168.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/61168/61168-0.txt'
            },
            'download_count':
            1483
        }, {
            'id':
            28890,
            'title':
            'Helps to Latin Translation at Sight',
            'authors': [{
                'name': 'Luce, Edmund',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Latin language -- Readers'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/28890.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/28890.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/28890.epub.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/28890/28890-h/28890-h.htm',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/28890/28890-0.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/28890.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/28890/28890-0.zip',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/28890/28890-8.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/28890/pg28890.cover.medium.jpg'
            },
            'download_count':
            1471
        }, {
            'id':
            14264,
            'title':
            'The Practice and Science of Drawing',
            'authors': [{
                'name': 'Speed, Harold',
                'birth_year': 1873,
                'death_year': 1957
            }],
            'translators': [],
            'subjects': ['Drawing'],
            'bookshelves': ['Art'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/14264/14264.txt',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/14264.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/14264.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/14264.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/14264.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/14264.html.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/14264/14264-8.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/14264/14264-h/14264-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/14264/pg14264.cover.medium.jpg'
            },
            'download_count':
            1468
        }, {
            'id':
            3160,
            'title':
            'The Odyssey',
            'authors': [{
                'name': 'Homer',
                'birth_year': -750,
                'death_year': -650
            }],
            'translators': [{
                'name': 'Pope, Alexander',
                'birth_year': 1688,
                'death_year': 1744
            }],
            'subjects': [
                'Epic poetry, Greek -- Translations into English',
                'Homer -- Translations into English',
                'Odysseus, King of Ithaca (Mythological character) -- Poetry'
            ],
            'bookshelves': [
                "Banned Books from Anne Haight's list", 'Classical Antiquity',
                'Harvard Classics'
            ],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/3160/pg3160.cover.medium.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/3160.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/3160.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/3160.rdf',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/3160/3160-h/3160-h.htm',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/3160/3160-0.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/3160.html.images'
            },
            'download_count':
            1465
        }, {
            'id':
            68815,
            'title':
            'Galactic Patrol',
            'authors': [{
                'name': 'Smith, E. E. (Edward Elmer)',
                'birth_year': 1890,
                'death_year': 1965
            }],
            'translators': [],
            'subjects': [
                'Interplanetary voyages -- Fiction',
                'Life on other planets -- Fiction',
                'Peace officers -- Fiction', 'Science fiction',
                'Space pirates -- Fiction', 'Space warfare -- Fiction',
                'Telepathy -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/files/68815/68815-h/68815-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68815/68815-0.txt',
                'application/octet-stream':
                'https://www.gutenberg.org/files/68815/68815-0.zip',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68815.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68815.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68815.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68815.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68815/pg68815.cover.medium.jpg'
            },
            'download_count':
            1463
        }, {
            'id':
            10609,
            'title':
            'English Literature: Its History and Its Significance for the Life of the English-Speaking World',
            'authors': [{
                'name': 'Long, William J. (William Joseph)',
                'birth_year': 1867,
                'death_year': 1952
            }],
            'translators': [],
            'subjects': ['English literature -- History and criticism'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/10609.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/10609.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/10609.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/10609.kindle.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/10609/pg10609.cover.medium.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/10609.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/10609/10609.txt',
                'application/zip':
                'https://www.gutenberg.org/files/10609/10609-h.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/10609/10609-h/10609-h.htm',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/10609/10609-8.txt'
            },
            'download_count':
            1457
        }, {
            'id':
            61221,
            'title':
            'A Passage to India',
            'authors': [{
                'name': 'Forster, E. M. (Edward Morgan)',
                'birth_year': 1879,
                'death_year': 1970
            }],
            'translators': [],
            'subjects': [
                'British -- India -- Fiction',
                'India -- Social conditions -- 20th century -- Fiction',
                'Political fiction', 'Race relations -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/61221.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/61221.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/61221.epub.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/61221/61221-h/61221-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/61221/pg61221.cover.medium.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/61221.html.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/61221/61221-0.txt'
            },
            'download_count':
            1456
        }, {
            'id': 10947,
            'title': 'The Best American Humorous Short Stories',
            'authors': [],
            'translators': [],
            'subjects': ['Short stories, American'],
            'bookshelves': ['Short Stories'],
            'languages': ['en'],
            'copyright': False,
            'media_type': 'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/10947.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/10947.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/10947.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/10947.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/files/10947/10947-h/10947-h.htm',
                'application/zip':
                'https://www.gutenberg.org/files/10947/10947.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/10947/pg10947.cover.medium.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/10947/10947-0.txt',
                'application/octet-stream':
                'https://www.gutenberg.org/files/10947/10947-8.zip'
            },
            'download_count': 1454
        }, {
            'id':
            68717,
            'title':
            'The American scene',
            'authors': [{
                'name': 'James, Henry',
                'birth_year': 1843,
                'death_year': 1916
            }],
            'translators': [],
            'subjects': [
                'Atlantic States -- Description and travel',
                'James, Henry, 1843-1916 -- Travel -- Atlantic States',
                "Travelers' writings, American",
                'United States -- Description and travel',
                'United States -- Social life and customs -- 1865-1918'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68717.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68717.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68717.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68717.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68717/pg68717.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/68717/68717-0.zip',
                'text/html':
                'https://www.gutenberg.org/files/68717/68717-h/68717-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68717/68717-0.txt'
            },
            'download_count':
            1452
        }, {
            'id':
            68829,
            'title':
            'Mistake inside',
            'authors': [{
                'name': 'Blish, James',
                'birth_year': 1921,
                'death_year': 1975
            }],
            'translators': [],
            'subjects':
            ['Fantasy fiction', 'Hell -- Fiction', 'Magic -- Fiction'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/files/68829/68829-h/68829-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68829/68829-0.txt',
                'application/octet-stream':
                'https://www.gutenberg.org/files/68829/68829-0.zip',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68829.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68829.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68829.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68829.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68829/pg68829.cover.medium.jpg'
            },
            'download_count':
            1449
        }, {
            'id':
            15474,
            'title':
            'The Mahabharata of Krishna-Dwaipayana Vyasa, Volume 1: Books 1, 2 and 3',
            'authors': [],
            'translators': [{
                'name': 'Ganguli, Kisari Mohan',
                'birth_year': None,
                'death_year': None
            }],
            'subjects': ['Epic literature, Sanskrit'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/15474.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/15474/pg15474.cover.medium.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/15474.kindle.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/15474/15474-0.txt',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/15474.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/15474.epub.images',
                'application/zip':
                'https://www.gutenberg.org/files/15474/15474-h.zip',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/15474/15474-h/15474-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/15474/15474.txt'
            },
            'download_count':
            1446
        }, {
            'id':
            6087,
            'title':
            'The Vampyre; a Tale',
            'authors': [{
                'name': 'Polidori, John William',
                'birth_year': 1795,
                'death_year': 1821
            }],
            'translators': [],
            'subjects':
            ['Gothic fiction', 'Horror tales', 'Vampires -- Fiction'],
            'bookshelves': ['Gothic Fiction', 'Horror'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/6087/pg6087.cover.small.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/6087/6087-8.txt',
                'text/plain':
                'https://www.gutenberg.org/ebooks/6087.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/6087.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/6087.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/6087.kindle.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/6087/6087.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/6087/6087-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/6087/6087-8.zip',
                'text/html':
                'https://www.gutenberg.org/ebooks/6087.html.images'
            },
            'download_count':
            1445
        }, {
            'id':
            22120,
            'title':
            "Chaucer's Works, Volume 4 — The Canterbury Tales",
            'authors': [{
                'name': 'Chaucer, Geoffrey',
                'birth_year': 1342,
                'death_year': 1400
            }],
            'translators': [],
            'subjects': ['Christian pilgrims and pilgrimages -- Poetry'],
            'bookshelves': ['Best Books Ever Listings'],
            'languages': ['enm'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/22120.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/22120.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/22120.rdf',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/22120/22120-0.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/22120.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/22120/pg22120.cover.small.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/22120/22120-h/22120-h.htm',
                'application/zip':
                'https://www.gutenberg.org/files/22120/22120-h.zip'
            },
            'download_count':
            1445
        }, {
            'id':
            32,
            'title':
            'Herland',
            'authors': [{
                'name': 'Gilman, Charlotte Perkins',
                'birth_year': 1860,
                'death_year': 1935
            }],
            'translators': [],
            'subjects': [
                'Black humor', 'Utopian fiction', 'Utopias -- Fiction',
                'Women -- Fiction'
            ],
            'bookshelves': ['Best Books Ever Listings'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/32.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/32/32-0.txt',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/32.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/32.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/32.kindle.images',
                'text/html':
                'https://www.gutenberg.org/files/32/32-h/32-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/32/pg32.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/32/32-0.zip'
            },
            'download_count':
            1443
        }, {
            'id':
            500,
            'title':
            'The Adventures of Pinocchio',
            'authors': [{
                'name': 'Collodi, Carlo',
                'birth_year': 1826,
                'death_year': 1890
            }],
            'translators': [{
                'name': 'Della Chiesa, Carol',
                'birth_year': 1887,
                'death_year': None
            }],
            'subjects': [
                'Fairy tales',
                'Pinocchio (Fictitious character) -- Juvenile fiction',
                'Puppets -- Juvenile fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/500.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/500.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/500.kindle.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/500/500-h/500-h.htm',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/500/500-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/500/pg500.cover.medium.jpg',
                'text/html': 'https://www.gutenberg.org/ebooks/500.html.images'
            },
            'download_count':
            1437
        }, {
            'id':
            1600,
            'title':
            'Symposium',
            'authors': [{
                'name': 'Plato',
                'birth_year': -428,
                'death_year': -348
            }],
            'translators': [{
                'name': 'Jowett, Benjamin',
                'birth_year': 1817,
                'death_year': 1893
            }],
            'subjects': [
                'Classical literature', 'Love -- Early works to 1800',
                'Philosophy, Ancient', 'Socrates, 470 BC-399 BC'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/1600/pg1600.cover.medium.jpg',
                'text/plain':
                'https://www.gutenberg.org/ebooks/1600.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/1600.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/1600.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/1600.rdf',
                'text/html; charset=us-ascii':
                'https://www.gutenberg.org/files/1600/1600-h/1600-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/1600/1600.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/1600.html.images'
            },
            'download_count':
            1430
        }, {
            'id':
            68662,
            'title':
            'Elements of arithmetic',
            'authors': [{
                'name': 'De Morgan, Augustus',
                'birth_year': 1806,
                'death_year': 1871
            }],
            'translators': [],
            'subjects': ['Algebra', 'Arithmetic -- Early works to 1900'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68662.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68662.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68662.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68662.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68662/pg68662.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/68662/68662-0.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68662/68662-0.txt',
                'text/html':
                'https://www.gutenberg.org/files/68662/68662-h/68662-h.htm'
            },
            'download_count':
            1429
        }, {
            'id':
            503,
            'title':
            'The Blue Fairy Book',
            'authors': [{
                'name': 'Lang, Andrew',
                'birth_year': 1844,
                'death_year': 1912
            }],
            'translators': [],
            'subjects': ['Fairy tales', 'Folklore'],
            'bookshelves': ["Children's Literature"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/503.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/503.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/503.kindle.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/503/503.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/503/pg503.cover.medium.jpg',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/503/503-0.txt',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/503/503-h/503-h.htm',
                'text/html': 'https://www.gutenberg.org/ebooks/503.html.images'
            },
            'download_count':
            1427
        }, {
            'id':
            9105,
            'title':
            'Reflections; or Sentences and Moral Maxims',
            'authors': [{
                'name': 'La Rochefoucauld, François duc de',
                'birth_year': 1613,
                'death_year': 1680
            }],
            'translators': [{
                'name': 'Friswell, J. Hain (James Hain)',
                'birth_year': 1825,
                'death_year': 1878
            }, {
                'name': 'Willis Bund, J. W. (John William)',
                'birth_year': 1843,
                'death_year': 1928
            }],
            'subjects': ['Maxims'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/9105.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/9105.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/9105.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/9105.rdf',
                'text/html':
                'https://www.gutenberg.org/ebooks/9105.html.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/9105/9105-h/9105-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/9105/pg9105.cover.small.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/9105/9105.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/9105/9105-8.zip',
                'application/zip':
                'https://www.gutenberg.org/files/9105/9105.zip'
            },
            'download_count':
            1424
        }, {
            'id':
            33044,
            'title':
            'Birds from North Borneo: University of Kansas Publications, Museum of Natural History, Volume 17, No. 8, '
            'pp. 377-433, October 27, 1966',
            'authors': [{
                'name': 'Thompson, Max C.',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Birds -- Malaysia -- Sabah'],
            'bookshelves': ['Animal', 'Animals-Wild-Birds'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/33044/33044.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/33044/pg33044.cover.medium.jpg',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/33044.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/33044.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/33044.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/33044.txt.utf-8',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/33044/33044-h/33044-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/33044.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/33044/33044.zip',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/33044/33044-8.txt'
            },
            'download_count':
            1421
        }, {
            'id':
            60,
            'title':
            'The Scarlet Pimpernel',
            'authors': [{
                'name': 'Orczy, Emmuska Orczy, Baroness',
                'birth_year': 1865,
                'death_year': 1947
            }],
            'translators': [],
            'subjects': [
                'Adventure stories',
                'Blakeney, Percy, Sir (Fictitious character) -- Fiction',
                'British -- France -- Fiction',
                'France -- History -- Revolution, 1789-1799 -- Fiction',
                'Historical fiction', 'Nobility -- Fiction'
            ],
            'bookshelves':
            ['Adventure', 'Best Books Ever Listings', 'Movie Books'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/60.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/60.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/60.kindle.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/60/pg60.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/60/60-0.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/60/60-0.txt',
                'text/plain': 'https://www.gutenberg.org/ebooks/60.txt.utf-8',
                'text/html': 'https://www.gutenberg.org/files/60/60-h/60-h.htm'
            },
            'download_count':
            1419
        }, {
            'id':
            155,
            'title':
            'The Moonstone',
            'authors': [{
                'name': 'Collins, Wilkie',
                'birth_year': 1824,
                'death_year': 1889
            }],
            'translators': [],
            'subjects': [
                'Country homes -- Fiction',
                'East Indians -- England -- Fiction', 'England -- Fiction',
                'Jewelry theft -- Fiction', 'Mystery fiction',
                'Police -- England -- Fiction'
            ],
            'bookshelves': ['Detective Fiction', 'Mystery Fiction'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/155.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/155.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/155.kindle.images',
                'text/html':
                'https://www.gutenberg.org/files/155/155-h/155-h.htm',
                'application/octet-stream':
                'https://www.gutenberg.org/files/155/155-0.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/155/pg155.cover.medium.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/155/155-0.txt',
                'text/plain': 'https://www.gutenberg.org/ebooks/155.txt.utf-8'
            },
            'download_count':
            1412
        }, {
            'id':
            4705,
            'title':
            'A Treatise of Human Nature',
            'authors': [{
                'name': 'Hume, David',
                'birth_year': 1711,
                'death_year': 1776
            }],
            'translators': [],
            'subjects': ['Knowledge, Theory of'],
            'bookshelves': ['Philosophy'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/files/4705/4705-h/4705-h.htm',
                'application/octet-stream':
                'https://www.gutenberg.org/files/4705/4705-0.zip',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/4705.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/4705.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/4705.kindle.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/4705/4705-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/4705/pg4705.cover.medium.jpg',
                'text/plain': 'https://www.gutenberg.org/ebooks/4705.txt.utf-8'
            },
            'download_count':
            1410
        }, {
            'id':
            33451,
            'title':
            'The Atlantic Monthly, Volume 20, No. 119, September, 1867: A Magazine of Literature, Science, Art, '
            'and Politics',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['American periodicals'],
            'bookshelves': ['The Atlantic Monthly'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/33451/33451.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/33451.html.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/33451.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/33451.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/33451.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/33451.kindle.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/33451/pg33451.cover.small.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/33451/33451-8.txt',
                'application/zip':
                'https://www.gutenberg.org/files/33451/33451-h.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/33451/33451-h/33451-h.htm'
            },
            'download_count':
            1407
        }, {
            'id':
            805,
            'title':
            'This Side of Paradise',
            'authors': [{
                'name': 'Fitzgerald, F. Scott (Francis Scott)',
                'birth_year': 1896,
                'death_year': 1940
            }],
            'translators': [],
            'subjects': [
                'Advertising -- Fiction', 'Bildungsromans',
                'Children of the rich -- Fiction',
                'College students -- Fiction', 'Love stories',
                'World War, 1914-1918 -- Veterans -- Fiction',
                'Young men -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/805.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/805.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/805.kindle.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/805/805-0.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/805/805-8.txt',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/805/805.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/805/pg805.cover.medium.jpg',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/805/805-h/805-h.htm',
                'text/html': 'https://www.gutenberg.org/ebooks/805.html.images'
            },
            'download_count':
            1405
        }, {
            'id':
            45631,
            'title':
            'Twelve Years a Slave: Narrative of Solomon Northup, a Citizen of New-York, Kidnapped in Washington '
            'City in 1841, and Rescued in 1853, from a Cotton Plantation near the Red River in Louisiana',
            'authors': [{
                'name': 'Northup, Solomon',
                'birth_year': 1808,
                'death_year': None
            }],
            'translators': [],
            'subjects': [
                'African Americans -- Biography',
                'Northup, Solomon, 1808-1863?',
                'Plantation life -- Louisiana -- History -- 19th century',
                'Slavery -- Louisiana -- History -- 19th century',
                'Slaves -- United States -- Biography',
                "Slaves' writings, American"
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/45631.html.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/45631/45631-8.txt',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/45631/45631.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/45631/pg45631.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/45631.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/45631.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/45631.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/45631.kindle.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/45631/45631-h/45631-h.htm'
            },
            'download_count':
            1402
        }, {
            'id':
            9662,
            'title':
            'An Enquiry Concerning Human Understanding',
            'authors': [{
                'name': 'Hume, David',
                'birth_year': 1711,
                'death_year': 1776
            }],
            'translators': [],
            'subjects': ['Ethics', 'Knowledge, Theory of'],
            'bookshelves': ['Harvard Classics', 'Philosophy'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/9662/9662-8.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/9662.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/9662/pg9662.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/9662.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/9662.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/9662.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/9662.kindle.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/9662/9662.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/9662/9662-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/9662/9662-8.zip'
            },
            'download_count':
            1397
        }]
    }


def success_return_page_2_of_child_titles():
    return {
        'count':
        610,
        'next':
        'https://gutendex.com/books/?page=3&search=child',
        'previous':
        'https://gutendex.com/books/?search=child',
        'results': [{
            'id':
            15484,
            'title':
            "The Care and Feeding of Children: A Catechism for the Use of Mothers and Children's Nurses",
            'authors': [{
                'name': 'Holt, L. Emmett (Luther Emmett)',
                'birth_year': 1855,
                'death_year': 1924
            }],
            'translators': [],
            'subjects': ['Child care', 'Children -- Nutrition'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15484/15484-h/15484-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/15484.html.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/15484.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/15484.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/15484.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/15484.txt.utf-8',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15484/15484-8.txt',
                'application/zip':
                'https://www.gutenberg.org/files/15484/15484-h.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/15484/pg15484.cover.small.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/15484/15484.txt'
            },
            'download_count':
            226
        }, {
            'id':
            22096,
            'title':
            'Stories the Iroquois Tell Their Children',
            'authors': [{
                'name': 'Powers, Mabel',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Iroquois Indians -- Folklore'],
            'bookshelves': [
                "Children's Myths, Fairy Tales, etc.", 'Folklore',
                'Native America'
            ],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/22096/pg22096.cover.small.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/22096.html.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/22096.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/22096.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/22096.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/22096.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/22096/22096.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/22096/22096-h/22096-h.htm',
                'application/zip':
                'https://www.gutenberg.org/files/22096/22096.zip'
            },
            'download_count':
            222
        }, {
            'id':
            28402,
            'title':
            'The Sexual Life of the Child',
            'authors': [{
                'name': 'Moll, Albert',
                'birth_year': 1862,
                'death_year': 1939
            }],
            'translators': [{
                'name': 'Paul, Eden',
                'birth_year': 1865,
                'death_year': 1944
            }],
            'subjects': ['Children -- Sexual behavior', 'Sex instruction'],
            'bookshelves': ['Sociology'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/28402.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/28402.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/28402.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/28402.rdf',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/28402/28402-h/28402-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/28402.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/28402/28402-8.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/28402/28402.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/28402/pg28402.cover.medium.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/28402/28402-8.txt'
            },
            'download_count':
            206
        }, {
            'id':
            14916,
            'title':
            'Fairy Tales Every Child Should Know',
            'authors': [],
            'translators': [],
            'subjects': ['Fairy tales'],
            'bookshelves':
            ["Children's Anthologies", "Children's Myths, Fairy Tales, etc."],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/14916.html.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/14916/14916-8.txt',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/14916/14916.zip',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/14916.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/14916.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/14916.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/14916.txt.utf-8',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/14916/pg14916.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/14916/14916-h/14916-h.htm'
            },
            'download_count':
            203
        }, {
            'id':
            68649,
            'title':
            "The spoil'd child: A farce, in two acts, as performed at the Theatre Royal, Drury Lane",
            'authors': [{
                'name': 'Bickerstaff, Isaac',
                'birth_year': 1735,
                'death_year': 1812
            }, {
                'name': 'Ford, Richard, Sir',
                'birth_year': None,
                'death_year': 1806
            }, {
                'name': 'Hoare, Prince',
                'birth_year': 1755,
                'death_year': 1834
            }, {
                'name': 'Jordan, Dorothy',
                'birth_year': 1761,
                'death_year': 1816
            }],
            'translators': [],
            'subjects': ['English drama -- 18th century', 'Farces'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68649.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68649.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68649.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68649.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68649/pg68649.cover.medium.jpg',
                'application/octet-stream':
                'https://www.gutenberg.org/files/68649/68649-0.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68649/68649-0.txt',
                'text/html':
                'https://www.gutenberg.org/files/68649/68649-h/68649-h.htm'
            },
            'download_count':
            202
        }, {
            'id':
            23580,
            'title':
            "The Children's Bible",
            'authors': [{
                'name': 'Kent, Charles Foster',
                'birth_year': 1867,
                'death_year': 1925
            }, {
                'name': 'Sherman, Henry A.',
                'birth_year': 1870,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Bible stories, English'],
            'bookshelves': ["Children's Religion"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/23580.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/23580.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/23580.rdf',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/23580/23580.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/23580.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/23580/pg23580.cover.medium.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/23580/23580.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/23580/23580-h/23580-h.htm',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/23580/23580-0.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/23580/23580-8.txt'
            },
            'download_count':
            193
        }, {
            'id':
            12236,
            'title':
            'Death Valley in \'49: Important chapter of California pioneer history. The autobiography of a pioneer, '
            'detailing his life from a humble home in the Green Mountains to the gold mines of California; '
            'and particularly reciting the sufferings of the band of men, women and children who gave '
            '"Death Valley" its name',
            'authors': [{
                'name': 'Manly, William Lewis',
                'birth_year': 1820,
                'death_year': 1903
            }],
            'translators': [],
            'subjects': [
                'California -- Biography', 'California -- Gold discoveries',
                'Death Valley (Calif. and Nev.) -- History',
                'Manly, William Lewis, 1820-',
                'Overland journeys to the Pacific',
                'Pioneers -- California -- Biography'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/12236/12236.txt',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/12236.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/12236.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/12236.epub.images',
                'application/octet-stream':
                'https://www.gutenberg.org/files/12236/12236-h/jj',
                'text/plain':
                'https://www.gutenberg.org/ebooks/12236.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/12236.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/12236/pg12236.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/12236/12236-8.zip',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/12236/12236-8.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/12236/12236-h/12236-h.htm'
            },
            'download_count':
            188
        }, {
            'id':
            19722,
            'title':
            "A Child's Garden of Verses",
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'translators': [],
            'subjects': ["Children's poetry, English"],
            'bookshelves': [
                "Children's Literature", "Children's Picture Books",
                "Children's Verse"
            ],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/19722.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/19722.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/19722.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/19722.rdf',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/19722/19722-h/19722-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/19722/pg19722.cover.small.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/19722.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/19722/19722-h.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/19722/19722.txt'
            },
            'download_count':
            185
        }, {
            'id':
            15164,
            'title':
            'Folk Tales Every Child Should Know',
            'authors': [],
            'translators': [],
            'subjects': ['Fairy tales'],
            'bookshelves':
            ["Children's Anthologies", "Children's Myths, Fairy Tales, etc."],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/15164.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/15164/15164.zip',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15164/15164-h/15164-h.htm',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/15164.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/15164.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/15164.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/15164.txt.utf-8',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/15164/15164-8.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/15164/pg15164.cover.medium.jpg'
            },
            'download_count':
            182
        }, {
            'id':
            13213,
            'title':
            'The Night Before Christmas and Other Popular Stories For Children',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': ['Christmas -- Poetry', 'Christmas stories'],
            'bookshelves': ['Christmas'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/13213/13213.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/13213/pg13213.cover.small.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/13213.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/13213.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/13213.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/13213.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/13213.html.images',
                'text/html; charset=us-ascii':
                'https://www.gutenberg.org/files/13213/13213-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/13213/13213.zip'
            },
            'download_count':
            180
        }, {
            'id':
            11592,
            'title':
            "Children's Hour with Red Riding Hood and Other Stories",
            'authors': [],
            'translators': [],
            'subjects': ['Fairy tales'],
            'bookshelves':
            ["Children's Anthologies", "Children's Picture Books"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/11592/11592-h/11592-h.htm',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/11592.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/11592.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/11592.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/11592.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/files/11592/11592-h.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/11592/pg11592.cover.small.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/11592/11592.txt'
            },
            'download_count':
            175
        }, {
            'id':
            42232,
            'title':
            "A Child's Dream of a Star",
            'authors': [{
                'name': 'Dickens, Charles',
                'birth_year': 1812,
                'death_year': 1870
            }],
            'translators': [],
            'subjects': [
                'Children -- Death -- Juvenile fiction',
                'Children and death -- Juvenile fiction',
                'Christian life -- Juvenile fiction',
                'Grief -- Juvenile fiction', 'Heaven -- Juvenile fiction',
                'Short stories'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/42232/42232.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/42232/pg42232.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/42232.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/42232.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/42232.kindle.images',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/42232/42232-0.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/42232.html.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/42232/42232-h/42232-h.htm'
            },
            'download_count':
            175
        }, {
            'id':
            25545,
            'title':
            "Children's Literature: A Textbook of Sources for Teachers and Teacher-Training Classes",
            'authors': [{
                'name': 'Curry, Charles Madison',
                'birth_year': 1869,
                'death_year': 1944
            }, {
                'name': 'Clippinger, Erle Elsworth',
                'birth_year': 1875,
                'death_year': 1939
            }],
            'translators': [],
            'subjects': [
                'Children -- Books and reading',
                "Children's literature -- Study and teaching"
            ],
            'bookshelves': ["Children's Literature"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/25545.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/25545.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/25545.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/25545.txt.utf-8',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/25545/pg25545.cover.medium.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/25545/25545-h/25545-h.htm',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/25545/25545-8.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/25545.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/25545/25545.txt',
                'application/zip':
                'https://www.gutenberg.org/files/25545/25545-8.zip'
            },
            'download_count':
            174
        }, {
            'id':
            38025,
            'title':
            'Fables for Children, Stories for Children, Natural Science Stories, Popular Education, Decembrists,'
            ' Moral Tales',
            'authors': [{
                'name': 'Tolstoy, Leo, graf',
                'birth_year': 1828,
                'death_year': 1910
            }],
            'translators': [{
                'name': 'Wiener, Leo',
                'birth_year': 1862,
                'death_year': 1939
            }],
            'subjects': ['Russian literature -- Translations into English'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/38025.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/38025.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/38025.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/38025.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/files/38025/38025-h/38025-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/38025/38025-0.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/38025/pg38025.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/38025/38025-0.zip'
            },
            'download_count':
            172
        }, {
            'id':
            17782,
            'title':
            'Animal Children: The Friends of the Forest and the Plain',
            'authors': [{
                'name': 'Kirkwood, Edith Brown',
                'birth_year': 1875,
                'death_year': 1954
            }],
            'translators': [],
            'subjects': ['Animals -- Juvenile poetry'],
            'bookshelves': ["Children's Picture Books", "Children's Verse"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/17782/pg17782.cover.small.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/17782/17782-h/17782-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/17782.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/17782/17782.txt',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/17782.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/17782.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/17782.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/17782.kindle.images'
            },
            'download_count':
            169
        }, {
            'id':
            136,
            'title':
            "A Child's Garden of Verses",
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'translators': [],
            'subjects': ["Children's poetry, English"],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/136.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/136.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/136.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/136.kindle.images',
                'text/html':
                'https://www.gutenberg.org/ebooks/136.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/136/pg136.cover.medium.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/136/136.txt'
            },
            'download_count':
            165
        }, {
            'id':
            21558,
            'title':
            'The Children of the New Forest',
            'authors': [{
                'name': 'Marryat, Frederick',
                'birth_year': 1792,
                'death_year': 1848
            }],
            'translators': [],
            'subjects': [
                'Foresters -- Juvenile fiction',
                'Great Britain -- History -- Civil War, 1642-1649 -- Juvenile fiction',
                'New Forest (England : Forest) -- Juvenile fiction',
                'Orphans -- Juvenile fiction', 'Soldiers -- Juvenile fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/21558.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/21558.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/21558.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/21558.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/21558/21558.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/21558/pg21558.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/21558/21558.zip',
                'text/html':
                'https://www.gutenberg.org/ebooks/21558.html.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/21558/21558-h/21558-h.htm'
            },
            'download_count':
            165
        }, {
            'id':
            46597,
            'title':
            'In Search of the Castaways: A Romantic Narrative of the Loss of Captain Grant of the Brig Britannia '
            'and of the Adventures of His Children and Friends in His Discovery and Rescue',
            'authors': [{
                'name': 'Verne, Jules',
                'birth_year': 1828,
                'death_year': 1905
            }],
            'translators': [],
            'subjects': [
                'Australia -- Fiction', 'Castaways -- Fiction',
                'New Zealand -- Fiction', 'Ocean travel -- Fiction',
                'Seafaring life -- Fiction', 'Ship captains -- Fiction',
                'South America -- Fiction', 'Voyages and travels -- Fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/46597/46597.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/46597/46597-8.txt',
                'text/html':
                'https://www.gutenberg.org/files/46597/46597-h/46597-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/46597/pg46597.cover.medium.jpg',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/46597.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/46597.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/46597.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/46597.kindle.images'
            },
            'download_count':
            161
        }, {
            'id':
            27175,
            'title':
            "The Bad Child's Book of Beasts",
            'authors': [{
                'name': 'Belloc, Hilaire',
                'birth_year': 1870,
                'death_year': 1953
            }],
            'translators': [],
            'subjects': [
                'Animals -- Juvenile poetry', "Children's poetry, English",
                'Nonsense verses'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/27175.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/27175.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/27175.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/27175.kindle.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/27175/27175-h/27175-h.htm',
                'application/zip':
                'https://www.gutenberg.org/files/27175/27175-h.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/27175/pg27175.cover.medium.jpg',
                'text/html':
                'https://www.gutenberg.org/ebooks/27175.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/27175/27175.txt'
            },
            'download_count':
            158
        }, {
            'id':
            30272,
            'title':
            'Very Short Stories and Verses For Children',
            'authors': [{
                'name': 'Clifford, W. K., Mrs.',
                'birth_year': None,
                'death_year': 1929
            }],
            'translators': [],
            'subjects':
            ["Children's poetry, English", "Children's stories, English"],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/30272.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/30272.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/30272.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/30272.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/30272.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/30272/30272.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/30272/pg30272.cover.small.jpg',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/30272/30272-h.zip'
            },
            'download_count':
            158
        }, {
            'id':
            62928,
            'title':
            'Child Whispers',
            'authors': [{
                'name': 'Blyton, Enid',
                'birth_year': 1897,
                'death_year': 1968
            }],
            'translators': [],
            'subjects': ["Children's poetry, English"],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/62928.kindle.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/62928.txt.utf-8',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/62928.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/62928.epub.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/62928/pg62928.cover.medium.jpg',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/62928/62928.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/62928.html.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/62928/62928-h/62928-h.htm'
            },
            'download_count':
            157
        }, {
            'id':
            29259,
            'title':
            'The Child and the Curriculum',
            'authors': [{
                'name': 'Dewey, John',
                'birth_year': 1859,
                'death_year': 1952
            }],
            'translators': [],
            'subjects': ['Education'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/29259/29259-8.txt',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/29259.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/29259.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/29259.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/29259.txt.utf-8',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/29259/29259-h/29259-h.htm',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/29259/29259.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/29259.html.images',
                'application/zip':
                'https://www.gutenberg.org/files/29259/29259-8.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/29259/pg29259.cover.small.jpg'
            },
            'download_count':
            154
        }, {
            'id':
            68080,
            'title':
            'Incidents of childhood',
            'authors': [{
                'name': 'Anonymous',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': [
                'Children -- Conduct of life -- Juvenile fiction',
                "Children's stories", 'Conduct of life -- Juvenile fiction'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/octet-stream':
                'https://www.gutenberg.org/files/68080/68080-0.zip',
                'text/html':
                'https://www.gutenberg.org/files/68080/68080-h/68080-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/68080/pg68080.cover.medium.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/68080.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/68080.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/68080.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/68080.epub.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/68080/68080-0.txt'
            },
            'download_count':
            153
        }, {
            'id':
            26990,
            'title':
            "Holy in Christ: Thoughts on the Calling of God's Children to be Holy as He is Holy",
            'authors': [{
                'name': 'Murray, Andrew',
                'birth_year': 1828,
                'death_year': 1917
            }],
            'translators': [],
            'subjects': ['Holiness'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain':
                'https://www.gutenberg.org/ebooks/26990.txt.utf-8',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/26990.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/26990.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/26990.rdf',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/26990/pg26990.cover.medium.jpg',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/26990/26990-8.txt',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/26990/26990-h/26990-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/26990.html.images',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/26990/26990.zip',
                'application/zip':
                'https://www.gutenberg.org/files/26990/26990-8.zip'
            },
            'download_count':
            149
        }, {
            'id':
            20817,
            'title':
            'The Mother and Her Child',
            'authors': [{
                'name': 'Sadler, William S. (William Samuel)',
                'birth_year': 1875,
                'death_year': 1969
            }, {
                'name': 'Sadler, Lena K. (Lena Kellogg)',
                'birth_year': 1875,
                'death_year': None
            }],
            'translators': [],
            'subjects': [
                'Child care', 'Infants -- Care',
                'Infants -- Health and hygiene', 'Pregnancy'
            ],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/20817.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/20817.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/20817.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/20817.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/20817/20817.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20817/20817-8.txt',
                'text/html':
                'https://www.gutenberg.org/files/20817/20817-h/20817-h.htm',
                'application/zip':
                'https://www.gutenberg.org/files/20817/20817-8.zip',
                'application/octet-stream':
                'https://www.gutenberg.org/files/20817/20817-page-images.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/20817/pg20817.cover.medium.jpg'
            },
            'download_count':
            146
        }, {
            'id':
            14411,
            'title':
            "The Children's Six Minutes",
            'authors': [{
                'name': 'Wright, Bruce S. (Bruce Simpson)',
                'birth_year': 1879,
                'death_year': 1942
            }],
            'translators': [],
            'subjects': ["Children's sermons"],
            'bookshelves': ["Children's Religion"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/14411/14411.txt',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/14411.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/14411.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/14411.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/14411.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/14411.html.images',
                'text/html; charset=us-ascii':
                'https://www.gutenberg.org/files/14411/14411-h.zip',
                'application/zip':
                'https://www.gutenberg.org/files/14411/14411.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/14411/pg14411.cover.small.jpg'
            },
            'download_count':
            143
        }, {
            'id':
            43984,
            'title':
            'Chaucer for Children: A Golden Key',
            'authors': [{
                'name': 'Chaucer, Geoffrey',
                'birth_year': 1342,
                'death_year': 1400
            }],
            'translators': [],
            'subjects': ['Chaucer, Geoffrey, -1400 -- Adaptations'],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/html':
                'https://www.gutenberg.org/ebooks/43984.html.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/43984/43984-h/43984-h.htm',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/43984/43984-8.txt',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/43984.epub.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/43984.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/43984.rdf',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/43984/43984-0.txt',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/43984/43984.txt',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/43984/pg43984.cover.medium.jpg'
            },
            'download_count':
            143
        }, {
            'id':
            2841,
            'title':
            'The Ivory Child',
            'authors': [{
                'name': 'Haggard, H. Rider (Henry Rider)',
                'birth_year': 1856,
                'death_year': 1925
            }],
            'translators': [],
            'subjects': [
                'Adventure stories', 'Fantasy fiction, English',
                'Quatermain, Allan (Fictitious character) -- Fiction'
            ],
            'bookshelves': ['Adventure'],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/2841.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/2841.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/2841.epub.images',
                'text/html':
                'https://www.gutenberg.org/ebooks/2841.html.images',
                'text/html; charset=utf-8':
                'https://www.gutenberg.org/files/2841/2841-h/2841-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/2841/pg2841.cover.medium.jpg',
                'text/plain; charset=utf-8':
                'https://www.gutenberg.org/files/2841/2841-0.txt'
            },
            'download_count':
            140
        }, {
            'id':
            10541,
            'title':
            "Children's Classics in Dramatic Form, A Reader for the Fourth Grade",
            'authors': [{
                'name': 'Stevenson, Augusta',
                'birth_year': 1869,
                'death_year': 1976
            }],
            'translators': [],
            'subjects': ["Children's plays"],
            'bookshelves': [],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/10541.kindle.images',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/10541/10541-h/10541-h.htm',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/10541.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/10541.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/10541.txt.utf-8',
                'text/html':
                'https://www.gutenberg.org/ebooks/10541.html.images',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/10541/10541-8.zip',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/10541/10541.txt',
                'application/zip':
                'https://www.gutenberg.org/files/10541/10541.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/10541/pg10541.cover.small.jpg'
            },
            'download_count':
            140
        }, {
            'id':
            20015,
            'title':
            'The Child of Pleasure',
            'authors': [{
                'name': "D'Annunzio, Gabriele",
                'birth_year': 1863,
                'death_year': 1938
            }],
            'translators': [{
                'name': 'Symons, Arthur',
                'birth_year': 1865,
                'death_year': 1945
            }, {
                'name': 'Harding, Georgina',
                'birth_year': None,
                'death_year': None
            }],
            'subjects': ['Fiction'],
            'bookshelves': ["Banned Books from Anne Haight's list"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/20015/20015.txt',
                'text/plain; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20015/20015-8.txt',
                'text/html':
                'https://www.gutenberg.org/ebooks/20015.html.images',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/20015/pg20015.cover.medium.jpg',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/20015.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/20015.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/20015.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/20015.txt.utf-8',
                'text/html; charset=iso-8859-1':
                'https://www.gutenberg.org/files/20015/20015-h/20015-h.htm'
            },
            'download_count':
            140
        }, {
            'id':
            17162,
            'title':
            'Mother Stories from the Old Testament: A Book of the Best Stories from the Old Testament that Mothers '
            'can tell their Children',
            'authors': [{
                'name': 'Anonymous',
                'birth_year': None,
                'death_year': None
            }],
            'translators': [],
            'subjects': [
                'Bible stories, English',
                'Bible. Old Testament -- Juvenile literature'
            ],
            'bookshelves': ["Children's Picture Books", "Children's Religion"],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/17162/17162.txt',
                'text/html; charset=us-ascii':
                'https://www.gutenberg.org/files/17162/17162-h/17162-h.htm',
                'text/html':
                'https://www.gutenberg.org/ebooks/17162.html.images',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/17162.kindle.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/17162.rdf',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/17162.epub.images',
                'text/plain':
                'https://www.gutenberg.org/ebooks/17162.txt.utf-8',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/17162/pg17162.cover.small.jpg',
                'application/zip':
                'https://www.gutenberg.org/files/17162/17162-h.zip'
            },
            'download_count':
            139
        }, {
            'id':
            16537,
            'title':
            'Myths That Every Child Should Know: A Selection Of The Classic Myths Of All Times For Young People',
            'authors': [],
            'translators': [],
            'subjects': ['Mythology -- Juvenile literature'],
            'bookshelves':
            ["Children's Anthologies", "Children's Myths, Fairy Tales, etc."],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'application/octet-stream':
                'https://www.gutenberg.org/files/16537/16537-h.zip',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/16537.rdf',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/16537.kindle.images',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/16537.epub.images',
                'application/zip':
                'https://www.gutenberg.org/files/16537/16537-0.zip',
                'text/html':
                'https://www.gutenberg.org/files/16537/16537-h/16537-h.htm',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/16537/pg16537.cover.medium.jpg',
                'text/plain':
                'https://www.gutenberg.org/ebooks/16537.txt.utf-8',
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/16537/16537-0.txt'
            },
            'download_count':
            138
        }]
    }


@patch('requests.get')
def test_get_books_success(requests_mock):
    success_response = Mock()
    success_response.json.return_value = success_returned_value()
    success_response.raise_for_status.side_effect = None

    requests_mock.return_value = success_response
    response = client.get('/books')
    assert response.status_code == 200
    assert response.json() == {
        'pagination': {
            'page': 1,
            'count': 68800,
            'pages': 2150,
            'page_size': 32
        },
        'books': [{
            'id':
            1342,
            'title':
            'Pride and Prejudice',
            'authors': [{
                'name': 'Austen, Jane',
                'birth_year': 1775,
                'death_year': 1817
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1661,
            'title':
            'The Adventures of Sherlock Holmes',
            'authors': [{
                'name': 'Doyle, Arthur Conan',
                'birth_year': 1859,
                'death_year': 1930
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            11,
            'title':
            "Alice's Adventures in Wonderland",
            'authors': [{
                'name': 'Carroll, Lewis',
                'birth_year': 1832,
                'death_year': 1898
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            84,
            'title':
            'Frankenstein; Or, The Modern Prometheus',
            'authors': [{
                'name': 'Shelley, Mary Wollstonecraft',
                'birth_year': 1797,
                'death_year': 1851
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            505,
            'title':
            'History of the Warfare of Science with Theology in Christendom',
            'authors': [{
                'name': 'White, Andrew Dickson',
                'birth_year': 1832,
                'death_year': 1918
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            27107,
            'title':
            '金雲翹傳',
            'authors': [{
                'name': 'Qingxincairen',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['zh'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            345,
            'title':
            'Dracula',
            'authors': [{
                'name': 'Stoker, Bram',
                'birth_year': 1847,
                'death_year': 1912
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            2701,
            'title':
            'Moby Dick; Or, The Whale',
            'authors': [{
                'name': 'Melville, Herman',
                'birth_year': 1819,
                'death_year': 1891
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            174,
            'title':
            'The Picture of Dorian Gray',
            'authors': [{
                'name': 'Wilde, Oscar',
                'birth_year': 1854,
                'death_year': 1900
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            98,
            'title':
            'A Tale of Two Cities',
            'authors': [{
                'name': 'Dickens, Charles',
                'birth_year': 1812,
                'death_year': 1870
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            33283,
            'title':
            'Calculus Made Easy: Being a very-simplest introduction to those beautiful methods which are generally '
            'called by the terrifying names of the Differential Calculus and the Integral Calculus',
            'authors': [{
                'name': 'Thompson, Silvanus P. (Silvanus Phillips)',
                'birth_year': 1851,
                'death_year': 1916
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            4300,
            'title':
            'Ulysses',
            'authors': [{
                'name': 'Joyce, James',
                'birth_year': 1882,
                'death_year': 1941
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1952,
            'title':
            'The Yellow Wallpaper',
            'authors': [{
                'name': 'Gilman, Charlotte Perkins',
                'birth_year': 1860,
                'death_year': 1935
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1184,
            'title':
            'The Count of Monte Cristo, Illustrated',
            'authors': [{
                'name': 'Dumas, Alexandre',
                'birth_year': 1802,
                'death_year': 1870
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            105,
            'title':
            'Persuasion',
            'authors': [{
                'name': 'Austen, Jane',
                'birth_year': 1775,
                'death_year': 1817
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1232,
            'title':
            'The Prince',
            'authors': [{
                'name': 'Machiavelli, Niccolò',
                'birth_year': 1469,
                'death_year': 1527
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            64317,
            'title':
            'The Great Gatsby',
            'authors': [{
                'name': 'Fitzgerald, F. Scott (Francis Scott)',
                'birth_year': 1896,
                'death_year': 1940
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            2600,
            'title':
            'War and Peace',
            'authors': [{
                'name': 'Tolstoy, Leo, graf',
                'birth_year': 1828,
                'death_year': 1910
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            2554,
            'title':
            'Crime and Punishment',
            'authors': [{
                'name': 'Dostoyevsky, Fyodor',
                'birth_year': 1821,
                'death_year': 1881
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            2591,
            'title':
            "Grimms' Fairy Tales",
            'authors': [{
                'name': 'Grimm, Wilhelm',
                'birth_year': 1786,
                'death_year': 1859
            }, {
                'name': 'Grimm, Jacob',
                'birth_year': 1785,
                'death_year': 1863
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            30254,
            'title':
            'The Romance of Lust: A classic Victorian erotic novel',
            'authors': [{
                'name': 'Anonymous',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1260,
            'title':
            'Jane Eyre: An Autobiography',
            'authors': [{
                'name': 'Brontë, Charlotte',
                'birth_year': 1816,
                'death_year': 1855
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            6130,
            'title':
            'The Iliad',
            'authors': [{
                'name': 'Homer',
                'birth_year': -750,
                'death_year': -650
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1400,
            'title':
            'Great Expectations',
            'authors': [{
                'name': 'Dickens, Charles',
                'birth_year': 1812,
                'death_year': 1870
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            43,
            'title':
            'The Strange Case of Dr. Jekyll and Mr. Hyde',
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            5200,
            'title':
            'Metamorphosis',
            'authors': [{
                'name': 'Kafka, Franz',
                'birth_year': 1883,
                'death_year': 1924
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1080,
            'title':
            'A Modest Proposal: For preventing the children of poor people in Ireland, from being a burden on their '
            'parents or country, and for making them beneficial to the publick',
            'authors': [{
                'name': 'Swift, Jonathan',
                'birth_year': 1667,
                'death_year': 1745
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            74,
            'title':
            'The Adventures of Tom Sawyer, Complete',
            'authors': [{
                'name': 'Twain, Mark',
                'birth_year': 1835,
                'death_year': 1910
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            58585,
            'title':
            'The Prophet',
            'authors': [{
                'name': 'Gibran, Kahlil',
                'birth_year': 1883,
                'death_year': 1931
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            13790,
            'title':
            'Life And Letters Of John Gay (1685-1732), Author of "The Beggar\'s Opera"',
            'authors': [{
                'name': 'Melville, Lewis',
                'birth_year': 1874,
                'death_year': 1932
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            35,
            'title':
            'The Time Machine',
            'authors': [{
                'name': 'Wells, H. G. (Herbert George)',
                'birth_year': 1866,
                'death_year': 1946
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            514,
            'title':
            'Little Women',
            'authors': [{
                'name': 'Alcott, Louisa May',
                'birth_year': 1832,
                'death_year': 1888
            }],
            'languages': ['en'],
            'download_count':
            1000,
            'reviews':
            None,
            'average_rating':
            None
        }]
    }


@patch('requests.get')
def test_get_books_http_error(requests_mock):
    fail_response = Mock()
    fail_response.status_code = 500
    fail_response.raise_for_status.side_effect = HTTPError(
        'Gutendex not working')
    requests_mock.return_value = fail_response
    response = client.get('/books')
    assert response.status_code == 500
    assert response.json() == {'message': 'Gutendex not working'}


@patch('requests.get')
def test_get_book_by_id_success(requests_mock):
    success_response = Mock()
    success_response.json.return_value = success_returned_value_book_id_80()
    success_response.raise_for_status.side_effect = None

    requests_mock.return_value = success_response
    response = client.get('/books?book_id=80')
    assert response.status_code == 200
    assert response.json() == {
        'pagination': {
            'page': 1,
            'count': 1,
            'pages': 1,
            'page_size': 1
        },
        'books': [{
            'id':
            80,
            'title':
            'The Online World',
            'authors': [{
                'name': 'De Presno, Odd',
                'birth_year': 1944,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            31,
            'reviews':
            None,
            'average_rating':
            None
        }]
    }


@patch('requests.get')
def test_get_book_not_found(requests_mock):
    fail_response = Mock()
    fail_response.status_code = 200
    fail_response.json.return_value = book_not_found()

    requests_mock.return_value = fail_response
    response = client.get('/books?book_id=800000')
    assert response.status_code == 404
    assert response.json() == {'message': 'Book not found'}


@patch('requests.get')
def test_get_book_by_title_success(requests_mock):
    success_response = Mock()
    success_response.json.return_value = success_book_by_title()
    success_response.raise_for_status.side_effect = None

    requests_mock.return_value = success_response
    response = client.get('/books?title=colors')
    assert response.status_code == 200
    assert response.json() == {
        'pagination': {
            'page': 1,
            'count': 22,
            'pages': 1,
            'page_size': 22
        },
        'books': [{
            'id':
            22739,
            'title':
            'The Human Aura: Astral Colors and Thought Forms',
            'authors': [{
                'name': 'Atkinson, William Walker',
                'birth_year': 1862,
                'death_year': 1932
            }],
            'languages': ['en'],
            'download_count':
            232,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            20796,
            'title':
            'The Colors of Space',
            'authors': [{
                'name': 'Bradley, Marion Zimmer',
                'birth_year': 1930,
                'death_year': 1999
            }],
            'languages': ['en'],
            'download_count':
            145,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            30000,
            'title':
            'The Bird Book: Illustrating in natural colors more than seven hundred North American birds; also several '
            'hundred photographs of their nests and eggs.',
            'authors': [{
                'name': 'Reed, Chester A. (Chester Albert)',
                'birth_year': 1876,
                'death_year': 1912
            }],
            'languages': ['en'],
            'download_count':
            97,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            30877,
            'title':
            'The Painter in Oil: A complete treatise on the principles and technique necessary to the painting of '
            'pictures in oil colors',
            'authors': [{
                'name': 'Parkhurst, Daniel Burleigh',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            82,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            53647,
            'title':
            'Texas Flowers in Natural Colors',
            'authors': [{
                'name': 'Whitehouse, Eula',
                'birth_year': 1892,
                'death_year': 1974
            }],
            'languages': ['en'],
            'download_count':
            51,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            23085,
            'title':
            'The Colors of Space',
            'authors': [{
                'name': 'Bradley, Marion Zimmer',
                'birth_year': 1930,
                'death_year': 1999
            }],
            'languages': ['en'],
            'download_count':
            42,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            27016,
            'title':
            'Eight dwelling places of Buddhist immortals',
            'authors': [{
                'name': 'Five colors stone',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['zh'],
            'download_count':
            40,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            28328,
            'title':
            'Americanism Contrasted with Foreignism, Romanism, and Bogus Democracy in the Light of Reason, History, '
            'and Scripture;: In which Certain Demagogues in Tennessee, and Elsewhere,; are Shown Up in Their '
            'True Colors',
            'authors': [{
                'name': 'Brownlow, William Gannaway',
                'birth_year': 1805,
                'death_year': 1877
            }],
            'languages': ['en'],
            'download_count':
            40,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            52800,
            'title':
            "Lowney's Cook Book: Illustrated in Colors",
            'authors': [{
                'name': 'Howard, Maria Willett',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            36,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            32173,
            'title':
            'Under Boy Scout Colors',
            'authors': [{
                'name': 'Ames, Joseph Bushnell',
                'birth_year': 1878,
                'death_year': 1928
            }],
            'languages': ['en'],
            'download_count':
            32,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            43500,
            'title':
            "Graining and Marbling: A Series of Practical Treatises on Material, Tools and Appliances Used; General "
            "Operations; Preparing Oil Graining Colors; Mixing; Rubbing; Applying Distemper Colors; Wiping Out; "
            "Penciling; The Use of Crayons; Review of Woods; The Graining of Oak, Ash, Cherry, Satinwood, Mahogany, "
            "Maple, Bird's Eye Maple, Sycamore, Walnut, Etc.; Marbling in All Shades.",
            'authors': [{
                'name': 'Maire, F. (Frederick)',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            32,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            20986,
            'title':
            'Tom Slade with the Colors',
            'authors': [{
                'name': 'Fitzhugh, Percy Keese',
                'birth_year': 1876,
                'death_year': 1950
            }],
            'languages': ['en'],
            'download_count':
            29,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            63087,
            'title':
            'Color Standards and Color Nomenclature: With fifty-three colored plates and eleven hundred and fifteen '
            'named colors',
            'authors': [{
                'name': 'Ridgway, Robert',
                'birth_year': 1850,
                'death_year': 1929
            }],
            'languages': ['en'],
            'download_count':
            29,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            36051,
            'title':
            'Colors of Life: Poems and Songs and Sonnets',
            'authors': [{
                'name': 'Eastman, Max',
                'birth_year': 1883,
                'death_year': 1969
            }],
            'languages': ['en'],
            'download_count':
            20,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            41749,
            'title':
            'Practical Graining, with Description of Colors Employed and Tools Used',
            'authors': [{
                'name': 'Wall, William E. (William Edmund)',
                'birth_year': 1858,
                'death_year': 1934
            }],
            'languages': ['en'],
            'download_count':
            20,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            62275,
            'title':
            'West Point Colors',
            'authors': [{
                'name': 'Warner, Anna Bartlett',
                'birth_year': 1824,
                'death_year': 1915
            }],
            'languages': ['en'],
            'download_count':
            13,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            20072,
            'title':
            'With the Colors: Songs of the American Service',
            'authors': [{
                'name': 'Appleton, Everard Jack',
                'birth_year': 1872,
                'death_year': 1931
            }],
            'languages': ['en'],
            'download_count':
            10,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            48141,
            'title':
            'Birds and All Nature, Vol. 6, No. 4, November 1899: In Natural Colors',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            9,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            48503,
            'title':
            'Birds and Nature, Vol. 08, No. 1, June 1900: In Natural Colors',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            8,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            15179,
            'title':
            'The Inner Sisterhood: A Social Study in High Colors',
            'authors': [{
                'name': 'Sherley, Douglass',
                'birth_year': 1857,
                'death_year': 1917
            }],
            'languages': ['en'],
            'download_count':
            7,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            45079,
            'title':
            'The Art of Graining: How Acquired and How Produced.: With the description of colors and their '
            'applications.',
            'authors': [{
                'name': 'Pickert, Charles',
                'birth_year': None,
                'death_year': None
            }, {
                'name': 'Metcalf, A.',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            6,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            28391,
            'title':
            'True To His Colors',
            'authors': [{
                'name': 'Castlemon, Harry',
                'birth_year': 1842,
                'death_year': 1915
            }],
            'languages': ['en'],
            'download_count':
            3,
            'reviews':
            None,
            'average_rating':
            None
        }]
    }


@patch('requests.get')
def test_get_books_page_10(requests_mock):
    success_response = Mock()
    success_response.json.return_value = success_return_page_10()
    success_response.raise_for_status.side_effect = None

    requests_mock.return_value = success_response
    response = client.get('/books?page=10')
    assert response.status_code == 200
    assert response.json() == {
        'pagination': {
            'page': 10,
            'count': 68800,
            'pages': 2150,
            'page_size': 32
        },
        'books': [{
            'id':
            68283,
            'title':
            'The call of Cthulhu',
            'authors': [{
                'name': 'Lovecraft, H. P. (Howard Phillips)',
                'birth_year': 1890,
                'death_year': 1937
            }],
            'languages': ['en'],
            'download_count':
            1494,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            13415,
            'title':
            'The Lady with the Dog and Other Stories',
            'authors': [{
                'name': 'Chekhov, Anton Pavlovich',
                'birth_year': 1860,
                'death_year': 1904
            }],
            'languages': ['en'],
            'download_count':
            1491,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            22381,
            'title':
            'Myths and Legends of Ancient Greece and Rome',
            'authors': [{
                'name': 'Berens, E. M.',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1487,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            27805,
            'title':
            'The Wind in the Willows',
            'authors': [{
                'name': 'Grahame, Kenneth',
                'birth_year': 1859,
                'death_year': 1932
            }],
            'languages': ['en'],
            'download_count':
            1487,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            38769,
            'title':
            'A Course of Pure Mathematics: Third Edition',
            'authors': [{
                'name': 'Hardy, G. H. (Godfrey Harold)',
                'birth_year': 1877,
                'death_year': 1947
            }],
            'languages': ['en'],
            'download_count':
            1487,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            61168,
            'title':
            'The Man in the Brown Suit',
            'authors': [{
                'name': 'Christie, Agatha',
                'birth_year': 1890,
                'death_year': 1976
            }],
            'languages': ['en'],
            'download_count':
            1483,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            28890,
            'title':
            'Helps to Latin Translation at Sight',
            'authors': [{
                'name': 'Luce, Edmund',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1471,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            14264,
            'title':
            'The Practice and Science of Drawing',
            'authors': [{
                'name': 'Speed, Harold',
                'birth_year': 1873,
                'death_year': 1957
            }],
            'languages': ['en'],
            'download_count':
            1468,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            3160,
            'title':
            'The Odyssey',
            'authors': [{
                'name': 'Homer',
                'birth_year': -750,
                'death_year': -650
            }],
            'languages': ['en'],
            'download_count':
            1465,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            68815,
            'title':
            'Galactic Patrol',
            'authors': [{
                'name': 'Smith, E. E. (Edward Elmer)',
                'birth_year': 1890,
                'death_year': 1965
            }],
            'languages': ['en'],
            'download_count':
            1463,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            10609,
            'title':
            'English Literature: Its History and Its Significance for the Life of the English-Speaking World',
            'authors': [{
                'name': 'Long, William J. (William Joseph)',
                'birth_year': 1867,
                'death_year': 1952
            }],
            'languages': ['en'],
            'download_count':
            1457,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            61221,
            'title':
            'A Passage to India',
            'authors': [{
                'name': 'Forster, E. M. (Edward Morgan)',
                'birth_year': 1879,
                'death_year': 1970
            }],
            'languages': ['en'],
            'download_count':
            1456,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 10947,
            'title': 'The Best American Humorous Short Stories',
            'authors': [],
            'languages': ['en'],
            'download_count': 1454,
            'reviews': None,
            'average_rating': None
        }, {
            'id':
            68717,
            'title':
            'The American scene',
            'authors': [{
                'name': 'James, Henry',
                'birth_year': 1843,
                'death_year': 1916
            }],
            'languages': ['en'],
            'download_count':
            1452,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            68829,
            'title':
            'Mistake inside',
            'authors': [{
                'name': 'Blish, James',
                'birth_year': 1921,
                'death_year': 1975
            }],
            'languages': ['en'],
            'download_count':
            1449,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 15474,
            'title':
            'The Mahabharata of Krishna-Dwaipayana Vyasa, Volume 1: Books 1, 2 and 3',
            'authors': [],
            'languages': ['en'],
            'download_count': 1446,
            'reviews': None,
            'average_rating': None
        }, {
            'id':
            6087,
            'title':
            'The Vampyre; a Tale',
            'authors': [{
                'name': 'Polidori, John William',
                'birth_year': 1795,
                'death_year': 1821
            }],
            'languages': ['en'],
            'download_count':
            1445,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            22120,
            'title':
            "Chaucer's Works, Volume 4 — The Canterbury Tales",
            'authors': [{
                'name': 'Chaucer, Geoffrey',
                'birth_year': 1342,
                'death_year': 1400
            }],
            'languages': ['enm'],
            'download_count':
            1445,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            32,
            'title':
            'Herland',
            'authors': [{
                'name': 'Gilman, Charlotte Perkins',
                'birth_year': 1860,
                'death_year': 1935
            }],
            'languages': ['en'],
            'download_count':
            1443,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            500,
            'title':
            'The Adventures of Pinocchio',
            'authors': [{
                'name': 'Collodi, Carlo',
                'birth_year': 1826,
                'death_year': 1890
            }],
            'languages': ['en'],
            'download_count':
            1437,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            1600,
            'title':
            'Symposium',
            'authors': [{
                'name': 'Plato',
                'birth_year': -428,
                'death_year': -348
            }],
            'languages': ['en'],
            'download_count':
            1430,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            68662,
            'title':
            'Elements of arithmetic',
            'authors': [{
                'name': 'De Morgan, Augustus',
                'birth_year': 1806,
                'death_year': 1871
            }],
            'languages': ['en'],
            'download_count':
            1429,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            503,
            'title':
            'The Blue Fairy Book',
            'authors': [{
                'name': 'Lang, Andrew',
                'birth_year': 1844,
                'death_year': 1912
            }],
            'languages': ['en'],
            'download_count':
            1427,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            9105,
            'title':
            'Reflections; or Sentences and Moral Maxims',
            'authors': [{
                'name': 'La Rochefoucauld, François duc de',
                'birth_year': 1613,
                'death_year': 1680
            }],
            'languages': ['en'],
            'download_count':
            1424,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            33044,
            'title':
            'Birds from North Borneo: University of Kansas Publications, Museum of Natural History, Volume 17, No. 8, '
            'pp. 377-433, October 27, 1966',
            'authors': [{
                'name': 'Thompson, Max C.',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1421,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            60,
            'title':
            'The Scarlet Pimpernel',
            'authors': [{
                'name': 'Orczy, Emmuska Orczy, Baroness',
                'birth_year': 1865,
                'death_year': 1947
            }],
            'languages': ['en'],
            'download_count':
            1419,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            155,
            'title':
            'The Moonstone',
            'authors': [{
                'name': 'Collins, Wilkie',
                'birth_year': 1824,
                'death_year': 1889
            }],
            'languages': ['en'],
            'download_count':
            1412,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            4705,
            'title':
            'A Treatise of Human Nature',
            'authors': [{
                'name': 'Hume, David',
                'birth_year': 1711,
                'death_year': 1776
            }],
            'languages': ['en'],
            'download_count':
            1410,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            33451,
            'title':
            'The Atlantic Monthly, Volume 20, No. 119, September, 1867: A Magazine of Literature, Science, Art, '
            'and Politics',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1407,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            805,
            'title':
            'This Side of Paradise',
            'authors': [{
                'name': 'Fitzgerald, F. Scott (Francis Scott)',
                'birth_year': 1896,
                'death_year': 1940
            }],
            'languages': ['en'],
            'download_count':
            1405,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            45631,
            'title':
            'Twelve Years a Slave: Narrative of Solomon Northup, a Citizen of New-York, Kidnapped in Washington City '
            'in 1841, and Rescued in 1853, from a Cotton Plantation near the Red River in Louisiana',
            'authors': [{
                'name': 'Northup, Solomon',
                'birth_year': 1808,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            1402,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            9662,
            'title':
            'An Enquiry Concerning Human Understanding',
            'authors': [{
                'name': 'Hume, David',
                'birth_year': 1711,
                'death_year': 1776
            }],
            'languages': ['en'],
            'download_count':
            1397,
            'reviews':
            None,
            'average_rating':
            None
        }]
    }


@patch('requests.get')
def test_get_books_title_and_page_success(requests_mock):
    success_response = Mock()
    success_response.json.return_value = success_return_page_2_of_child_titles(
    )
    success_response.raise_for_status.side_effect = None

    requests_mock.return_value = success_response
    response = client.get('/books?page=2&title=child')
    assert response.status_code == 200
    assert response.json() == {
        'pagination': {
            'page': 2,
            'count': 610,
            'pages': 20,
            'page_size': 32
        },
        'books': [{
            'id':
            15484,
            'title':
            "The Care and Feeding of Children: A Catechism for the Use of Mothers and Children's Nurses",
            'authors': [{
                'name': 'Holt, L. Emmett (Luther Emmett)',
                'birth_year': 1855,
                'death_year': 1924
            }],
            'languages': ['en'],
            'download_count':
            226,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            22096,
            'title':
            'Stories the Iroquois Tell Their Children',
            'authors': [{
                'name': 'Powers, Mabel',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            222,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            28402,
            'title':
            'The Sexual Life of the Child',
            'authors': [{
                'name': 'Moll, Albert',
                'birth_year': 1862,
                'death_year': 1939
            }],
            'languages': ['en'],
            'download_count':
            206,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 14916,
            'title': 'Fairy Tales Every Child Should Know',
            'authors': [],
            'languages': ['en'],
            'download_count': 203,
            'reviews': None,
            'average_rating': None
        }, {
            'id':
            68649,
            'title':
            "The spoil'd child: A farce, in two acts, as performed at the Theatre Royal, Drury Lane",
            'authors': [{
                'name': 'Bickerstaff, Isaac',
                'birth_year': 1735,
                'death_year': 1812
            }, {
                'name': 'Ford, Richard, Sir',
                'birth_year': None,
                'death_year': 1806
            }, {
                'name': 'Hoare, Prince',
                'birth_year': 1755,
                'death_year': 1834
            }, {
                'name': 'Jordan, Dorothy',
                'birth_year': 1761,
                'death_year': 1816
            }],
            'languages': ['en'],
            'download_count':
            202,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            23580,
            'title':
            "The Children's Bible",
            'authors': [{
                'name': 'Kent, Charles Foster',
                'birth_year': 1867,
                'death_year': 1925
            }, {
                'name': 'Sherman, Henry A.',
                'birth_year': 1870,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            193,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            12236,
            'title':
            'Death Valley in \'49: Important chapter of California pioneer history. The autobiography of a pioneer, '
            'detailing his life from a humble home in the Green Mountains to the gold mines of California; and '
            'particularly reciting the sufferings of the band of men, women and children who gave '
            '"Death Valley" its name',
            'authors': [{
                'name': 'Manly, William Lewis',
                'birth_year': 1820,
                'death_year': 1903
            }],
            'languages': ['en'],
            'download_count':
            188,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            19722,
            'title':
            "A Child's Garden of Verses",
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'languages': ['en'],
            'download_count':
            185,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 15164,
            'title': 'Folk Tales Every Child Should Know',
            'authors': [],
            'languages': ['en'],
            'download_count': 182,
            'reviews': None,
            'average_rating': None
        }, {
            'id':
            13213,
            'title':
            'The Night Before Christmas and Other Popular Stories For Children',
            'authors': [{
                'name': 'Various',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            180,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 11592,
            'title': "Children's Hour with Red Riding Hood and Other Stories",
            'authors': [],
            'languages': ['en'],
            'download_count': 175,
            'reviews': None,
            'average_rating': None
        }, {
            'id':
            42232,
            'title':
            "A Child's Dream of a Star",
            'authors': [{
                'name': 'Dickens, Charles',
                'birth_year': 1812,
                'death_year': 1870
            }],
            'languages': ['en'],
            'download_count':
            175,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            25545,
            'title':
            "Children's Literature: A Textbook of Sources for Teachers and Teacher-Training Classes",
            'authors': [{
                'name': 'Curry, Charles Madison',
                'birth_year': 1869,
                'death_year': 1944
            }, {
                'name': 'Clippinger, Erle Elsworth',
                'birth_year': 1875,
                'death_year': 1939
            }],
            'languages': ['en'],
            'download_count':
            174,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            38025,
            'title':
            'Fables for Children, Stories for Children, Natural Science Stories, Popular Education, Decembrists, '
            'Moral Tales',
            'authors': [{
                'name': 'Tolstoy, Leo, graf',
                'birth_year': 1828,
                'death_year': 1910
            }],
            'languages': ['en'],
            'download_count':
            172,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            17782,
            'title':
            'Animal Children: The Friends of the Forest and the Plain',
            'authors': [{
                'name': 'Kirkwood, Edith Brown',
                'birth_year': 1875,
                'death_year': 1954
            }],
            'languages': ['en'],
            'download_count':
            169,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            136,
            'title':
            "A Child's Garden of Verses",
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'languages': ['en'],
            'download_count':
            165,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            21558,
            'title':
            'The Children of the New Forest',
            'authors': [{
                'name': 'Marryat, Frederick',
                'birth_year': 1792,
                'death_year': 1848
            }],
            'languages': ['en'],
            'download_count':
            165,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            46597,
            'title':
            'In Search of the Castaways: A Romantic Narrative of the Loss of Captain Grant of the Brig Britannia and '
            'of the Adventures of His Children and Friends in His Discovery and Rescue',
            'authors': [{
                'name': 'Verne, Jules',
                'birth_year': 1828,
                'death_year': 1905
            }],
            'languages': ['en'],
            'download_count':
            161,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            27175,
            'title':
            "The Bad Child's Book of Beasts",
            'authors': [{
                'name': 'Belloc, Hilaire',
                'birth_year': 1870,
                'death_year': 1953
            }],
            'languages': ['en'],
            'download_count':
            158,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            30272,
            'title':
            'Very Short Stories and Verses For Children',
            'authors': [{
                'name': 'Clifford, W. K., Mrs.',
                'birth_year': None,
                'death_year': 1929
            }],
            'languages': ['en'],
            'download_count':
            158,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            62928,
            'title':
            'Child Whispers',
            'authors': [{
                'name': 'Blyton, Enid',
                'birth_year': 1897,
                'death_year': 1968
            }],
            'languages': ['en'],
            'download_count':
            157,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            29259,
            'title':
            'The Child and the Curriculum',
            'authors': [{
                'name': 'Dewey, John',
                'birth_year': 1859,
                'death_year': 1952
            }],
            'languages': ['en'],
            'download_count':
            154,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            68080,
            'title':
            'Incidents of childhood',
            'authors': [{
                'name': 'Anonymous',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            153,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            26990,
            'title':
            "Holy in Christ: Thoughts on the Calling of God's Children to be Holy as He is Holy",
            'authors': [{
                'name': 'Murray, Andrew',
                'birth_year': 1828,
                'death_year': 1917
            }],
            'languages': ['en'],
            'download_count':
            149,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            20817,
            'title':
            'The Mother and Her Child',
            'authors': [{
                'name': 'Sadler, William S. (William Samuel)',
                'birth_year': 1875,
                'death_year': 1969
            }, {
                'name': 'Sadler, Lena K. (Lena Kellogg)',
                'birth_year': 1875,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            146,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            14411,
            'title':
            "The Children's Six Minutes",
            'authors': [{
                'name': 'Wright, Bruce S. (Bruce Simpson)',
                'birth_year': 1879,
                'death_year': 1942
            }],
            'languages': ['en'],
            'download_count':
            143,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            43984,
            'title':
            'Chaucer for Children: A Golden Key',
            'authors': [{
                'name': 'Chaucer, Geoffrey',
                'birth_year': 1342,
                'death_year': 1400
            }],
            'languages': ['en'],
            'download_count':
            143,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            2841,
            'title':
            'The Ivory Child',
            'authors': [{
                'name': 'Haggard, H. Rider (Henry Rider)',
                'birth_year': 1856,
                'death_year': 1925
            }],
            'languages': ['en'],
            'download_count':
            140,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            10541,
            'title':
            "Children's Classics in Dramatic Form, A Reader for the Fourth Grade",
            'authors': [{
                'name': 'Stevenson, Augusta',
                'birth_year': 1869,
                'death_year': 1976
            }],
            'languages': ['en'],
            'download_count':
            140,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            20015,
            'title':
            'The Child of Pleasure',
            'authors': [{
                'name': "D'Annunzio, Gabriele",
                'birth_year': 1863,
                'death_year': 1938
            }],
            'languages': ['en'],
            'download_count':
            140,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id':
            17162,
            'title':
            'Mother Stories from the Old Testament: A Book of the Best Stories from the Old Testament that Mothers '
            'can tell their Children',
            'authors': [{
                'name': 'Anonymous',
                'birth_year': None,
                'death_year': None
            }],
            'languages': ['en'],
            'download_count':
            139,
            'reviews':
            None,
            'average_rating':
            None
        }, {
            'id': 16537,
            'title':
            'Myths That Every Child Should Know: A Selection Of The Classic Myths Of All Times For Young People',
            'authors': [],
            'languages': ['en'],
            'download_count': 138,
            'reviews': None,
            'average_rating': None
        }]
    }


@patch('requests.get')
def test_get_books_title_and_page_not_found(requests_mock):
    fail_response = Mock()
    fail_response.status_code = 404
    fail_response.raise_for_status.side_effect = HTTPError(
        '404 Client Error: Not Found for url: '
        'https://gutendex.com/books/?page=2&search=colors')

    requests_mock.return_value = fail_response
    response = client.get('/books?page=2&title=colors')
    assert response.status_code == 500
    assert response.json() == {
        "message":
        "404 Client Error: Not Found for url: https://gutendex.com/books/?page=2&search=colors"
    }


def test_get_books_page_not_valid():
    response = client.get('/books?page=x')
    assert response.status_code == 422
    assert response.json() == {
        "detail": [{
            "loc": ["query", "page"],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }]
    }


@patch('requests.get')
def test_get_book_by_id_and_title_not_found(requests_mock):
    fail_response = Mock()
    fail_response.status_code = 200
    fail_response.json.return_value = book_not_found()

    requests_mock.return_value = fail_response
    response = client.get('/books?book_id=800000')
    assert response.status_code == 404
    assert response.json() == {'message': 'Book not found'}
