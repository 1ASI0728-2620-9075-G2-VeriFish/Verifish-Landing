# YakuControl Landing

Sitio estático: HTML, CSS y JavaScript. Publicar la raíz en Netlify; `netlify.toml` configura el directorio.

## Desarrollo y pruebas

```sh
python3 -m http.server 8000
# En otra terminal y con un entorno virtual activo:
python3 -m pip install -r requirements-dev.txt
python3 -m playwright install chromium
python3 -m unittest discover -s tests -v
```

Las cuatro pruebas Playwright cubren navegación, contacto válido e inválido, términos y presentación móvil. Si Chromium está instalado en otra ubicación, se puede indicar `PLAYWRIGHT_CHROMIUM_EXECUTABLE`.

El formulario valida en el navegador: no transmite ni guarda solicitudes. YakuTrace explica un flujo en prototipo y no verifica lotes reales. Los precios están por definir con los pilotos, según el informe. Los accesos a la Web apuntan a https://yakucontrol-v2.web.app.

## Publicación

En Netlify, importar este repositorio, seleccionar la rama revisada y publicar `.` sin comando de build. No se necesita instalar paquetes de producción. Confirmar que la cuenta tenga permisos antes de asociar el sitio; no se creó un sitio alternativo automáticamente.
