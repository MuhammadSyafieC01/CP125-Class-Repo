def process_actions(catalog, actions):
    # TODO: Your code here

    for i in actions:
        if i[1] in catalog:

            print(f"{i[1]} Exist")

            if i[0] == "BORROW":
                print(f"Borrow {i[1]}")

                value = catalog.get(i[1]) - 1
                catalog[i] = value
                
            else:
                print(f"Return {i[1]}")
                value = catalog.get(i[1]) + 1
                catalog[i] = value


        else:
            print(f"{i[1]} Dont exist")
            

catalog = {
    "978-A": 2,
    "978-B": 0,
    "978-C": 1,
}
actions = [
    ("BORROW", "978-A"),
    ("BORROW", "978-A"),
    ("BORROW", "978-B"),
    ("RETURN", "978-B"),
    ("BORROW", "978-Z"),
]
print("\n")
process_actions(catalog, actions)
print("\n")
print(catalog)
print("\n")
print("\n")