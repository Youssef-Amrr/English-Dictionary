class Node:
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"
 
class RBtree:
    def __init__(self):
        self.tnil = Node()
        self.tnil.color = "BLACK"
        self.root = self.tnil
        self.size = 0

    def size(self):
        return self.size

    def get_height(self,node):
        if node == self.tnil:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1 
           
    def inorder(self, node):
        if node != self.tnil:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def search(self, node, key):
        if node == self.tnil:
            return False
        if node.key.lower() == key.lower():
            return True
        if key.lower() < node.key.lower():
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)    

    def rotate_left(self, node):
        if node == self.tnil or node.right == self.tnil:
            return 
        y = node.right
        node.right = y.left
        if y.left != self.tnil:
            y.left.parent = node
        else:
            node.right = self.tnil   
        if node.parent != self.tnil:
            y.parent = node.parent
            if node.parent.left == node:
                node.parent.left = y
            else:
                node.parent.right = y
        else:
            y.parent = self.tnil       
        y.left = node
        node.parent = y
        return 

    def rotate_right(self, node):
        if node == self.tnil or node.left == self.tnil:
            return    
        y = node.left
        node.left = y.right
        if y.right != self.tnil:
            y.right.parent = node
        else:
            node.left = self.tnil    
        if node.parent != self.tnil:
            y.parent = node.parent    
            if node.parent.left == node:
                node.parent.left = y
            else:
                node.parent.right = y
        else:
            y.parent = self.tnil       
        y.right = node
        node.parent = y
        return 

    def fix_insert(self, node):
        if node.parent.parent == self.tnil:
            return   
        while node.color == "RED" and node.parent.color == "RED":
            if node.parent.parent.left == node.parent: #Parent is a left child
                if node.parent.parent.right.color == "RED": #if uncle is RED --> CASE 1
                    y = node.parent.parent.right
                    node.parent.color = "BLACK"
                    y.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                        if node == node.parent.right: #if the node is a right child --> CASE 2
                            node = node.parent
                            self.rotate_left(node)
                        node.parent.color = "BLACK" # CASE 3
                        node.parent.parent.color = "RED"
                        self.rotate_right(node.parent.parent)
                        node = node.parent
            else: #Parent is a left child
                if node.parent.parent.left.color == "RED": #if uncle is RED --> CASE 1
                    y = node.parent.parent.left
                    if y.color == "RED":  
                        node.parent.color = "BLACK"
                        y.color = "BLACK"
                        node.parent.parent.color = "RED"
                        node = node.parent.parent
                else:    
                    if node == node.parent.left: #if the node is a right child --> CASE 2
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "BLACK" # CASE 3
                    node.parent.parent.color = "RED"
                    self.rotate_left(node.parent.parent)
                    node = node.parent       
            if node.parent == self.tnil:
                node.color = "BLACK"
                self.root = node
                return 
            else:
                if node.parent.color == "BLACK":
                    return 
        
    def insert(self, node, key):
        if node == self.tnil:
            self.root = Node(key)
            self.root.parent = self.tnil
            self.root.left = self.tnil
            self.root.right = self.tnil 
            self.size = 1   
            self.root.color = "BLACK" 
            return
        while True:
            if node.key.lower() == key.lower():
                print("ERROR: Word already in the dictioanary!")
                return
            if key.lower() < node.key.lower():
                if node.left != self.tnil:
                    node = node.left
                else:
                    node.left = Node(key)
                    node.left.left = self.tnil
                    node.left.right = self.tnil
                    node.left.parent = node
                    self.fix_insert(node.left)
                    break
            else:
                if node.right != self.tnil:
                    node = node.right
                else:
                    node.right = Node(key)
                    node.right.parent = node
                    node.right.left = self.tnil
                    node.right.right = self.tnil
                    self.fix_insert(node.right)
                    break 
        self.size += 1
        return

def load_dictionnary(filename, tree):
    with open(filename) as f:
        line = f.readline()
        while line:
            if line.endswith('\n'):
                line = line[:-1]
            tree.insert(tree.root, line)
            line = f.readline()    
    return tree

def main():
    t = RBtree()
    filename = 'EN-US-Dictionary.txt'
    t = load_dictionnary(filename, t)
    print("Dictionary successfully loaded into Red-Black tree.")
    while True:
        print("Choose by typing the option number:")
        print("1.Insert a new word.\n2.Search a word.\n3.Print the height of the tree.\n4.Print the size of the tree.")
        n = input("Choice: ")
        if n == "1":
            str = input("Enter the new word: ")
            t.insert(t.root, str)
            print(f"Size = {t.size}")
            print(f"Height = {t.get_height(t.root)}")              

        elif n == "2": 
            str = input("Enter the word you want to search: ")
            if t.search(t.root, str) == True:
                print("YES! The word is found.") 
            else:
                print("NO! The word is not found.")
        elif n == "3":
            print(f"Height = {t.get_height(t.root)}")              
        elif n == "4":
            print(f"Size = {t.size}")
        else:
            print("Invalid choice!")
        more = input("If you want to perform another operation press 'y', else press any button: ")
        if more != "y":
            break 
        
main()
