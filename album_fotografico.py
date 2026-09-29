from csv import reader

def carica_da_file(file_path):
    try:
        foto_per_anno={}
        with open(file_path,"r") as csvfile:
            lettore=reader(csvfile)
            for row in lettore:
                try:
                    anno = int(row[4])
                except ValueError:
                    #se row[4] è "Anno" il codice entra qui e salta il giro
                    continue
                foto=row[0:4]
                if anno not in foto_per_anno:
                    foto_per_anno[anno]=[]
                foto_per_anno[anno].append(foto)
            return foto_per_anno

    except FileNotFoundError:
        return None


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    try:
        if anno not in album:
            album[anno]=[]
        nuovafoto=[codice,titolo,autore,mese]
        album[anno].append(nuovafoto)
        return nuovafoto

    except OSError :
        return None


def cerca_foto(album, codice):
    try:
        for key in album:
            for foto in album[key]:
                if foto[0] == codice:
                return f"{foto[0]},{foto[1]},{foto[2]},{foto[3]},album[key]"
            return None
    except:
        return None


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO


def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
