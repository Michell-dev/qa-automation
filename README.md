# QA Automation Suite

Suite de pruebas automatizadas con Selenium y pytest sobre la aplicación web [SauceDemo](https://www.saucedemo.com).

## Tecnologías

- Python 3.12
- Selenium 4
- pytest
- pytest-html
- Page Object Model (POM)

## Instalación

```bash
git clone https://github.com/Michell-dev/qa-automation.git
cd qa-automation
python3 -m venv venv
source venv/bin/activate
pip install selenium pytest pytest-html webdriver-manager
```

## Casos de prueba

| Test | Qué verifica |
|---|---|
| test_selenium.py | Que la página carga correctamente |
| test_login.py | Login exitoso con credenciales válidas |
| test_login_fallido.py | Mensaje de error con credenciales incorrectas |
| test_espera.py | Carga del inventario con espera explícita |
| test_pom.py | Login usando Page Object Model |

## Ejecutar los tests

```bash
pytest -v
```

## Generar reporte HTML

```bash
pytest -v --html=reporte.html --self-contained-html
```
