import json

address_book = {
    "Tom": {
        "name": "Thomas",
        "address": "10 Downing Street",
        "phone": 7798145632
    },
    "Jerry": {
        "name": "Jerry",
        "address": "10 Downing Street",
        "phone": 7798145633
    }
}

if __name__ == "__main__":
    strr = json.dumps(address_book)
    with open("C://Users//Sougata Ghosh//Documents//bliss//PyCharm projects//HelloWorld//data//"
              "address_book.txt", "w") as f:
        f.write(strr)
    data = open("C://Users//Sougata Ghosh//Documents//bliss//PyCharm projects//HelloWorld//data//"
                "address_book.txt", "r").read()
    print(data)
    book = json.loads(data)
    print(book)
    print(type(data), type(book))
    print(book["Tom"]["phone"])
    for key in book:
        print(book[key])