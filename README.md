# 🧪 Frameworks de Control de Calidad con Jenkins

Este proyecto demuestra la aplicación práctica de **frameworks de control de calidad** en un entorno Python, utilizando **Jenkins** como orquestador de integración continua (CI) para ejecutar pruebas automatizadas, generar reportes visuales y realizar análisis de seguridad.

Se toma como caso de estudio una **aplicación IA que clasifica mensajes según urgencia** usando Gemini (Google AI), expuesta vía FastAPI y con interfaz en Streamlit.

---

## 👨‍💻 Grupo N°8 - Programación para Dispositivos Móviles 

Exposición: **Frameworks de Control de Calidad**  
Caso práctico: **Clasificación Inteligente de Mensajes con IA y Validación Continua con Jenkins**

---

## 🎯 Objetivo del Proyecto

Implementar un sistema completo de validación continua aplicando frameworks de control de calidad que aseguren:

- La funcionalidad correcta de la API (tests unitarios)
- Resultados visuales claros (reportes HTML y JUnit)
- Análisis de seguridad en el código (Bandit + Warnings NG)
- Automatización completa mediante **pipelines de Jenkins**

---

## 🛠️ Herramientas y Frameworks Utilizados

| Tipo de herramienta            | Tecnología utilizada                     |
|-------------------------------|------------------------------------------|
| **CI/CD**                     | Jenkins 2.504.2                          |
| **Seguridad estática**        | Bandit 1.8.3                             |
| **Testing unitario**          | Pytest                                   |
| **Reportes funcionales**      | JUnit (XML) + HTML Plugin                |
| **Análisis de advertencias**  | Warnings Next Generation (CheckStyle)    |
| **Infraestructura virtual**   | Python venv                              |
| **Publicación de resultados** | HTML Publisher Plugin                    |

---

## 🖥️ Instalación de Jenkins (Opcional)

Si deseas implementar estos pipelines en tu propio entorno, necesitas tener **Jenkins** instalado previamente.

### 🔧 ¿Cómo instalar Jenkins?

A continuación, se proporcionan dos tutoriales en video, uno para cada sistema operativo. Ambos explican paso a paso cómo instalar y dejar funcionando Jenkins localmente.

| Sistema Operativo | Tutorial en YouTube |
|----------------|----------------------|
| 🪟 Windows      | [Ver tutorial](https://www.youtube.com/watch?v=3OY3A6XE6Us) |
| 🐧 Linux  | [Ver tutorial](https://www.youtube.com/watch?v=2_V-rXOpPKo&t=4s) |

> ⚠️ Recomendación: Tras instalar Jenkins, asegúrate de instalar los plugins:
> - **Warnings Next Generation**
> - **HTML Publisher**
> - **Git Plugin**
> - **Pipeline**
> - **Script Security**

Además, configura credenciales en Jenkins si necesitas usar claves de API (como `GEMINI_API_KEY`).

---

## 📁 Pipelines Desarrollados en Jenkins

Se implementaron 4 pipelines enfocados en **aspectos clave del control de calidad**:

| Proyecto Jenkins           | Función de Control de Calidad               |
|---------------------------|---------------------------------------------|
| ✅ **Demo-Calidad-Simple**     | Validación funcional con pruebas unitarias |
| ✅ **Demo-Calidad-HTML**       | Generación de reportes visuales en HTML    |
| ✅ **Demo-Calidad-Paralelo**   | Pruebas simultáneas (tiempo y cobertura)   |
| ✅ **Demo-Calidad-Seguridad**  | Análisis de seguridad con Bandit           |

---

## 🧩 ¿Qué hace cada Jenkinsfile?

### 🔧 `Demo-Calidad-Simple`

Pipeline secuencial:
- Clona el repositorio.
- Levanta la API FastAPI.
- Ejecuta `pytest` (report.xml).
- Publica resultados con el plugin **JUnit**.

👉 Ideal para control de calidad funcional básico.

---

### 🌐 `Demo-Calidad-HTML`

Pipeline con salida visual:
- Corre pruebas en `test_extra.py`.
- Genera `report.html` con Pytest.
- Publica visualmente usando **HTML Publisher**.

👉 Apto para validaciones legibles por no técnicos.

---

### ⚡ `Demo-Calidad-Paralelo`

Pipeline optimizado:
- Ejecuta 3 pruebas simultáneas:
  - Clasificación urgente
  - Clasificación normal
  - Pruebas generales

👉 Muestra cómo Jenkins permite paralelizar etapas para ganar tiempo y visibilidad.

---

### 🔐 `Demo-Calidad-Seguridad`

Pipeline de análisis estático:
- Ejecuta **Bandit** sobre el código fuente.
- Convierte resultados JSON a CheckStyle XML.
- Publica con **Warnings NG**:
  - Panel visual de errores por severidad.
  - Gráficas e historial de builds.

👉 Permite integrar control de seguridad dentro del proceso de calidad continua.

---

## 📊 Resultados Visuales

- **Warnings NG** muestra errores como: uso de `eval`, inyección de comandos, etc.
- **HTML Reports** permiten mostrar resultados claros.
- **JUnit XML** facilita integración con cualquier dashboard de calidad.

---

## 📌 Conclusión

> Este proyecto evidencia cómo un sistema real puede beneficiarse del uso de **frameworks de control de calidad** automatizados, desde pruebas funcionales hasta análisis de seguridad, todo orquestado con Jenkins como pilar CI/CD.

La combinación de pruebas unitarias, análisis estático y reportes visuales garantiza confianza en el software, eficiencia en validaciones y profesionalismo en despliegue continuo.

---

