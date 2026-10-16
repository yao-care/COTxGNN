---
layout: default
title: Flucytosine
parent: Solo Predicción del Modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Flucytosine: nueva indicación predicha, Enfermedad ósea de Paget (nivel de evidencia L5). Indicación original: FLUCITOSINA"
monitor_inn: "flucytosine"
predicted_indications: ["bone Paget disease"]
---

# Flucytosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Flucitosina: De Indicación Original (FLUCITOSINA) a Enfermedad Ósea de Paget

## Resumen en Una Frase

Flucitosina es un antimicótico que en Colombia contaba con un registro sanitario (ANCOTOSIN®) cuya indicación aprobada figura únicamente como "FLUCITOSINA".
El modelo TxGNN predice que podría ser efectivo para la **enfermedad ósea de Paget**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLUCITOSINA (el texto del registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Enfermedad ósea de Paget |
| Puntaje de Predicción TxGNN | 99.04% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la flucitosina es un profármaco antimicótico: la citosina desaminasa fúngica la convierte en 5-fluorouracilo, que inhibe la síntesis de ADN y ARN del hongo. Su eficacia se asocia a infecciones fúngicas, no a enfermedades óseas.

La enfermedad ósea de Paget se caracteriza por una actividad osteoclástica desregulada y un recambio óseo aumentado, con factores genéticos como variantes de SQSTM1. Nada en los datos disponibles conecta la flucitosina con estas vías. No se identificó un vínculo mecanístico establecido entre la indicación original y la nueva.

Cualquier justificación posible (por ejemplo, efectos de metabolitos tipo 5-FU sobre células en proliferación) sería especulativa. El puntaje alto de TxGNN (0.990) es una predicción derivada del modelo y no está respaldado por evidencia clínica ni bibliográfica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20135088 (cancelado) | ANCOTOSIN® | Cápsula dura | FLUCITOSINA |

El fabricante es Global Service Pharmaceutical S.A.S. No hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la flucitosina con contraindicación en:
  - Enfermedad renal y piouréter
  - Enfermedad hepática y enfermedad de la vesícula biliar
  - Trombocitopenia, leucopenia, agranulocitosis y neutropenia (incluidas diversas formas congénitas, constitucionales e idiopáticas del adulto)
  - Anemia aplásica (adquirida y otras formas)
  - Hematopoyesis cíclica
  - Deficiencia de potasio
- **Interacciones farmacológicas**: se registraron 85 interacciones, de las cuales se muestran 20. Casi todas son de nivel moderado:
  - Anfotericina B (incluidas las formulaciones lipídicas, de sulfato de colesterilo y liposomal)
  - Aminoglucósidos y otros antibióticos: vancomicina, kanamicina, neomicina, estreptomicina, polimixina B, bacitracina
  - Mesalazina, balsalazida, olsalazina y sulfasalazina
  - Deferasirox, pentamidina, ibuprofeno, yobenguano (I-131) y cloruro de estroncio Sr-89
  - **Deferiprona**: interacción de nivel **mayor**, la de mayor gravedad en la lista mostrada.

Las advertencias principales y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible con la enfermedad ósea de Paget. Además, el único registro sanitario local está cancelado y el perfil de seguridad sugiere riesgos hematológicos, renales y hepáticos relevantes.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), ya que su ausencia bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y ensayos que relacionen la flucitosina o el 5-FU con la enfermedad ósea de Paget.
- Evaluar estudios preclínicos que respalden un posible mecanismo antes de reconsiderar la candidatura.
- Aclarar la indicación clínica real del producto y su situación regulatoria (registro cancelado) si se contempla uso en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

