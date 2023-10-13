def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices 
# Example list of products
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

# Target product to search for
target_product = "Apple"

# Perform linear search and get indices of all occurrences
result_indices = linear_search_product(products, target_product)

# Check if the product was found and print the indices
if result_indices:
    print(f"{target_product} found at indices: {result_indices}")
else:
    print(f"{target_product} not found in the list.")
