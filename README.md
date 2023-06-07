# Todo-List-Verwaltung

 ## Kundenanforderungen analysieren
 
Folgende Beschreibung der Schnittstelle ist gegeben:
Es soll eine Server-Anwendung erstellt werden, mit deren Hilfe Todo-Listen mit ent- sprechenden Einträgen erstellt und bearbeitet werden können. Jede Liste besteht aus einer beliebigen Anzahl an Einträgen.
Jeder Eintrag einer Todo-Liste besteht aus einer ID, einem Namen, einer optionalen Beschreibung und der Zuordnung zu einer Todo-Liste. Jede Todo-Liste besitzt neben der ID einen Namen.
Die Schnittstelle muss es ermöglichen, Listen neu anzulegen und bestehende Listen zu löschen. Über einen Endpunkt können alle Einträge der Liste geladen werden. Außer- dem müssen Einträge in Listen hinzugefügt und gelöscht werden können.
Eine Authentifizierung ist zunächst nicht zu planen bzw. implementieren. Aus Sicher- heitsgründen sollen jedoch als IDs keine fortlaufenden Nummern verwendet werden. Statt dessen werden zufällige UUID genutzt.
