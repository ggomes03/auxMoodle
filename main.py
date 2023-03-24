from tkinter import filedialog
from file import Janela
import csv 

path = filedialog.askopenfilename()

if __name__ == '__main__':
  janela = Janela()
  janela.mainloop()


with open(path, encoding='cp1252',errors='ignore') as f:
  leitor = csv.reader(f)
  csvData = list(leitor)

def findIndex(header, attfind):
  indexName = -1
  for i in range(0, len(header[0])):
      if(header[0][i].lower() == attfind.lower()):
          indexName = i
  return indexName

def separateName(nomes):
  indexName = findIndex(nomes,"nome")
  separateNames = {
                    'firstname' :[],
                    'lastname'  :[]
  }

  if indexName == -1:
    print('o indíce do atributo nome não é aceitável')
  else:
    for i in range(1, len(nomes)):
      nameAux = nomes[i][indexName].split(' ')
      lastnameaux = " ".join(nameAux[1:len(nameAux)]);

      separateNames['firstname'].append(nameAux[0])
      separateNames['lastname'].append(lastnameaux)

  return separateNames


def objFinaltoWrite(dados):
  names = separateName(dados)
  matIndex = findIndex(dados,'matricula')
  emailIndex = findIndex(dados,'email')

  objFinal = []
  objAux = ['username','firstname','lastname','email','password']
  objFinal.append(objAux)
  for i in range(1,len(dados)):
    objAux = [dados[i][matIndex], names['firstname'][i-1], names['lastname'][i-1], dados[i][emailIndex],dados[i][matIndex]]
    objFinal.append(objAux)
  return objFinal



relatorio = objFinaltoWrite(csvData)

with open(janela.nome_arquivo, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for c in range(0, len(relatorio)):
    writer.writerow(relatorio[c])