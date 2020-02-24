
##Progetto Teoria della sicurezza e crittografia 2019-2020 Gruppo: Politi – Salman – Silvestri

Valutazione costi benefici dei principali algoritmi di crittografia:

RSA
ECC
AES
Blowfish Confrontiamo 1 vs 2 e 3 vs 4. La valutazione sarà effettuata secondo le caratteristiche: Per RSA e ECC dobbiamo generare chiavi, mentre per AES e BLOWFISH non occorre. Misurare al limite entropia con i genenratori random • Entropia o Chiavi sia pubbliche sia private: generiamo un campione esaustivo di chiavi e le concateniamo. Con OpenSSL utilizziamo il formato di uscita der( binario) e misuriamo l’entropia. o Messaggi: i messaggi devono essere cifrati. ? Usiamo generatore numeri casuali Butterfly (meno prevedibile di Strong):?Stringa base di almeno 100Mb
 
• Creazione messaggio (multiplo di 2048 per RSA e multiplo di 320 per ECC, etc..) ? Test1: • misuriamo entropia & Die-Hard delle stringa generata • cifriamo con RSA / ECC /AES /BLOWFISH e verifichiamo se entropia & Die-Hard aumenta o diminuisce( sia senza paddig sia con padding) ? Test2: comportamento su stringa uniforme( 1111111111) la cifriamo con i vari padding( 2 o 3 diversi) e misuriamo entropia e Die-Hard dei messaggi cifrati.
• Lunghezza del messaggio ( input o output) o Misuriamo la variazione di entropia e la velocità di cifratura e decifratura in base alla lunghezza del messaggio e creiamo dei report che indicano il comportamento asintotico

• Velocità di cifratura e decifratura o Direttamente da OpenSSL poco senso

• Velocità di generazione delle chiavi o Misuriamo il tempo di generazione delle chiavi da valori [0 a 2048] bit e creiamo dei report che indicano il comportamento asintotico. o Confrontiamo ECC/7 ( circa 320) con RSA(2048) perché le chiavi ECC sono più corte.

• Tecnica di padding o Decifrare il messaggio più un numero casuale; una motivazione valida è la seguente: se abbiamo una chiave privata e una pubblica e il messaggio inviato è sempre lo stesso, sniffando il canale risulterebbe che viaggia sempre lo stesso messaggio. o Il ricevente deve sapere come è fatto il padding. Con il padding si abbassa la randomicià ( es: sto cifrando meno bit di 1024 perché una parte è fissa, quella del padding) o Struttura padding con standard PKCS ?PKCS1 o Verifichiamo che riduce entropia ( mette una componente strutturata nel messaggio!) • Valutazioni: o Cosa scegliamo e perché o Report o La nostra misura di Entropia rispetto ai Test Die-Hard ( vedere se la valutazione Die-Hard segue lo stesso andamento della nostra Entropia) o Data la stringa di partenza e calcolata l’entropia verifichiamo se e come migliorano entropia gli algoritmi di cifratura.

Strumenti a disposizione : Test DieHard-random (Marsaglia): sono una batteria di test statistici per misurare la qualità di un generatore di numeri casuali. Sono stati sviluppati da George Marsaglia per diversi anni e pubblicati per la prima volta nel 1995
