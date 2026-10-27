---
layout: default
title: Flutamide
parent: Solo Predicción del Modelo (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flutamide: nueva indicación predicha, Susceptibilidad genética a cáncer de próstata/cerebro (nivel de evidencia L5). Indicación original: Registro sanitario sin detalle de indicación (solo figura \"FL…"
monitor_inn: "Flutamide"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Flutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Flutamida: De Cáncer de Próstata Avanzado a Susceptibilidad Genética a Cáncer de Próstata/Cerebro
{: .text-alpha }

## Resumen en Una Frase

La flutamida es un antiandrógeno no esteroideo, utilizado originalmente para el cáncer de próstata localmente confinado y metastásico. El modelo TxGNN predice que podría ser efectivo para **susceptibilidad genética a cáncer de próstata/cerebro**, pero para esta predicción concreta **no hay ensayos clínicos ni publicaciones** que la respalden. Además, se trata de un fenotipo de predisposición genética, no de una indicación tratable.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Registro sanitario sin detalle de indicación (solo figura "FLUTAMIDA"). Según los datos farmacológicos, cáncer de próstata |
| Nueva Indicación Predicha | Susceptibilidad genética a cáncer de próstata/cerebro |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La flutamida es un antagonista del receptor de andrógenos (AR). Aunque no se dispone de datos detallados del mecanismo de acción en la información compilada, los datos farmacológicos confirman que actúa sobre este receptor. Bloquea la señalización de los andrógenos en los tejidos que dependen de ellos, y por eso se usa en el cáncer de próstata.

Un vínculo con el cáncer de próstata es biológicamente plausible. Sin embargo, la entrada predicha es un **fenotipo de susceptibilidad genética**, no una enfermedad con tratamiento clínico definido. Por eso el puntaje, muy alto, debe interpretarse solo como una predicción del modelo. No se identificaron estudios que evalúen la flutamida en esta condición, y la similitud con la indicación original aún no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta predicción.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta predicción.

---

## Otras Predicciones con Mayor Respaldo

Entre las 10 predicciones evaluadas, otras tienen más evidencia que la primera:

| Rango | Enfermedad Predicha | Puntaje TxGNN | Nivel | Recomendación |
|---|---|---|---|---|
| 4 | Neoplasia benigna del sistema reproductor | 99.98% | L3 | Pregunta de investigación |
| 6 | Cáncer de órganos reproductores masculinos | 99.98% | L1 | Proceed with Guardrails |
| 2, 3, 5, 7 | Fibroma de próstata, tumor de Brenner, leiomioma de próstata, tumor filodes prostático benigno | 99.98% | L5 | Hold |
| 8-10 | VIH, infección por SIV, SIDA felino | 99.86%-99.92% | L5 | Hold |

**Cáncer de órganos reproductores masculinos (rango 6):**
- Es la entrada mejor respaldada, con ensayos de Fase 2 y Fase 3.
- Incluye el ensayo de quimioprevención de Fase 2 con flutamida en neoplasia intraepitelial prostática ([NCT00006214](https://clinicaltrials.gov/study/NCT00006214), n=63, completado).
- Incluye ensayos de Fase 3 de terapia hormonal en cáncer de próstata, como [NCT00003026](https://clinicaltrials.gov/study/NCT00003026) (n=966), [NCT00002855](https://clinicaltrials.gov/study/NCT00002855) (n=306), [NCT00936390](https://clinicaltrials.gov/study/NCT00936390) (n=1538) y [NCT00003645](https://clinicaltrials.gov/study/NCT00003645) (n=64, terminado).
- Esta entrada en gran medida **describe de nuevo el uso ya establecido en cáncer de próstata**. No es un hallazgo novedoso de reposicionamiento.
- En muchos de esos ensayos de Fase 3 no está confirmado qué papel tuvo la flutamida.

**Neoplasia benigna del sistema reproductor (rango 4):**
- La evidencia es pequeña, antigua y mayormente farmacodinámica.
- Incluye un estudio en hombres con hiperplasia prostática benigna ([PMID 1722793](https://pubmed.ncbi.nlm.nih.gov/1722793/), 1991) y estudios de terapia combinada con agonista de LHRH ([PMID 1989458](https://pubmed.ncbi.nlm.nih.gov/1989458/)).

Las predicciones sobre VIH y virus de inmunodeficiencia animal no tienen un vínculo mecanístico plausible y probablemente reflejan artefactos de la red del modelo.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35440 (cancelado) | ETACONIL DE 250 MG COMPRIMIDOS | Tableta | FLUTAMIDA |

---

## Citotoxicidad

La flutamida se usa como tratamiento antineoplásico en cáncer de próstata, pero no es un citotóxico convencional.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antiandrógeno no esteroideo), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (por el riesgo de hepatotoxicidad señalado en los datos compilados); consultar el prospecto para parámetros adicionales |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Hepatotoxicidad:** los datos compilados señalan una advertencia de caja (boxed warning) por hepatotoxicidad como salvaguarda clave. Sería una preocupación adicional en poblaciones que usan fármacos de metabolismo hepático, como los antirretrovirales.
- **Condiciones asociadas a contraindicación** (grafo de conocimiento TxGNN/PrimeKG, no texto del prospecto):
  - insuficiencia hepática y enfermedad hepática
  - enfermedad de la vesícula biliar
  - metahemoglobinemia (incluida la causada por deficiencia de metahemoglobina reductasa) y sulfohemoglobinemia
  - hiperbilirrubinemia, hiperbilirrubinemia hereditaria y síndrome de Gilbert
  - deficiencia de G6PD
  - enfermedad por depósito de glucógeno
  - cistinuria
  - galactosemia
  - deficiencia de piruvato deshidrogenasa E3
- **Interacciones farmacológicas:** la consulta no devolvió interacciones medicamentosas clínicas. Solo muestra la unión de la flutamida a su diana, el receptor de andrógenos (AR).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción principal es un fenotipo de susceptibilidad genética, no una indicación tratable, y no tiene ensayos ni literatura. El respaldo es solo el puntaje del modelo (L5).
- Además, el único registro sanitario en Colombia está cancelado, existe un riesgo de hepatotoxicidad y hay antiandrógenos más nuevos como bicalutamida y enzalutamida.

**Para avanzar se necesita:**
- Definir si la entrada "susceptibilidad a cáncer de próstata/cerebro" corresponde a una indicación clínicamente abordable.
- Si se quiere continuar, reorientar la evaluación hacia la predicción de cáncer de órganos reproductores masculinos (rango 6, L1). Para ello hay que verificar cuáles ensayos usaron flutamida realmente y tener presente que esa evidencia describe un uso ya establecido.
- Obtener el prospecto con advertencias y contraindicaciones oficiales, un vacío de información que bloquea el tamizaje de seguridad.
- Obtener datos detallados del mecanismo de acción.
- Evaluar la viabilidad regulatoria, dado que el estado de mercado es "solo cancelado", y comparar con alternativas antiandrogénicas disponibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

