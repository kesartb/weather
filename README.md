# Weather Forecast for Kindle Touch

Este repositorio contiene un script que actualiza un archivo HTML con la previsión del tiempo para Valencia, España, cada 30 minutos. El archivo HTML está diseñado para ser compatible con el navegador experimental del Kindle Touch.

## 🛠 Cómo funciona

1. **Script Python**: `update_weather.py` obtiene datos meteorológicos actuales desde OpenWeatherMap y actualiza `weather_forecast.html`.
2. **GitHub Actions**: Un workflow (`.github/workflows/update-weather.yml`) ejecuta el script automáticamente cada 30 minutos.
3. **Kindle Touch**: El archivo HTML es muy ligero y contiene una etiqueta `<meta>` que recarga la página cada 30 minutos.

## 🚀 Configuración

### Requisitos

- Cuenta de GitHub
- Clave de API de OpenWeatherMap
- Token personal de GitHub (PAT) con permisos `repo`

### Pasos

1. **Clona este repositorio** en tu cuenta.
2. **Agrega los secretos** en GitHub:
   - `OWM_API_KEY`: tu clave de OpenWeatherMap
   - `GH_PAT`: tu token personal de GitHub con permisos de escritura
3. **Verifica que el archivo `.github/workflows/update-weather.yml` esté presente**.
4. El workflow se ejecutará automáticamente cada 30 minutos y actualizará el archivo `weather_forecast.html`.

## 📱 Visualización en Kindle Touch

1. Abre el navegador experimental del Kindle.
2. Accede a la URL donde esté alojado el archivo `weather_forecast.html` (por ejemplo, usando GitHub Pages o un servidor propio).
3. La página se recargará automáticamente cada 30 minutos con la información más reciente.
