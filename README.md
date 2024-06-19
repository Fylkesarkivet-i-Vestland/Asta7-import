# Skript for håndtering av døde kryssreferanser for improt av arkivstruktur.xml i Asta7 

## Innstruks

Forutsetter at python er installert.
1. Last ned skriptet.
2. Legg skriptet i samme mappe som .xml-filen som du ønsker å validere for import i Asta7
3. Åpne skriptet i en teksteditor, og legg til navnet på .xml-filen
4. Lagre det endrerde skriptet
5. Åpne terminal 
6. Flytt til mappe med skriptet og .xml-filen med cd ../.. kommando
7. Kjør skriptet med kommandoen "python3 validate_uuids.py"
8. Terminalen jobber seg igjennom .xml-filen og output vil være en tekstfil med ugyldige kryssreferanser 

