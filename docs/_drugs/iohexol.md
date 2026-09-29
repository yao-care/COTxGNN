---
layout: default
title: Iohexol
parent: Solo Predicción del Modelo (L5)
nav_order: 227
evidence_level: L5
indication_count: 2
---

# Iohexol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Iohexol: De Medio de Contraste Radiográfico a Insomnio

## Resumen en Una Frase

Iohexol es un medio de contraste radiográfico yodado no iónico, usado como ayuda para obtener imágenes diagnósticas.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción es solo computacional y no tiene sustento mecanístico ni clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IOHEXOL (el texto del registro solo repite el nombre del principio activo; por su naturaleza, medio de contraste radiográfico) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, iohexol es un agente de contraste yodado no iónico, farmacológicamente inerte, que no tiene actividad conocida sobre receptores del sistema nervioso central. DrugBank tampoco lista indicaciones originales para este fármaco.

Por ello, **no se identifica un vínculo mecanístico** entre iohexol y el insomnio, ni una vía relacionada con el sueño. El puntaje de 99.87% proviene únicamente de asociaciones del grafo de conocimiento y no de un efecto farmacológico demostrado. La relación entre la indicación original (diagnóstico por imagen) y el insomnio (trastorno del sueño) es inexistente desde el punto de vista terapéutico.

Un puntaje alto en TxGNN no equivale a plausibilidad biológica. Sin evidencia adicional, esta predicción debe considerarse probablemente un artefacto del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20139023 | IOHEXOL INYECCION 300MG/ML (Unique Pharmaceutical Laboratories) | Solución inyectable | IOHEXOL |

Nota: los datos reportan 6 registros sanitarios en total, pero el detalle disponible muestra un único número de registro (20139023), repetido. Aquí se presenta una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde el uso de iohexol en insomnio, y no hay mecanismo plausible: es un agente de contraste inerte. La predicción (nivel L5) se basa solo en el modelo.

También se evaluó la segunda predicción del modelo, **ansiedad** (puntaje 99.25%). Los 5 ensayos y 6 publicaciones recuperados mencionan iohexol solo como marcador de tasa de filtración glomerular, contraste procedimental o contexto de efectos adversos, y ninguno evalúa iohexol como tratamiento. Tampoco sustenta un reposicionamiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Consultar DrugBank para obtener el mecanismo de acción.
- Identificar alguna hipótesis biológica que conecte iohexol con el sueño. Sin ella, se recomienda no invertir más recursos en esta predicción.
- Verificar el conteo y el detalle de los 6 registros sanitarios en INVIMA.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

