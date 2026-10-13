---
layout: default
title: Haloperidol
parent: Solo Predicción del Modelo (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Haloperidol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Haloperidol: De Indicación Registrada Sin Especificar a Trastorno Congénito de la Glicosilación con Fucosilación Defectuosa

## Resumen en Una Frase

Haloperidol es un antipsicótico que actúa bloqueando los receptores de dopamina D2. En los registros sanitarios colombianos su indicación figura solo con el nombre del fármaco, sin detalle clínico. El modelo TxGNN predice que podría ser efectivo para el **trastorno congénito de la glicosilación con fucosilación defectuosa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto registrado es solo "Haloperidol"); el fármaco es un antipsicótico antagonista D2 |
| Nueva Indicación Predicha | Trastorno congénito de la glicosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 6 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en la información compilada para este informe. Según el análisis realizado, haloperidol es un antagonista de los receptores dopaminérgicos D2, y esa es la base de su uso como antipsicótico.

Con los datos disponibles **no se identifica un vínculo mecanístico plausible** entre el bloqueo dopaminérgico D2 y los defectos de fucosilación que caracterizan esta enfermedad. El puntaje alto del modelo (99.91%) refleja una asociación estadística dentro del grafo de conocimiento, no un mecanismo validado. No existe evidencia experimental ni clínica que la sustente.

Por ello, esta predicción debe leerse como una hipótesis computacional sin respaldo, no como una oportunidad de reposicionamiento fundamentada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los 6 registros sanitarios encontrados están **cancelados**. No hay ningún registro vigente.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19929092 | Haloperidol Solución Inyectable | Solución inyectable | Haloperidol |
| 19999331 | Haloperidol Solución Oral 2 mg/mL | Solución oral | Haloperidol |
| 20118490 | Apracal Gotas | Solución oral | Haloperidol |
| 19940401 | Haloperidol Tabletas 10 mg | Tableta | Haloperidol |
| 11416 | Haloperidol 10 mg Tabletas Recubiertas | Tableta recubierta | Haloperidol |

Hay un sexto registro cancelado (45922, Apracal 5 mg tabletas), que no se lista por el límite de 5 filas.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo de TxGNN, no texto del prospecto):
  - Cardiovasculares: síndrome de QT largo (incluida la forma familiar), torsades de pointes, trastornos hipotensivos.
  - Neurológicas: epilepsia, enfermedad de los ganglios basales, distonía focal de la mano, blefaroespasmo, síndrome neuroléptico maligno.
  - Hematológicas: neutropenia (incluidas múltiples formas congénitas), agranulocitosis, leucopenia, hematopoyesis cíclica.
  - Hepáticas y biliares: enfermedad hepática, enfermedad de la vesícula biliar.
  - Endocrinas y metabólicas: hipotiroidismo, mixedema, hipotiroidismo congénito, deficiencia de potasio.
  - Oncológicas: carcinoma de mama femenino.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel **mayor** destacan:
  - Bupropión.
  - Morfina.
  - Claritromicina.
  - Dolasetrón.

  Entre las de nivel **moderado** figuran famotidina, epinefrina, hidrocortisona, anfotericina B, atropina, loperamida y aprepitant, entre otras. Las interacciones con prolongación del QT y con depresores del sistema nervioso central requieren especial atención.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico identificable. Además, el fármaco no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen una relación biológica con la fucosilación defectuosa.
- Estudios preclínicos que respalden la hipótesis.
- Obtención y análisis del prospecto (advertencias y contraindicaciones oficiales) para el cribado de seguridad.
- Confirmación de si existe una formulación vigente y disponible en Colombia.

**Nota complementaria:** entre las otras predicciones del modelo, la indicación **trastorno bipolar afectivo maníaco** sí cuenta con evidencia sólida: ensayos de Fase 3 con haloperidol como comparador activo y metaanálisis en red de ECAs (nivel L1, "Proceed with Guardrails"). Sin embargo, se trata de un uso establecido o muy cercano a la indicación original, no de un reposicionamiento novedoso. De avanzarse por esa vía, las salvaguardas serían:
- Monitoreo de ECG y QTc.
- Vigilancia de síntomas extrapiramidales.
- Cribado de interacciones.
- Confirmación de una formulación disponible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

