Instrukcja uruchomienia projektu
Aplikacja jest w pełni skonteneryzowana. Do jej uruchomienia wymagany jest jedynie zainstalowany Docker.
Sklonuj repozytorium na dysk lokalny:
Bash:
git clone https://github.com/Pablo1-22/Nowatorski_Projekt_Ind.git
cd Nowatorski_Projekt_Ind
Projekt wykorzystuje Docker Compose do orkiestracji serwisu aplikacji (FastAPI) oraz bazy danych (PostgreSQL). Aby zbudować i uruchomić środowisko w tle, wpisz:
Bash:
docker compose up -d –build
Po uruchomieniu aplikacja jest dostępna pod adresem: http://localhost:8000
Dostępne punkty końcowe (Endpoints):
- Dokumentacja API: http://localhost:8000/docs – tu można ręcznie testować endpointy.
- Status aplikacji:  http://localhost:8000/
- Test połączenia z bazą danych: http://localhost:8000/health-db – sprawdza czy kontener Python widzi kontener PostgreSQL.
Testy integracyjne są wykonywane wewnątrz kontenera, aby uruchomić testy ręcznie:
Bash:
docker compose exec web pytest
Aby zatrzymać kontenery i zwolnić zasoby:
Bash:
docker compose down
