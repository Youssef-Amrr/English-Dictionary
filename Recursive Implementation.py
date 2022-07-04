#Initiates a node by giving the key value
class Node():
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'RED'

#Initiates an empty tree with NIL node having key=None and root=NIL
class RedBlackTree():
    def __init__(self):
        self.TNIL=Node()
        self.TNIL.color = 'BLACK'
        self.TNIL.left = None
        self.TNIL.right = None
        self.root = self.TNIL
        self.tempParent=self.TNIL
        self.insertedNode=self.TNIL

    def rotateLeft(self,node):
        y=node.right
        node.right=y.left
        if y.left!=self.TNIL:
            y.left.parent=node
        y.parent=node.parent
        if node.parent==self.TNIL:
            self.root=y
        elif node==node.parent.left:
            node.parent.left=y
        else:
            node.parent.right=y
        y.left=node
        node.parent=y

    def rotateRight(self,node):
        y=node.left
        node.left=y.right
        if y.right!=self.TNIL:
            y.right.parent=node
        y.parent=node.parent
        if node.parent==self.TNIL:
            self.root=y
        elif node==node.parent.right:
            node.parent.right=y
        else:
            node.parent.left=y
        y.right=node
        node.parent=y

    def recolor(self,node):
        node.parent.color='BLACK'
        if node.parent.parent.right!= self.TNIL:
            node.parent.parent.right.color='BLACK'
        if node.parent.parent.left!= self.TNIL:
            node.parent.parent.left.color='BLACK'
        node.parent.parent.color='RED'
        self.insertionFixup(node.parent.parent)

    def insertionFixup(self,node): 
        if node.parent==self.TNIL: #Color the root black
            node.color='BLACK'
            return
        if node.parent.color== 'BLACK': #Parent is already black, do nothing
            return
        elif node.parent.parent.left.color=='RED' and node.parent.parent.right.color=='RED': #Uncle Red
            self.recolor(node)
        elif node.parent.key>node.key and node.parent.parent.right.color=='BLACK': #Left left case
            node.parent.color='BLACK'
            node.parent.parent.color='RED'
            self.rotateRight(node.parent.parent)
        elif node.parent.key<node.key and node.parent.parent.right.color=='BLACK': #Left right case
            self.rotateLeft(node.parent)
            node.color='BLACK'
            node.parent.color='RED'
            self.rotateRight(node.parent)
        elif node.parent.key < node.key and node.parent.parent.left.color=='BLACK': #Right right case
            node.parent.color='BLACK'
            node.parent.parent.color='RED'
            self.rotateLeft(node.parent.parent)
        elif node.parent.key>node.key and node.parent.parent.left.color=='BLACK': #Right left case
            self.rotateRight(node.parent)
            node.color='BLACK'
            node.parent.color='RED'
            self.rotateLeft(node.parent)
    
    def insertNode(self,node,key):
        if node==self.TNIL:
            node=Node(key.lower())
            node.left=self.TNIL
            node.right=self.TNIL
            node.parent=self.tempParent
            self.insertedNode=node
            return node
        elif key.lower()>node.key.lower():
            self.tempParent=node
            node.right=self.insertNode(node.right,key)
        elif key.lower()<node.key.lower():
            self.tempParent=node
            node.left=self.insertNode(node.left,key)
        else:
            print("Error! Word already exists in dictionary!")
        return node
        
    def searchNode(self,node,key):
        if node == self.TNIL:  
            print("The word '",key,"' could not be found!")
        elif node.key==key.lower():
            print("The word '",key,"' was found successfully!")
        elif key.lower()>node.key:
            self.searchNode(node.right,key)
        else:
            self.searchNode(node.left,key)
        
    def printHeight(self,node):
        if node==self.TNIL:
            return 0
        return 1+max(self.printHeight(node.left),self.printHeight(node.right))

    def printSize(self,node):
        if node==self.TNIL:   
            return 0
        return 1+self.printSize(node.left)+self.printSize(node.right)

    def inorderPrint(self,node):
        if node!=self.TNIL:
            self.inorderPrint(node.left)
            print(node.key)
            self.inorderPrint(node.right)

    def readFileToRBTree(self):
        try:
            f=open('EN-US-Dictionary.txt','r')
        except:
            print("ERROR! Dictionary cannot be found!")
            return
        for line in f:
            dictionaryWord=line
            if dictionaryWord.endswith('\n'):
                dictionaryWord = dictionaryWord[:-1]
            self.root=self.insertNode(self.root,dictionaryWord)
            self.insertionFixup(self.insertedNode)
        f.close()
        print("\n\nDictionary loaded successfully to tree!")


            
def printMenu():
    print("----------------------------------------")
    print("            DICTIONARY MENU             ")
    print("----------------------------------------")
    print("  1.  Search for a word\n  2.  Insert a word\n  3.  Print dictionary size \n  4.  Print dictionary height\n  5.  To exit\n\n")
    x = input("Your choice: ")
    return x

def main():
   booleanFlag = True
   myTree=RedBlackTree()
   myTree.readFileToRBTree()
   while booleanFlag == True:
       x=printMenu()
       if x=='1':
           str=input("\nEnter a word to search for: ")
           myTree.searchNode(myTree.root,str)
       elif x=='2':
           str=input("\nEnter a word to insert in dictionary: ")
           node=myTree.insertedNode
           myTree.root=myTree.insertNode(myTree.root,str)
           if myTree.insertedNode != node:  #Successful insertion
               myTree.insertionFixup(myTree.insertedNode)
               print("Word added successfully to dictionary!")
               print("Dictionary size: ", myTree.printSize(myTree.root)," words")
               print("Dictionary height: ", myTree.printHeight(myTree.root)," words on the longest path\n\n")
       elif x=='3':
            print("\nDictionary size: ", myTree.printSize(myTree.root)," words")
       elif x=='4':
            print("\nDictionary height: ", myTree.printHeight(myTree.root)," words on the longest path")
       elif x=='5':
           print("              THANK YOU               ")
           booleanFlag=False
       else:
           print("INVALID INPUT! TRY AGAIN!")

       
main()
