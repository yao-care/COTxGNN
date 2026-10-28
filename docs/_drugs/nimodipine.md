---
layout: default
title: Nimodipine
parent: Solo Predicción del Modelo (L5)
nav_order: 468
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Nimodipine: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L5). Indicación original: NIMODIPINA"
monitor_inn: "nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Nimodipino: De Nimodipino (indicación no detallada en el registro) a Hipercolesterolemia Familiar Homocigota
{: .text-alpha }

## Resumen en Una Frase

Nimodipino es un bloqueador de los canales de calcio tipo L (dihidropiridina) con actividad preferente sobre la circulación cerebral, y sus registros sanitarios en Colombia solo indican "NIMODIPINA" como indicación, sin mayor detalle.
El modelo TxGNN predice que podría ser efectivo para **hipercolesterolemia familiar homocigota**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NIMODIPINA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 0.9929 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, nimodipino es una dihidropiridina que bloquea los canales de calcio tipo L, con actividad preferente en los vasos cerebrales.

La hipercolesterolemia familiar homocigota, en cambio, se origina por defectos en la vía del receptor de LDL (genes LDLR, APOB, PCSK9, LDLRAP1), que producen niveles muy elevados de colesterol LDL. **No existe un vínculo mecanístico clínicamente establecido** entre ambas condiciones. Algunos bloqueadores de los canales de calcio han mostrado efectos menores e inconsistentes sobre el metabolismo lipídico o la progresión de la aterosclerosis en contextos preclínicos u observacionales, pero esto no corrige el defecto genético de fondo.

El puntaje alto de TxGNN (0.9929) proviene únicamente de una predicción del modelo TxGNN (aprendizaje profundo) y no está respaldado por ningún ensayo ni publicación recuperados.

Como segunda predicción, el modelo propone el **síndrome nefrogénico de antidiuresis inapropiada** (puntaje 0.9905). Existe una conexión teórica a través de la señalización del calcio posterior al receptor V2, pero no hay evidencia de que nimodipino actúe sobre esa vía de forma terapéuticamente útil. Es una enfermedad extremadamente rara, lo que dificulta generar evidencia clínica. También tiene nivel L5 y recomendación Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19907710 | NISOM® 30 MG TABLETAS RECUBIERTAS | Tableta recubierta | NIMODIPINA | Vigente |
| 19966420 | NIMODIPINO 30MG TABLETAS | Tableta recubierta | NIMODIPINA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar y trastornos hipotensivos.
- **Interacciones Farmacológicas**: se identificaron 147 interacciones en total. Entre las listadas, las de nivel **mayor** son:
  - Claritromicina
  - Dolasetrón

  Otras de nivel **moderado** incluyen bupropión, aprepitant, morfina, ácido acetilsalicílico, cimetidina, miconazol, sulfato de magnesio, canagliflozina, dapagliflozina, empagliflozina, dronabinol, nabilona, kanamicina, neomicina y varias sales de calcio (fosfato, acetato, carbonato y cloruro).

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con respaldo computacional (nivel L5), sin ensayos clínicos ni publicaciones, y no hay un vínculo mecanístico clínicamente establecido entre el bloqueo de canales de calcio y los defectos genéticos de la vía del receptor de LDL. Además, ambos registros sanitarios en Colombia están cancelados, y existen opciones terapéuticas establecidas para esta enfermedad.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de nimodipino y un análisis de su vínculo mecanístico con la nueva indicación
- Estudios preclínicos que muestren un efecto de nimodipino sobre el metabolismo lipídico o la vía del LDL
- Advertencias y contraindicaciones del prospecto de INVIMA (hoy no disponibles)
- Aclarar la situación regulatoria, dado que no hay registros vigentes en Colombia
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (pendientes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

