---
layout: default
title: Diltiazem
parent: Solo Predicción del Modelo (L5)
nav_order: 222
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diltiazem: nueva indicación predicha, Susceptibilidad obsoleta a accidente cerebrovascular isquémico (nivel de evidencia L5). Indicación original: No especificada en el registro (solo figura el nombr…"
---

# Diltiazem
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

# Diltiazem: De Indicación No Especificada a Susceptibilidad Obsoleta a Accidente Cerebrovascular Isquémico

## Resumen en Una Frase

Diltiazem es un bloqueador de los canales de calcio no dihidropiridínico, cuyo único registro sanitario en Colombia (hoy cancelado) no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad obsoleta a accidente cerebrovascular isquémico**, un término que la ontología considera obsoleto.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (solo figura el nombre "DILTIAZEM") |
| Nueva Indicación Predicha | Susceptibilidad obsoleta a accidente cerebrovascular isquémico |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, diltiazem es un bloqueador de los canales de calcio no dihidropiridínico, y mecanísticamente podría ser aplicable al riesgo de accidente cerebrovascular isquémico.

Los vínculos plausibles, derivados de la farmacología general, incluyen la reducción de la presión arterial, la disminución del tono del músculo liso vascular y del vasoespasmo, y posibles efectos sobre la resistencia vascular cerebral y la entrada de calcio neuronal. Ninguno de estos vínculos está respaldado por evidencia en los datos disponibles.

Además, el término de la enfermedad está marcado como "obsoleto" en la ontología, es decir, es un concepto en desuso o redundante y no una entidad clínica bien definida. El puntaje alto de TxGNN (0.991) es solo una predicción del modelo y no ha sido validado con evidencia clínica ni bibliográfica.

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
| 51602 (cancelado) | DILTIAZEM TABLETAS POR 60 MG | Tableta | DILTIAZEM |

Fabricante: GENFAR S.A. Vía de administración: oral.

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG de TxGNN, no texto de prospecto):
  - Cardiovasculares: estenosis aórtica y enfermedad de la válvula aórtica, miocardiopatía hipertrófica, trastornos hipotensivos, taquicardia ventricular, bloqueo auriculoventricular, síndrome del seno enfermo, síndrome de Wolff-Parkinson-White, síndrome de Lown-Ganong-Levine, obstrucción de la arteria renal.
  - Hepáticas y renales: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, piouréter.
  - Hematológicas: neutropenia, agranulocitosis.
  - Angioedema (incluidas formas hereditarias y adquiridas).
  - Enfermedades del tejido conectivo, óseo y del cartílago.
- **Interacciones farmacológicas**: se identificaron 369 interacciones; las 20 primeras listadas corresponden a:
  - **Mayor**: loperamida.
  - **Moderadas**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida (incluida la nasal), pioglitazona, bupropión, aprepitant, morfina, ácido acetilsalicílico, canagliflozina y varias sales de calcio (fosfato, acetato, carbonato, cloruro, citrato, glubionato, glucoheptonato).

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y la enfermedad predicha es un término obsoleto. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar qué concepto clínico vigente reemplaza al término obsoleto (por ejemplo, prevención de accidente cerebrovascular isquémico) y reevaluar la predicción con él.
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Realizar una búsqueda sistemática de ensayos y literatura sobre diltiazem y prevención de ACV isquémico.
- Verificar la situación regulatoria actual del diltiazem en Colombia, ya que el registro identificado está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

