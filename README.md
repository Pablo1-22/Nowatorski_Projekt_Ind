Instrukcja uruchomienia projektu<br>
Aplikacja jest w pełni skonteneryzowana. Do jej uruchomienia wymagany jest jedynie zainstalowany Docker.<br>
Sklonuj repozytorium na dysk lokalny:<br>
Bash:<br>
git clone https://github.com/Pablo1-22/Nowatorski_Projekt_Ind.git<br>
cd Nowatorski_Projekt_Ind<br>
Projekt wykorzystuje Docker Compose do orkiestracji serwisu aplikacji (FastAPI) oraz bazy danych (PostgreSQL). Aby zbudować i uruchomić środowisko w tle, wpisz:<br>
Bash:<br>
docker compose up -d –build<br>
Po uruchomieniu aplikacja jest dostępna pod adresem: http://localhost:8000<br>
Dostępne punkty końcowe (Endpoints):
- Dokumentacja API: http://localhost:8000/docs – tu można ręcznie testować endpointy.
- Status aplikacji:  http://localhost:8000/
- Test połączenia z bazą danych: http://localhost:8000/health-db – sprawdza czy kontener Python widzi kontener PostgreSQL.<br>

Testy integracyjne są wykonywane wewnątrz kontenera, aby uruchomić testy ręcznie:<br>
Bash:<br>
docker compose exec web pytest<br>
Aby zatrzymać kontenery i zwolnić zasoby:<br>
Bash:<br>
docker compose down
