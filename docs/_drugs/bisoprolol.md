---
layout: default
title: Bisoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 93
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bisoprolol: De Hipertensión, Angina e Insuficiencia Cardíaca a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Bisoprolol es un bloqueador beta-1 selectivo, usado para tratar hipertensión, angina crónica estable y algunas formas de insuficiencia cardíaca crónica estable. En Colombia se registra como combinación con tiazidas.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.
Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bisoprolol y tiazidas (texto del registro INVIMA) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, bisoprolol actúa sobre el receptor β1-adrenérgico (gen ADRB1), y su eficacia en hipertensión ha sido comprobada. Mecanísticamente, al bloquear ese receptor reduce la presión arterial y la liberación de renina, lo que podría ser aplicable a la hipertensión renovascular.

Sin embargo, la hipertensión maligna es una emergencia hipertensiva que normalmente se maneja con fármacos parenterales. Los datos disponibles no muestran que un bloqueador beta oral como bisoprolol tenga un papel en ese escenario. Si hubiera beneficio, sería un efecto indirecto sobre la presión arterial, no un mecanismo específico de la enfermedad.

Además, no hay indicaciones originales estructuradas ni datos de mecanismo de acción en el paquete, por lo que el puntaje no puede contrastarse con la indicación aprobada.

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
| 202329 | ZIAC ® 10 MG (MERCK S.A.) | Tableta recubierta | Bisoprolol y tiazidas |

El paquete de evidencia reporta 20 registros sanitarios en total. Las cinco entradas suministradas corresponden al mismo registro (202329) repetido, por lo que se muestra una sola vez. La vía de administración disponible es oral.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se reportan interacciones con otros fármacos. El único registro corresponde a la diana farmacológica del bisoprolol, el receptor β1-adrenérgico (ADRB1, humano). No hay datos públicos de bioactividad frente a esta diana.
- **Punto de atención**: aunque bisoprolol es β1-selectivo, el bloqueo beta en enfermedad pulmonar con hipoxia plantea un riesgo de broncoconstricción. Esto aplica a otras predicciones de la lista.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, y la plausibilidad mecanística es limitada porque la hipertensión maligna se maneja habitualmente con terapia parenteral. Las otras cuatro predicciones (enfermedad renal hipertensiva maligna, dos formas de hipertensión pulmonar y síndrome de Braddock) también están en nivel L5 y en Hold.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío que bloquea el tamizaje de seguridad.
- Consultar el mecanismo de acción en DrugBank (DB00612) y las indicaciones originales estructuradas.
- Hacer una búsqueda bibliográfica dirigida de bisoprolol o bloqueadores beta en hipertensión renovascular o maligna.
- Definir si un fármaco oral tiene sentido clínico en este contexto, dado que el tratamiento habitual es parenteral.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

