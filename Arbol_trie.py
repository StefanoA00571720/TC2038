class TrieNode:
    """
        Class that is used to represent a Trie node. 
    """    
    _children = {}          # Dictionary of children nodes.
       
    _end_of_word = False    # This flag indicates whether the node is the end of a word.
    
    def __init__(self):
        """ 
            This constructor initializes a node. 
        """        
        self._children = {}
        self._end_of_word = False





class Trie:
    _root = [] #Nodo raiz

    def __init__(self, directed:bool = False): #Inicia el arbol
       
        self._root = TrieNode()

    def insert(self, word:str) -> None:

        current = self._root
        
        for c in word:
            if c not in current._children:
                current._children[c] = TrieNode()
                
            current = current._children[c]
        current._end_of_word = True
    
    def search(self, word:str) -> bool:
        """ 
            This method searches a word in the Trie. 
            
            param word: The word to search in the Trie.
        """ 
        current = self._root
        
        for c in word:
            if c not in current._children:
                return False
                
            current = current._children[c]
        return current._end_of_word
    
    def starts_width(self, prefix:str) -> bool:
        """ 
            This method searches a word in the Trie. 
            
            param prefix: The prefix to search in the Trie.
        """ 
        current = self._root
        
        for c in prefix:
            if c not in current._children:
                return False
                
            current = current._children[c]
        return True
    
trie = Trie()

with open("PGD.txt", "r") as novela:
    for linea in novela:
        palabras = linea.split()
        for palabra in palabras:
            trie.insert(palabra)

print("Search : Dracula", trie.search("Dracula"))
print("Search : Doctor", trie.search("Doctor"))
print("Search : doctor", trie.search("doctor"))
print("Search : werewolf", trie.search("werewolf"))
print("Search : Moon", trie.search("moon"))
print("Search : Stars", trie.search("stars"))
print("Search : Mountain", trie.search("mountain"))
print("Search : Crypt", trie.search("crypt"))
print("Search : Supernatural", trie.search("supernatural"))
print("Search : Transylvania", trie.search("Transylvania"))
print("Search : Coffin", trie.search("coffin"))
print("Search : Mysterious", trie.search("mysterious"))
print("Search : Tenebrous", trie.search("tenebrous"))
print("Search : Gothic", trie.search("gothic"))
print("Search : Lurking", trie.search("lurking"))
print("Search : Undead", trie.search("undead"))
print("Search : Crypt", trie.search("crypt"))
print("Search : Bats", trie.search("Bats"))
print("Search : Bats", trie.search("bats"))
print("Search : Elixir", trie.search("elixir"))

print("Starts with : Dracula", trie.starts_width("Dracula"))
print("Starts with : Doctor", trie.starts_width("Dr"))
print("Starts with : doctor", trie.starts_width("doctor"))
print("Starts with : werewolf", trie.starts_width("werewolf"))
print("Starts with : Moon", trie.starts_width("Moon"))
print("Starts with : Stars", trie.starts_width("Stars"))
print("Starts with : Mountain", trie.starts_width("Mountain"))
print("Starts with : Crypt", trie.starts_width("Crypt"))
print("Starts with : Supernatural", trie.starts_width("Supernatural"))
print("Starts with : Transylvania", trie.starts_width("Transylvania"))
print("Starts with : Coffin", trie.starts_width("Coffin"))
print("Starts with : Mysterious", trie.starts_width("Mysterious"))
print("Starts with : Tenebrous", trie.starts_width("Tenebrous"))
print("Starts with : Gothic", trie.starts_width("Gothic"))
print("Starts with : Lurking", trie.starts_width("Lurking"))
print("Starts with : Undead", trie.starts_width("Undead"))
print("Starts with : Crypt", trie.starts_width("Crypt"))
print("Starts with : Bats", trie.starts_width("Bats"))
print("Starts with : Bats", trie.starts_width("bats"))
print("Starts with : Elixir", trie.starts_width("elixir"))
