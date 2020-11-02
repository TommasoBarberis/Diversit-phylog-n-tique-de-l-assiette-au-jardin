from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from get_NCBI_taxonomy import get_taxid

# Pré requis : Téléchargez le binaire WebDriver pris en charge par votre navigateur et placez-le dans le repertoire du script.
# https://www.selenium.dev/documentation/fr/webdriver/driver_requirements/


# Driver au choix suivant votre navigateur ( le driver dans être placé dans le répertoire du script)

try :
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
except:
    driver = webdriver.Chrome(executable_path= "chromedriver.exe")

# Création de la liste ID à partir de la liste espèce donnée
liste_espece = ['Homo sapiens', 'primate']
liste_ID = list(get_taxid(liste_espece))
# Ouverture du navigateur sur le site suivant
driver.get("http://lifemap-ncbi.univ-lyon1.fr/")
# Ajout des éléments dans la zone de texte
inputElement = driver.find_element_by_id("textarea")
inputElement.send_keys(str(liste_ID))
# Détéction du bouton View et click effectué
View = driver.find_element_by_id("viewMulti")
View.click()




