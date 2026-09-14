# Yaku Landing — Stack Técnico y Guía de Despliegue

## 1. Información General del Proyecto
- **Tipo de Proyecto**: Landing Page estática institucional y comercial para el producto YakuControl (tecnología acuícola de precisión).
- **Arquitectura**: Single Page Application estática (Vanilla Web).
- **Lenguajes / Tecnologías Core**: HTML5 semántico, CSS3 moderno (Custom Properties / CSS Variables, Flexbox, Grid, Glassmorphism, Keyframe Animations), Vanilla JavaScript ES6+.

---

## 2. Decisiones de Diseño y Rendimiento

| Aspecto | Implementación | Propósito |
|---|---|---|
| **Estructura** | HTML5 semántico | Accesibilidad y SEO optimizado (etiquetas semánticas, metadatos responsivos). |
| **Estilos & UI** | CSS3 Vanilla con paleta temática acuícola (`--ink`, `--cyan`, `--blue`, `--mist`) | Cero dependencias externas de frameworks pesados; carga instantánea y rendimiento ultrarrápido (99+ en Google PageSpeed). |
| **Tipografía** | Google Fonts (`DM Sans`, `DM Mono`) | Tipografía moderna pre-conectada mediante `preconnect`. |
| **Interactividad** | JavaScript nativo (IntersectionObserver API, DOM events) | Acordeón FAQ accesible, animaciones de barras al hacer scroll y contadores numéricos reactivos sin librerías externas. |

---

## 3. Servicios Externos e Integraciones

1. **Google Fonts CDN**: Fuentes web tipográficas (`DM Sans`, `DM Mono`).
2. **Yaku Web App App Link**: Enlace directo en el botón CTA hacia la aplicación web de YakuControl.

---

## 4. Cómo Probar y Desplegar Localmente

### Ejecución Local
No requiere compilación ni instalación de dependencias (`npm` / `node`).

- **Opción 1 (Directa):** Abrir el archivo `index.html` directamente en cualquier navegador web.
- **Opción 2 (Servidor HTTP local con Python):**
  ```bash
  python -m http.server 3000
  ```
  Acceder a `http://localhost:3000`.

- **Opción 3 (VS Code Live Server o npx serve):**
  ```bash
  npx serve .
  ```

### Opciones de Despliegue en Producción
- **GitHub Pages**: Despliegue automático desde la rama `main`.
- **Vercel / Netlify / Cloudflare Pages**: Despliegue estático con 1 click.
- **Firebase Hosting / Azure Static Web Apps / AWS S3 + CloudFront**.
