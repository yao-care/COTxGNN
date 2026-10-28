---
layout: default
title: Meloxicam
parent: Solo Predicción del Modelo (L5)
nav_order: 425
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Meloxicam: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Meloxicam"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Meloxicam: De Indicación Registrada (Meloxicam) a Displasia acromesomélica, tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) con registros sanitarios en Colombia, cuyo texto de indicación aprobada solo menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Meloxicam (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, meloxicam es un AINE con preferencia por la inhibición de COX-2, que reduce la inflamación y el dolor mediada por prostaglandinas.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético genético raro, causado por mutaciones en CDMP1/GDF5, que afecta el crecimiento óseo. No se identifica un vínculo mecanístico plausible entre la inhibición de COX y los defectos de la señalización de GDF5. El puntaje alto del modelo parece reflejar cercanía en la red de conocimiento y no una justificación biológica.

**Otras predicciones del modelo (también sin respaldo clínico, salvo una con evidencia indirecta):**
- **Espondiloartropatía (susceptibilidad):** es la más plausible biológicamente, porque los AINE son tratamiento de primera línea en espondiloartritis. Sin embargo, no sería un reposicionamiento novedoso y no hay evidencia en los datos compilados.
- **Artritis idiopática juvenil poliarticular FR-positiva:** cuenta con una publicación indirecta sobre seguridad de AINE en AIJ (nivel L4).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

*Referencia indirecta (para la predicción de AIJ poliarticular FR-positiva, no para la indicación principal):*

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Estudio de seguridad (registro Fase 4) | Pediatric Rheumatology Online Journal | Evalúa la seguridad a largo plazo y datos de desarrollo en pacientes con AIJ tratados con celecoxib o AINE no selectivos; no es específico de meloxicam |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19986264 | MEPROGAL 15MG TABLETA | Tableta | MELOXICAM | Vigente |
| 227880 | ARTRICLOX 15 MG TABLETAS | Tableta | MELOXICAM | Vigente |
| 53916 | MELCOX 7.5 MG TABLETAS | Tableta | MELOXICAM | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no del prospecto):** hipertensión, enfermedad renal e insuficiencia renal, insuficiencia cardíaca congestiva, enfermedad cardiovascular, infarto de miocardio, trombosis coronaria, accidente cerebrovascular e infarto cerebral, úlcera péptica activa, gastritis, trastornos de la coagulación, diabetes mellitus y cetoacidosis diabética, hiperlipidemia (incluida la familiar), anemia (incluida la macrocítica), hemoglobinopatías y abuso/dependencia de sustancias.
- **Interacciones farmacológicas (100 registradas; se destacan algunas):**
  - Moderadas: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), ácido acetilsalicílico, mesalazina, balsalazida, metformina, antidiabéticos sulfonilureicos (glimepirida, clorpropamida), aprepitant, vancomicina, kanamicina, sales de potasio (citrato y bicarbonato) y laxantes/preparaciones intestinales (ácido picosulfúrico, polietilenglicol, sulfato de sodio).
  - Menor: linaclotida.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no cuenta con ensayos clínicos ni literatura, carece de un vínculo mecanístico plausible (trastorno genético del crecimiento óseo vs. inhibición de COX) y, aunque el medicamento está comercializado en Colombia con 3 registros sanitarios vigentes, el puntaje alto de TxGNN (modelo de aprendizaje profundo) por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción del fármaco (dato faltante) y evaluar cualquier vínculo con la vía GDF5/CDMP1.
- Obtener el prospecto de INVIMA para completar las advertencias y contraindicaciones.
- Aclarar la situación regulatoria: el medicamento está comercializado en Colombia con 3 registros vigentes.
- Si se busca una línea más viable, priorizar la revisión de literatura sobre espondiloartropatía y AIJ, donde los AINE tienen un fundamento clínico establecido (aunque no sería un reposicionamiento novedoso).
- Estudios preclínicos o de mecanismo si se desea explorar la indicación de displasia acromesomélica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

