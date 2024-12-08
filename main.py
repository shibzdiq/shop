from crud import insert_document, delete_document, update_document, display_all_documents
from db import orders_collection, menu_collection, reviews_collection

def main():
    while True:
        print("\n1. Вставка замовлення")
        print("2. Видалення замовлення")
        print("3. Оновлення замовлення")
        print("4. Пошук замовлення")
        print("5. Вставка елементу меню")
        print("6. Видалення елементу меню")
        print("7. Оновлення елементу меню")
        print("8. Пошук елементу меню")
        print("9. Вставка відгуку")
        print("10. Видалення відгуку")
        print("11. Оновлення відгуку")
        print("12. Пошук відгуків")
        print("13. Вивід всіх замовлень")
        print("14. Вивід всіх елементів меню")
        print("15. Вивід всіх відгуків")
        print("0. Вихід")
        
        choice = input("Виберіть дію: ")

        if choice == '1':
            order = {
                "customer_name": input("Ім'я клієнта: "),
                "order_details": input("Деталі замовлення: "),
                "total_price": float(input("Загальна ціна: "))
            }
            insert_document(orders_collection, order)
        elif choice == '2':
            order_id = input("ID замовлення для видалення: ")
            delete_document(orders_collection, {"_id": order_id})
        elif choice == '3':
            order_id = input("ID замовлення для оновлення: ")
            new_details = input("Нові деталі замовлення: ")
            update_document(orders_collection, {"_id": order_id}, {"order_details": new_details})
        elif choice == '4':
            order_id = input("ID замовлення для пошуку: ")
            orders = find_documents(orders_collection, {"_id": order_id})
            for order in orders:
                print(order)
        elif choice == '5':
            menu_item = {
                "name": input("Назва страви: "),
                "description": input("Опис: "),
                "price": float(input("Ціна: "))
            }
            insert_document(menu_collection, menu_item)
        elif choice == '6':
            menu_item_id = input("ID страви для видалення: ")
            delete_document(menu_collection, {"_id": menu_item_id})
        elif choice == '7':
            menu_item_id = input("ID страви для оновлення: ")
            new_price = float(input("Нова ціна: "))
            update_document(menu_collection, {"_id": menu_item_id}, {"price": new_price})
        elif choice == '8':
            menu_item_id = input("ID страви для пошуку: ")
            menu_items = find_documents(menu_collection, {"_id": menu_item_id})
            for item in menu_items:
                print(item)
        elif choice == '9':
            review = {
                "customer_name": input("Ім'я клієнта: "),
                "review": input("Відгук: "),
                "rating": int(input("Оцінка (1-5): "))
            }
            insert_document(reviews_collection, review)
        elif choice == '10':
            review_id = input("ID відгуку для видалення: ")
            delete_document(reviews_collection, {"_id": review_id})
        elif choice == '11':
            review_id = input("ID відгуку для оновлення: ")
            new_rating = int(input("Нова оцінка (1-5): "))
            update_document(reviews_collection, {"_id": review_id}, {"rating": new_rating})
        elif choice == '12':
            review_id = input("ID відгуку для пошуку: ")
            reviews = find_documents(reviews_collection, {"_id": review_id})
            for review in reviews:
                print(review)
        elif choice == '13':
            print("\nВсі замовлення:")
            display_all_documents(orders_collection)
        elif choice == '14':
            print("\nВсі елементи меню:")
            display_all_documents(menu_collection)
        elif choice == '15':
            print("\nВсі відгуки:")
            display_all_documents(reviews_collection)
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()
