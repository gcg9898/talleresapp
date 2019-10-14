from bs4 import BeautifulSoup
import requests 



pag = 0
URL1 = "https://www.paginasamarillas.es/search/talleres-mecanicos/all-ma/all-pr/all-is/all-ci/all-ba/all-pu/all-nc/" 
URL2 = "?what=talleres+mecanicos&qc=true"
status_code = 200
while(status_code == 200):
    pag += 1
    req = requests.get(URL1 + str(pag) + URL2)

    # Comprobamos que la peticin nos devuelve un Status Code = 200
    status_code = req.status_code

    if status_code == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los divs donde estn las entradas
        main = html.find_all('div', {'itemtype': 'http://schema.org/LocalBusiness'})

        # Recorremos todas las entradas para extraer el ttulo, autor y fecha
        for i, entrada in enumerate(main):
            # Con el mtodo "getText()" no nos devuelve el HTML
            #titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
            # Sino llamamos al mtodo "getText()" nos devuelve tambin el HTML
            #autor = entrada.find('span', {'class': 'autor'})
            #fecha = entrada.find('span', {'class': 'fecha'}).getText()
            titulo =calle =codigPostal =ciudad = enlace ="no tiene"
            if(entrada.find('span', {'itemprop' :'name'})):
                titulo = entrada.find('span', {'itemprop' :'name'}).getText()

            # Imprimo el Ttulo, Autor y Fecha de las entradas
            if(entrada.find('span', {'itemprop' :'streetAddress'})):
                calle = entrada.find('span', {'itemprop' :'streetAddress'}).getText()
            if(entrada.find('span', {'itemprop' :'postalCode'})):
                codigPostal = entrada.find('span', {'itemprop' :'postalCode'}).getText()
            if(entrada.find('span', {'itemprop' :'addressLocality'})):
                ciudad = entrada.find('span', {'itemprop' :'addressLocality'}).getText()
            if(entrada.find('a', {'data-omniclick' :'name'})):
                enlace = entrada.find('a').get('href')
                sub = requests.get(enlace)
                htmlSub = BeautifulSoup(sub.text, "html.parser")
                telefonos =[]
                descripcion = ""
                if(htmlSub.find('span', {'itemprop' :'telephone'})):
                    tlf = htmlSub.find_all('span', {'itemprop' :'telephone'})
                    for t in tlf:
                        print(t.getText())
                        telefonos.append(t.getText())
                        
            print(i + ((pag -1)*29))
            print(titulo)
            print(codigPostal)
            print(ciudad)
            print(enlace)
            print(telefonos)
            print("\n")

    else:
        print(str(status_code))