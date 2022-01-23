# Symulator maszyny szyfrującej Enigma
### Projekt na przedmiot Podstawy Informatyki i Programowania, semestr 21Z
### Autor: Kajetan Rożej
## Wstęp
Enigma to niemiecka przenośna elektromechaniczna maszyna szyfrująca, oparta na mechanizmie obracających się wirników, skonstruowana przez Artura Scherbiusa. Chociaż w użytku komercyjnym znajdowała się już od lat 20 XX wieku największą „sławę” zawdzięcza II Wojnie Światowej podczas której wykorzystywana była przez stronę niemiecką do kodowania wiadomości wojskowych. Ocenia się, że złamanie szyfru Enigmy przez Aliantów pozwoliło zakończyć wojnę kilka lat wcześniej. W tym przełomowym wydarzeniu niebagatelną rolę odegrali również polscy kryptolodzy: Marian Rejewski, Jerzy Różycki i Henryk Zygalski.
## Cel Projektu
Celem projektu było napisanie programu komputerowego który swym działaniem symulowałby maszynę szyfrującą Enigma. Nie chodziło jednak o odwzorowywanie konkretnego modelu urządzenia, a o uogólnioną implementację maszyny wirnikowej, z niezdefiniowaną odgórnie liczbą wirników (w przeciwieństwie do fizycznych urządzeń). Stworzony program miał mieć możliwość kodowania tekstu litera po literze (jak w oryginalnej maszynie) oraz kodowania tekstu z pliku. Dodatkową wartością symulatora miał być element edukacyjno-poznawczy, pozwalający prześledzić „drogę” kodowanej litery w celu lepszego zrozumienia działania maszyny.

## Wykorzystane narzędzia
Projekt zrealizowano w języku programowania Python, wersja 3.8.10. Interfejs graficzny napisano z wykorzystaniem biblioteki Qt i Pyside. Do edycji kodu wykorzytsano program Visual Studio Code. Program testowano z użyciem frameworka pytest w wersji 6.2.5

## Struktura Projektu

	.
    |_ enigma_classes
	|	|_ rotor_class.py
	|	|_ plugboard_class.py
	|	|_ reflector_class.py
	|	|_ enigma_class.py
	|	|_ functions.py
	|
    |_ enigma_gui
    |	|_ gui.py
    |	|_ main_window.py
    |	|_ enigma.ui
    |	|_ table_models.py
    |	|_ dialogs.py
    |   |_ errors.py
    |
    |_  rsc
    |	|_ config.json
    |	|_ default.json
    |	|_ custom. json
    |
    |_ tests
    |	|_ test_rotor_class.py
    |	|_ test_plugboard_class.py
    |	|_ test_reflector_class.py
    |	|_ test_enigma_class.py
    |	|_ test_functions.py
    |	|_ test_rsc_manager.py
    |	|_ test_elements_database.py
    |
    |_ rsc_manager.py
    |_ elements_database.py
    |_ enigma.py
    |_ README.md

Na strukturę projektu składają się cztery podkatalogi:

 - enigma_classes - z implementacją klas poszczególnych elementów Enigmy i samej maszyny:
	 -  rotor_class.py – implementacja klasy reprezentującej wirinik
	 - plugboard_class.py – implementacja klasy reprezentującej łącznicę kablową
	 - reflector_class.py – implementacja klasy reprezentującej bęben odbijający
	 -  enigma_class.py – implementacja klasy reprezentującej całą maszynę z wirnikami, bębnem odbijającym i łącznicą kablową
	 - functions.py – wyodrębnienie funkcji wykorzystywanych w wielu klasach

 -  enigma_gui – zawierające pliki z implementacją interfejsu graficznego:
	 - gui.py - główny plik z klasą EnigmaWindow (zasadnicze okno programu)
	 - main_window.py - kompozycja głównego okna programu wygenerowana z pliku .ui przy użyciu pyside-uic
	 - enigma.ui - kompozycja głównego okna stworzona przy użyciu designera
	 - table_models.py - modele tabel wyświatlanych w interfejsie
	 - dialogs.py - definicje okien dialogowych wyświetlanych w ramach interfejsu
     - errors.py - definicje informacji o błędach wyświetlanych w ramach interfejsu

- rsc - zawierający pliki z zasobami i zapisaną konfigurację:
     - config.json - domyślna konfiguracja maszyny szyfrującej
     - default.json - baza domyślnych elementów (wirników i bębnów odbijających) pochodzących z oryginalnej Enigmy
     - custom.json - baza elementów zdefiniowanych przez użytkownika

- tests - zawierający testy jednostkowe do projektu

oraz cztery pliki w katalogu głównym:

- rsc_manager.py - odpowiadający za zarządzanie plikami (zapis i odczyt oraz podstawowa obróbka) znajdującymi się w katalogu w katalogu rsc
- elements_database.py - zawi
- enigma.py - główny program, wywoływany z konsoli z odpowiednimi parametrami
- README.md - plik z dokumentacją


## Format plików konfiguracyjncyh

- conf.json
      - machine
          - rotors
          - rings
          - start_position
          - reflector
          - plugboard
      - settings
          - double_step
          - space_dist

    {
        "machine": {
            "rotors": [
            ],
            "rings": "QAA",
            "start_positions": "TAA",
            "reflector": "reflectorUKWC",
            "plugboard": "AS DF RY"
        },
        "settings": {
            "double_step": # if true double step is enabled, if false disabled
            "space_dist": # distance between
        }
    }

- custom.json and default.json
      - rotors
          - [
          - name
          - wiring
          - indentation
          - ]

      - reflectors
          - [
          - name
          - wiring
          - ]
    {
        "rotors": [
            {
                "name": "ROTOE1",
                "wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "indentations": "AF"
            }
        ],
        "reflectors": [

            {
                "name": "reflectorUKWB",
                "wiring": "AY BR CU DH EQ FS GL IP JX KN MO TZ VW"
            }
        ]
    }


Nie jest zalecane samodzielne modyfikowanie plików konfiguracyjnych!!!
## Instrukcja użytkownika
Uruchomienia programu należy dokonać poprzez jego wywołanie z konsoli z odpowiednimi parametrami:

    usage: enigma.py [-h] [-m] [-i] [-o] [-c]

    Simulate Enigma machine.

    optional arguments:
    -h, --help           show this help message and exit
    -m , --mode          define the mode in wich programme should be run (default: gui)
    -i , --input_file    file with plain text to encode, required in cmd mode
    -o , --output_file   file with result (default: result.txt)
    -c , --config        json file with initial configuration of machine (default: .../rsc/config.json)

Domyślnie (bez podania żadnych parametrów) program uruchomi się w postaci interfejsu graficznego.

### Tryb interfejsu graficznego
Funkcje:
- związane stricte z maszyną szyfrującą
    - kodowanie tekstu litera po literze wraz z wyświetleniem poszczególnych kroków
    - kodowanie tekstu z pliku wejściowego do pliku wynikowego
    - zmiana obecnej konfiguracji maszyny
- związane ogólnie z działaniem symulatora
    - dodanie/usunięcie/modyfikacja spersonalizowanych wirników
    - dodanie/usunięcie/modyfikacja spersonalizowanych bębnów odbijających
    - zmiana ustawień

Każdej z funkcji odpowiada jedno okno programu, do którego przenieść się można dzięki rozwijanemu górnemu menu

## Podsumowanie
Podsumowując efekty pracy uważam, że



