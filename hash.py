print("33_ITB_Ekta singh")
def linear_probing(hash_table, key):
    hash_value = key % 10

    if hash_table[hash_value] is None:
        hash_table[hash_value] = key
    else:
        for i in range(hash_value + 1, len(hash_table)):
            if hash_table[i] is None:
                hash_table[i] = key
                break


hash_table = [None] * 10

linear_probing(hash_table, 25)
linear_probing(hash_table, 35)
linear_probing(hash_table, 45)
linear_probing(hash_table, 15)
linear_probing(hash_table, 55)
linear_probing(hash_table, 50)
linear_probing(hash_table, 30)

print(hash_table)  