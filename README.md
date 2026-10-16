# 🌿 Elena Vance Studio • Infoproducto E-Commerce

> Sistema integral de contenidos, embudo de ventas y producto digital **"The 21-Day Gentle Wall Reset Guide"** diseñado para movilidad articular en adultos +45.

---

## 🚀 Despliegue en Vercel

Este proyecto está 100% preparado para desplegarse en **Vercel** en menos de 1 minuto:

1. Ve a [vercel.com/new](https://vercel.com/new).
2. Conecta tu cuenta de GitHub y selecciona el repositorio **`jakesroodriguez/infoproducto`**.
3. En **Framework Preset**, déjalo en **`Other`** (proyecto estático).
4. Pulsa **Deploy**.

---

## 🌐 Estructura y Rutas Web (Rutas Limpias con `vercel.json`)

| Ruta | Archivo Destino | Descripción |
| :--- | :--- | :--- |
| **`/`** o **`/dashboard`** | `index.html` / `dashboard_contenidos.html` | **Master Content Engine (30 Días)**: Dashboard interactivo con calendario, guiones diarios, prompts de IA y simulador móvil de Instagram |
| **`/tienda`** o **`/landing`** | `01_TIENDA_Y_WEB/landing_page.html` | **Página de Ventas Oficial**: Landing page de conversión optimizada con checkout, insignias de pago y prueba social |
| **`/guia`** | `02_PRODUCTO_GUIA/guide_printable.html` | **Guía Interactiva 21 Días**: Versión web responsive e imprimible de la rutina de pared |
| **`/guia-pdf`** | `02_PRODUCTO_GUIA/The_21_Day_Gentle_Wall_Reset_Guide.pdf` | **Documento PDF Oficial** listo para entrega automática a clientes |
| **`/descargar`** | `descargar.html` | **Página de Descarga Móvil**: Reproductor y botón de descarga directa para el reel de video |

---

## 📁 Arquitectura del Repositorio

```text
├── index.html                   # Entry point para Vercel (Dashboard Master de 30 Días)
├── dashboard_contenidos.html    # Motor de contenidos interactivo
├── descargar.html               # Vista de descarga optimizada para móviles
├── vercel.json                  # Configuración de URLs amigables para Vercel
├── 01_TIENDA_Y_WEB/             # Assets y landing page oficial de venta
│   ├── landing_page.html
│   ├── pagina_venta_gumroad.md
│   ├── icons/payment/           # Sellos de seguridad y pasarelas de pago
│   └── INSTAGRAM_HIGHLIGHTS/    # Portadas de historias destacadas
├── 02_PRODUCTO_GUIA/            # Infoproducto principal
│   ├── The_21_Day_Gentle_Wall_Reset_Guide.pdf
│   ├── guide_printable.html
│   └── guia_21_dias_completa.md
├── 03_REELS_Y_VIDEOS/           # Guiones, audios, subtítulos (.srt/.ass) y videos
│   ├── POST1/
│   ├── POST2/
│   └── POST3/ (con POST3.mp4 listo)
├── 04_PROMPTS_IA/               # Lotes de prompts optimizados para IA (Google Flow / Midjourney)
└── 05_AVATAR_ELENA/             # Fotografías y ficha visual del avatar de Elena
```

---

## 🛠️ Tecnologías Utilizadas

- **Frontend:** HTML5, Tailwind CSS, Google Fonts (Plus Jakarta Sans, Playfair Display, Fraunces).
- **IA & Media:** Prompts fotorealistas anti-IA para Google Flow, generador de subtítulos `.srt`/`.ass` y Remotion Hooks.
- **Hosting:** Vercel Static Hosting.
