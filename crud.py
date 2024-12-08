from db import orders_collection, menu_collection, reviews_collection
from tabulate import tabulate

# Вставка документа
def insert_document(collection, document):
    collection.insert_one(document)

# Видалення документа
def delete_document(collection, query):
    collection.delete_one(query)

# Оновлення документа
def update_document(collection, query, new_values):
    collection.update_one(query, {"$set": new_values})

# Пошук документа
def find_documents(collection, query):
    return collection.find(query)

# Відображення документів у вигляді таблиці
def display_all_documents(collection):
    documents = find_documents(collection, {})
    data = []
    headers = ["_id"] + list(documents[0].keys())[1:]
    for document in documents:
        data.append([str(document["_id"])] + list(document.values())[1:])
    print(tabulate(data, headers, tablefmt="pretty"))
