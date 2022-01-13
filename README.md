# Symulator maszyny szyfrującej Enigma
### Projekt na przedmiot Podstawy Informatyki i Programowania, semestr 21Z
### Autor: Kajetan Rożej
## Wstęp
Enigma to niemiecka przenośna elektromechaniczna maszyna szyfrująca, oparta na mechanizmie obracających się wirników, skonstruowana przez Artura Scherbiusa. Chociaż w użytku komercyjnym znajdowała się już od lat 20 XX wieku największą „sławę” zawdzięcza II Wojnie Światowej podczas której wykorzystywana była przez stronę niemiecką do kodowania wiadomości wojskowych. Ocenia się, że złamanie szyfru Enigmy przez Aliantów pozwoliło zakończyć wojnę kilka lat wcześniej. W tym przełomowym wydarzeniu niebagatelną rolę odegrali również polscy kryptolodzy: Marian Rejewski, Jerzy Różycki i Henryk Zygalski.
## Cel Projektu
Celem projektu było napisanie programu komputerowego który swym działaniem symulowałby maszynę szyfrującą Enigma. Nie chodziło jednak o odwzorowywanie konkretnego modelu urządzenia, a o uogólnioną implementację maszyny wirnikowej, z niezdefiniowaną odgórnie liczbą wirników (w przeciwieństwie do fizycznych urządzeń). Stworzony program miał mieć możliwość kodowania tekstu litera po literze (jak w oryginalnej maszynie) oraz kodowania tekstu z pliku. Dodatkową wartością symulatora miał być element edukacyjno-poznawczy, pozwalający prześledzić „drogę” kodowanej litery w celu lepszego zrozumienia działania maszyny.

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
    |	|_ dialog_windows.py
    |
    |_ rsc
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
    |
    |_ rsc_manager.py
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
	 - ...
	 - ...
	 - ...
	 - ...
	 - ...

- rsc - zawierający pliki z zasobami i zapisaną konfigurację:
     - config.json
     - default.json
     -  custom.json
- tests - zawierający testy jednostkowe do projektu

oraz trzy pliki w katalogu głównym:

- rsc_manager.py - odpowiadający za zarządzanie plikami w katalogu rsc
- enigma.py - główny program, wywoływany z konsoli z odpowiednimi flagami
- README.md - plik z dokumentacją


## Format plików konfiguracyjncyh

## Instrukcja użytkownika

## Podsumowanie





