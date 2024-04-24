# Koguciki

Aplikacja "Koguciki" jest projektem komercyjnym zaprojektowanym na zlecenie klienta, mającym na celu usprawnienie zarządzania procesami hodowlanymi. Aplikacja umożliwia użytkownikom wprowadzanie i analizę danych dotyczących hodowli drobiu, w tym liczby piskląt, zużycia paszy, a także obliczanie wskaźników takich jak śmiertelność i efektywność zużycia paszy.

## Technologie i wymagania:
- Python 3
- Flask
- Jinja2
- CSS
- Gunicorn (do wdrożenia na Heroku)

## Strona dostępna online:
Strona jest już opublikowana i dostępna pod adresem [Koguciki](https://kogutki-f05ac1087282.herokuapp.com/).

## Jak uruchomić aplikację lokalnie:
1. Zainstaluj Python 3 oraz odpowiednie zależności ze środowiska wirtualnego.
2. Zainstaluj wymagane zależności przy pomocy polecenia: `pip install -r requirements.txt`.
3. Uruchom aplikację za pomocą polecenia: `flask run` lub użyj Gunicorn jeżeli wdrażasz na produkcję: `gunicorn app:app`.
4. Aplikacja powinna być dostępna lokalnie na `http://127.0.0.1:5000/`.

## Struktura projektu:
- `app.py`: Główny plik aplikacji serwerowej.
- `functions.py`: Moduł pomocniczy zawierający logikę biznesową.
- `requirements.txt`: Lista zależności potrzebnych do uruchomienia aplikacji.
- `templates/`: Folder zawierający szablony HTML.
- `static/`: Folder zawierający pliki statyczne, takie jak CSS i obrazy.

Aplikacja została zaprojektowana, zbudowana i zaakceptowana przez klienta, spełniając wszystkie oczekiwania w zakresie funkcjonalności i wydajności. Została opublikowana i jest dostępna dla użytkowników.
