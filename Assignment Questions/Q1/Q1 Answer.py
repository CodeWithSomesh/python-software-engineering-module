import os

class Smartphone:
    # Constructor
    # Initializing phones, all nodes originally have all these attributes
    def __init__(self, productCode, brand, model, sellingPrice, color,  quantityOnHAnd, serialNumber):
        self.productCode = productCode
        self.brand = brand
        self.model = model
        self.sellingPrice = sellingPrice
        self.color = color
        self.quantityOnHAnd = quantityOnHAnd
        self.serialNumber = serialNumber

    # def __str__(self):
    #     return (f"ID: {self.product_id}, Brand: {self.brand}, Model: {self.model}, "
    #             f"Price: ${self.price}, Quantity: {self.quantity}")

class BST_Node:
    # Constructor
    # Initializing nodes, all nodes originally have no left or right branch
    def __init__(self, phone):
        self.root = phone
        self.left = None
        self.right = None

class BST:
    # Constructor
    # Initializing BST Tree, BST trees originally are always empty with no Root Node
    def __init__(self):
        self.root = None

    def addChild(self, phone, node):
        # Checking to see whether there is already a Root Node
        if self.root is None:
            self.root = BST_Node(phone) # If no Root Node then make the first value Root Node
        else:
            # If got Root Node, but current product code is BIGGER than Root Node
            if phone.productCode > node.phone.productCode:
                # And if there is no RIGHT CHILD for this node, then make the current phone the RIGHT CHILD
                if node.right is None:
                    node.right = BST_Node(phone)
                # If not run this same method recursively until it becomes a RIGHT CHILD
                else:
                    self.addChild(phone, node.right)
            # If got Root Node, but current product code is SMALLER than Root Node
            elif phone.productCode < node.phone.productCode:
                # And if there is no LEFT CHILD for this node, then make the current phone the LEFT CHILD
                if node.left is None:
                    node.left = BST_Node(phone)
                # If not run this same method recursively until it becomes a LEFT CHILD
                else:
                    self.addChild(phone, node.left)
            else:
                return False # Add Print Statement print("Phone with this Product Code already exists.")


    # Using LVR to return an array of elements (phones)
    def inOrderTraversal(self, node):
        # Initialize empty array
        elements = []

        # Vist Left node first, then recursively find for the furthest left leaf node,
        # then add in the array
        if node.left:
            elements += self.inOrderTraversal(node.left)

        # After adding the left node value of the node, then add the root node value
        elements.append(node.phone)

        # Lastly add the right node recursively
        if node.right:
            elements += self.inOrderTraversal(node.right)

        # If array is empty then it means no product has been added in the system yet
        if len(elements) == 0:
            return None
        else:
            return elements

    def search(self, productCode, node):
        # If the BST is empty then return None
        if node is None:
            return None # Add Print Statement
        elif productCode == node.phone.productCode:
            return node.phone
        # If the current phone productCode is BIGGER than node's,
        # then run this same method recursively until the phone with given product code is found
        elif productCode > node.phone.productCode:
            self.search(productCode, node.right)
        # If the current phone productCode is SMALLER than node's,
        # then run this same method recursively until the phone with given product code is found
        elif productCode < node.phone.productCode:
            self.search(productCode, node.left)
        else:
            return False # Add Print Statement

class StockManagementSystem:

    def __init__(self):



if __name__ == "__main__":
    # system = StockManagementSystem()
    # system.menu()