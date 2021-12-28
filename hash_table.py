class Node:
	#def __init__(self,data=None,next_node=None):
	def __init__(self,key=None,value=None,next_node=None):
		#self.data=data,
		self.key = key
		self.value = value
		self.next_node =next_node

# class Data:
# 	def __init__(self,key,value):
# 		self.key = key
# 		self.value = value

class HashTable:
	def __init__(self,table_size):
		self.table_size = table_size
		self.hash_table = [None] * table_size


	def custom_hash(self,key):
		hash_value = 0
		for i in key:
			hash_value += ord(i)
			hash_value = (hash_value * ord(i)) % self.table_size
		return hash_value

	def add_key_value(self,key,value):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is None:
			#self.hash_table[hashed_key] = Node(Data(key,value), None)
			self.hash_table[hashed_key] = Node(key,value, None)
		else:
			node = self.hash_table[hashed_key]
			while node.next_node:
				node = node.next_node
			#node.next_node = Node(Data(key,value),None)
			node.next_node = Node(key,value,None)

	def get_value(self,key):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is not None:
			node = self.hash_table[hashed_key]
			if node.next_node is None:
				#return node.data.value
				return node.value
			while node.next_node:
				if key == node.key:
					#return node.data.value
					return node.value
				node = node.next_node

			#if key == node.data.key:
			if key == node.key:
				return node.value

				#return node.data.value

		return None

	def print_table(self):
		print("{")
		for i, val in enumerate(self.hash_table):

			if val is not None:
				llist_string = ""
				node = val
				
				if node.next_node:
					while node.next_node:
						#llist_string += (str(node.data.key) + " : " + str(node.data.value) + " --> ")
						llist_string += (str(node.key) + " : " + str(node.value) + " --> ")
						node = node.next_node

					#llist_string += (str(node.data.key) + " : " + str(node.data.value) + " -->  None")
					llist_string += (str(node.key) + " : " + str(node.value) + " -->  None")
					print(f"     [{i}] {llist_string}")
				else:
					print(f"     [{i}] {val.key} : {val.value}")
					#print(f"     [{i}] {val.data.key} : {val.data.value}")
			else:
				print(f"     [{i}] {val}")

		print("}")

# ht = HashTable(2)
# ht.add_key_value('hello','there')
# ht.add_key_value('nla','hhd')
# ht.print_table()