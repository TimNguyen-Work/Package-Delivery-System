# Implement a Hash Map class
# Citing source: zyBooks: Figure 7.8.2: Hash table using chaining - W-1_ChainingHashTable_zyBooks_Key-Value_CSV.py
class Hash_Table:

    def __init__(self, capacity_limit=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(capacity_limit):
            self.table.append([])

    # Inserts a new item into the hash table using uid_key and user_input_value
    def add_uid_key(self, uid_key, user_input_value):  # does both insert and update
        # get the bucket list where this item will go.
        key_number = hash(uid_key) % len(self.table)
        key_number_list = self.table[key_number]

        # update key if it is already in the bucket
        for any_key_value in key_number_list:
            # print (key_value)
            if any_key_value[0] == uid_key:
                any_key_value[1] = user_input_value
                return True

        # if not, insert the item to the end of the bucket list.
        uid_key_value = [uid_key, user_input_value]
        key_number_list.append(uid_key_value)
        return True

    # Find items in hash table using uid_key
    def find_uid_key(self, uid_key):
        # get the bucket list where this key would be.
        key_number = hash(uid_key) % len(self.table)
        key_number_list = self.table[key_number]
        # print(bucket_list)

        # search for the key in the bucket list
        for any_key_value in key_number_list:
            # print (key_value)
            if any_key_value[0] == uid_key:
                return any_key_value[1]  # value
        return None

    # Remove an item from the hash table

    def delete_uid_key(self, uid_key):
        key_number = hash(uid_key) % len(self.table)
        key_number_list = self.table[key_number]

        # Remove the item from the hash table if the key is found
        for any_key_value in key_number_list:
            if any_key_value[0] == uid_key:
                key_number_list.remove([any_key_value[0], any_key_value[1]])


