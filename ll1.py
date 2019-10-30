class Node:
	def __init__(self, data):
		self.item = data
		self.ref = None


class LinkedList:
	def __init__(self):
		self.start_node = None

	def traverse_list(self):
		if self.start_node is None:
			print("list has no element")
			return
		else:
			n = self.start_node
			while n is not None:
				print(n.item, " ")
				n = n.ref

	def insert_at_start(self, data):
		new_node = Node(data)
		new_node.ref = self.start_node
		self.start_node = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.start_node is None:
			self.start_node = new_node
			return
		n = self.start_node
		while n.ref is not None:
			n = n.ref
		n.ref = new_node

	def insert_after_item(self, x, data):
		n = self.start_node
		print(n.ref)
		while n is not None:
			if n.item == x:
				break
			n = n.ref
		if n is None:
			print("item not in the list")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def insert_before_item(self, x, data):
		if self.start_node is None:
			print("List has no element")
			return

		if x == self.start_node.item:
			new_node = Node(data)
			new_node.ref = self.start_node
			self.start_node = new_node
			return

		n = self.start_node
		print(n.ref)
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref

		if n.ref is None:
			print("item not in the list")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def insert_at_index (self, index, data):
		if index == 1:
			new_node = Node(data)
			new_node.ref = self.start_node
			self.start_node = new_node
		i = 1
		n = self.start_node
		while i < index-1 and n is not None:
			n = n.ref
			i = i+1
		if n is None:
			print("Index out of bound")
		else: 
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def get_count(self):
		if self.start_node is None:
			return 0
		n = self.start_node
		count = 0
		while n is not None:
			count = count + 1
			n = n.ref
		return count

	def search_item(self, x):
		if self.start_node is None:
			print("list has no element")
			return

		n = self.start_node
		while n is not None:
			if n.item == x:
				print("item found")
				return True
			n = n.ref
		print("item not found")
		return False

	def make_new_list(self):
		nums = int(input("how many nodes do you want to create: "))
		if nums == 0:
			return
		for i in range(nums):
			value = int(input("enter the value for the node: "))
			self.insert_at_end(value)

	def delete_at_start(self):
		if self.start_node is None:
			print("the list has no element to delete")
			return
		self.start_node = self.start_node.ref

	def delete_at_end(self):
		if self.start_node is None:
			print("the list has no element to delete")
			return

		n = self.start_node
		while n.ref.ref is not None:
			n = n.ref
		n.ref = None

	def delete_element_by_value(self, x):
		if self.start_node is None:
			print("the list has no element to delete")
			return

		if self.start_node.item == x:
			self.start_node = self.start_node.ref
			return

		n = self.start_node
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref

		if n.ref is None:
			print("item not found in the list")

		else:
			n.ref = n.ref.ref

	def reverse_linkedlist(self):
		prev = None
		n = self.start_node
		while n is not None:
			next = n.ref
			n.ref = prev
			prev = n
			n = next
		self.start_node = prev

	def bub_sort_datachange(self):
		end = None
		while end != self.start_node:
			p = self.start_node
			while p.ref != end:
				q = p.ref
				if p.item >q.item:
					p.item, q.item = q.item, p.item
				p = p.ref
			end = p

	def bub_sort_linkchange(self):
		end = None
		while end != self.start_node:
			r = p = self.start_node
			while p.ref != end:
				q = p.ref
				if p.item > q.item:
					p.ref = q.ref
					q.ref = p
					if p != self.start_node:
						r.ref = q
					else:
						self.start_node = q
					p,q = q,p
				r = p
				p = p.ref
			end = p

	def merge_helper(self, list2):
		merge_list = LinkedList()
		merge_list.start_node = self.merge_by_newlist(self.start_node, list2.start_node)
		return merge_list

	def merge_by_newlist(self, p, q):
		if p.item <= q.item:
			startNode = Node(p.item)
			p = p.ref
		else:
			startNode = Node(q.item)
			q = q.ref

		em = startNode

		while p is not None and q is not None:
			if p.item <= q.item:
				em.ref = Node(p.item)
				p = p.ref
			else:
				em.ref = Node(q.item)
				q = q.ref
			em = em.ref

		while p is not None:
			em.ref = Node(p.item)
			p = p.ref
			em = em.ref

		while q is not None:
			em.ref = Node(q.item)
			q = q.ref
			em = em.ref

		return startNode

	def merge_helper2(self, list2):
		merge_list = LinkedList()
		merge_list.start_node = self.merge_by_linkChange(self.start_node, list2.start_node)
		return merge_list

	def merge_by_linkChange(self, p, q):
		if p.item <= q.item:
			startNode = Node(p.item)
			p = p.ref
		else:
			startNode = Node(q.item)
			q = q.ref

		em = startNode

		while p is not None and q is not None:
			if p.item <= q.item:
				em.ref = Node(p.item)
				em = em.ref
				p = p.ref
			else:
				em.ref = Node(q.item)
				em = em.ref
				q = q.ref

		if p is None:
			em.ref = q
		else:
			em.ref = p

		return startNode

