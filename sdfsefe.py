class NoArvore():
    ## Atributos necessários
    def _init_(self,codigo,letra):
        self.esquerda = None
        self.direita = None
        self.codigo = codigo
        self.letra = letra
    ## Método para inserir na árvore
    def inserir(self,codigo,letra):
        if self.codigo:
            if codigo < self.codigo:
                if self.esquerda is None:
                    self.esquerda = NoArvore(codigo,letra)
                else:
                    self.esquerda.inserir(codigo,letra)
            elif codigo > self.codigo:
                if self.direita is None:
                    self.direita = NoArvore(codigo,letra)
                else:
                    self.direita.inserir(codigo,letra)
        else:
            self.codigo = codigo
            self.letra = letra

    def obterFrase(self,listacod):
        if listacod < self.listacod:
            return self.left.obterCaractere(listacod)
        elif listacod > self.listacod:
            return self.right.obterCaractere(listacod)
        else:
            return self.letra

class Arvore():
  ### Atributos necessarios ###
    def insereFrase(self,listaCod,frase):
      for i in range(len(listaCod)):
            if i == 0:
              self.raiz = NoArvore(listaCod[i], frase[i])
            else:
              self.raiz.insereNo(listaCod[i],frase[i])
      def obtemFrase(self,listaCod):
    frase = ""
    for i in range(len(listaCod)):
            frase += self.raiz.obterCaractere(listaCod[i])
    return frase
  