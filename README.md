# DISCOVER YOUR CITY

Entdecke deine Stadt. Dieses Skript soll dafür sorgen, deine Stadt kennenzulernen. Es zieht nacheinander 
Bezirke + Sub-Bezirke, die man danach erkunden kann und schließt diese bei weiteren Ziehungen aus.
Bei jeder Auslosung wird ein Bezirk gezogen und der Gewinner bekommt daraufhin eine Mail mit dem
gezogenen Bezirk und den noch verbleibenden und zur Auswahl stehenden Sub-Bezirken. Mit einer Antwort per Mail des
Gewinners und dem gewählten Sub-Bezirks wird der ausgewählte Bezirk + Sub-Bezirk + Name in die history.txt 
geschrieben.

Eigenschaften:
- Berücksichtigt bereits ausgewählte Sub-Bezirke und schließt diese aus.
- Max. 2x hintereinander der selbe Gewinner
- Nicht hintereinander der selbe Bezirk (jedes Mal ein anderer Bezirk)
- Short oder long Ausflug per Command Argument

# Einrichtung:
Die Datei data_city.py muss angepasst werden. Distance beschreibt, ob es sich um einen großen 
oder kleinen Ausflug handelt. Hier ein Beispiel (ohne Berlin-Mitte) für Berlin:

    city_districts = [
        {
            "name": "Charlottenburg-Wilmersdorf",
            "subdistrict": ['Charlottenburg', 'Charlottenburg-Nord', 'Grunewald', 'Halensee', 'Schmargendorf', 'Westend',
                            'Wilmersdorf'],
            "distance": "short",
        },
        {
            "name": "Friedrichshain-Kreuzberg",
            "subdistrict": ["Friedrichshain", "Kreuzberg"],
            "distance": "short",
        },
        {
            "name": "Lichtenberg",
            "subdistrict": ['Alt-Hohenschönhausen', 'Falkenberg', 'Fennpfuhl', 'Friedrichsfelde', 'Karlshorst',
                            'Lichtenberg', 'Malchow', 'Neu-Hohenschönhausen', 'Rummelsburg', 'Wartenberg'],
            "distance": "short",
        },
        {
            "name": "Marzahn-Hellersdorf",
            "subdistrict": ['Biesdorf', 'Hellersdorf', 'Kaulsdorf', 'Mahlsdorf', 'Marzahn'],
            "distance": "long",
        },
        {
            "name": "Neu-Kölln",
            "subdistrict": ['Britz', 'Buckow', 'Gropiusstadt', 'Neukölln', 'Rudow'],
            "distance": "long",
        },
        {
            "name": "Pankow",
            "subdistrict": ['Blankenburg', 'Blankenfelde', 'Buch', 'Französisch Buchholz', 'Heinersdorf', 'Karow',
                            'Niederschönhausen', 'Pankow', 'Prenzlauer Berg', 'Rosenthal', 'Stadtrandsiedlung Malchow',
                            'Weißensee', 'Wilhelmsruh'],
            "distance": "short",
        },
        {
            "name": "Reinickendorf",
            "subdistrict": ['Borsigwalde', 'Frohnau', 'Heiligensee', 'Hermsdorf', 'Konradshöhe', 'Lübars',
                            'Märkisches Viertel', 'Reinickendorf', 'Waidmannslust', 'Wittenau'],
    
            "distance": "short",
        },
        {
            "name": "Spandau",
            "subdistrict": ['Falkenhagener Feld', 'Gatow', 'Hakenfelde', 'Haselhorst', 'Kladow', 'Siemensstadt', 'Spandau',
                            'Staaken', 'Wilhelmstadt'],
            "distance": "short",
        },
        {
            "name": "Steglitz-Zehlendorf",
            "subdistrict": ['Dahlem', 'Lankwitz', 'Lichterfelde', 'Nikolassee', 'Steglitz', 'Wannsee', 'Zehlendorf'],
            "distance": "long",
        },
        {
            "name": "Tempelhof-Schöneberg",
            "subdistrict": ['Buckow', 'Friedenau', 'Kreuzberg', 'Lichtenrade', 'Mariendorf', 'Marienfelde', 'Schöneberg',
                            'Tempelhof'],
            "distance": "short",
        },
        {
            "name": "Treptow-Köpenik",
            "subdistrict": ['Adlershof', 'Alt-Treptow', 'Altglienicke', 'Baumschulenweg', 'Bohnsdorf', 'Friedrichshagen',
                            'Grünau', 'Köpenick', 'Müggelheim', 'Niederschöneweide', 'Oberschöneweide', 'Plänterwald',
                            'Rahnsdorf', 'Schmöckwitz'],
            "distance": "long",
        },
    ]

Die Datei data.py muss erzeugt werden: 
    
    MAIL_ADDRESS = "my@email.com"
    MAIL_PASSWORD = "mypassword"
    IMAP_SERVER = 'my_IMAP_Server_Address'
    
    PLAYER = [
        {"name": "Name1", "mail": "name1@email.com"},
        {"name": "Name2", "mail": "name2@email.com"}
    ]
    
    # Distance argument, if there is no argument with command:
    distance = "long"  # short or long

# Start des Scripts:
    python3 main.py short

Anschließend bekommt der Gewinner eine Mail:

<img width="460" alt="Winner-Mail" src="https://user-images.githubusercontent.com/72299469/159120646-670e1a0d-4f6c-44e4-b0ac-a04d7bfa5149.jpg">

Nach der Antwort per Mail kommt die Bestätigung:

<img width="460" alt="Confirmation" src="https://user-images.githubusercontent.com/72299469/159120642-3d1a3ce7-c11f-458e-b6b5-75cf735116e3.jpg">

Das Log sieht dann so aus:

<img width="460" alt="history.txt" src="https://user-images.githubusercontent.com/72299469/159121113-7e7c596b-a1cb-41b9-a93d-8eb2da36aafa.png">