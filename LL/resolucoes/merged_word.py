def mergeAlternately(self, word1: str, word2: str) -> str:
    
        merged = []

        for a, b in zip(word1, word2):
            # o for vai parar quando word1 ou word2 acabar
            # zip vai pegar os dois iteraveis e colocar em uma tupla
            # exemplo: word1 = "abc" e word2 = "def" -> [('a', 'd'), ('b', 'e'), ('c', 'f')]
            
            merged.append(a + b)
    
        # o merged abaixo vai pegar o restante de word1 ou word2 e colocar no final
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)

def init():

    word1 = "abc"
    word2 = "defg"
    print(mergeAlternately(word1, word2))
    # Saída: "adbecfg"

def main():
    
    init()
    # print(mergeAlternately("abc", "defg"))
    # Saída: "adbecfg"