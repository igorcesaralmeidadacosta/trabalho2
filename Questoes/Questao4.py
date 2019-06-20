class Carro():

    def __init__ (self, csm):
        self.csm = csm
        self.cmb = 0

    def andar(self, km):
        gst = (km/self.csm)
        self.cmb = self.cmb - gst

    def obterGasolina(self):
        return self.cmb

    def obterGasolinaPrint(self):
        print(self.cmb)

    def adicionarGasolina(self,add):
        self.cmb = self.cmb + add

def main():

   meuFusca = Carro(15)
   meuFusca.adicionarGasolina(20)
   meuFusca.andar(100)
   meuFusca.obterGasolinaPrint()
   print(meuFusca.obterGasolina())
   
      
main()
