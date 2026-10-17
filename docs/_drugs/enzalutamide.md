---
layout: default
title: Enzalutamide
parent: Solo Predicción del Modelo (L5)
nav_order: 255
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Enzalutamide: nueva indicación predicha, Cáncer de órgano reproductor masculino (male reproductive organ cance… (nivel de evidencia L5). Indicación original: Enzalutamida"
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Enzalutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Enzalutamida: De Cáncer de Próstata a Cáncer de Órgano Reproductor Masculino

## Resumen en Una Frase

Enzalutamida es un inhibidor de la señalización del receptor de andrógenos, originalmente utilizado para el tratamiento del cáncer de próstata avanzado.
El modelo TxGNN predice que podría ser efectivo para **cáncer de órgano reproductor masculino**, con **35 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Sin embargo, esta indicación coincide en la práctica con el uso ya establecido en cáncer de próstata, por lo que no constituye un hallazgo de reposicionamiento genuino.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enzalutamida (el registro sanitario no detalla el texto de la indicación; según la información de referencia, cáncer de próstata avanzado/resistente a la castración) |
| Nueva Indicación Predicha | Cáncer de órgano reproductor masculino (male reproductive organ cancer) |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L1 (ensayos de Fase 3 presentes, pero en la indicación ya aprobada; ver nota) |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

**Nota sobre la selección de la indicación:** El candidato con mayor puntaje TxGNN (99.71%) es "susceptibilidad a cáncer de próstata/cerebro", un concepto genético sin entidad tratable, sin ensayos ni literatura. Los demás candidatos de mayor puntaje (leiomioma de próstata, tumor de Brenner, fibroma de próstata, tumor filodes prostático benigno, neoplasia benigna del sistema reproductor) solo tienen predicción del modelo o literatura preclínica, sin ensayos. La única predicción con evidencia clínica sustancial es "cáncer de órgano reproductor masculino" (puntaje 99.51%), por lo que este informe se centra en ella.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, la enzalutamida es un inhibidor de la señalización del receptor de andrógenos (AR, gen *AR*), objetivo farmacológico que figura en los datos de interacciones. Su eficacia en cáncer de próstata avanzado (incluido el resistente a la castración, el no metastásico y el metastásico sensible a la castración) está respaldada por la referencia clínica de la base farmacológica.

El cáncer de próstata es el cáncer dominante de los órganos reproductores masculinos, y la señalización mediada por AR es su principal motor. Por ello, el modelo asocia el fármaco con esta categoría más amplia. La relación es real, pero se trata esencialmente de una reformulación de la indicación ya conocida y no de una nueva oportunidad terapéutica.

Un revisor debe confirmar si esta predicción representa una indicación nueva o simplemente la ya aprobada antes de emitir cualquier recomendación. Las demás predicciones (tumores prostáticos benignos, tumor de Brenner) carecen de respaldo mecanístico claro en los datos disponibles.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 35 registrados), priorizando los de mayor fase y relevancia directa con el fármaco.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Fase 3 | Activo, sin reclutar | 1125 | ENZAMET: enzalutamida vs. antiandrógeno no esteroideo con terapia de privación androgénica de primera línea en cáncer de próstata metastásico |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Fase 3 | Activo, sin reclutar | 600 | MEVPRO-1: mevrometostat + enzalutamida vs. enzalutamida o docetaxel en CPRCm tras abiraterona |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) | Fase 3 | Reclutando | 500 | Tratamiento estándar ± 177Lu-PSMA617 en cáncer de próstata hormonosensible metastásico; evidencia indirecta para enzalutamida |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Fase 3 | Terminado | 1244 | KEYNOTE-641: pembrolizumab + enzalutamida vs. placebo + enzalutamida en CPRCm |
| [NCT07751133](https://clinicaltrials.gov/study/NCT07751133) | Fase 3 | Reclutando | 1500 | Dosis reducidas vs. estándar de inhibidores de la vía del receptor de andrógenos en cáncer de próstata metastásico |
| [NCT06059118](https://clinicaltrials.gov/study/NCT06059118) | Fase 2 | Reclutando | 50 | Ensayo APEX: DFMO y testosterona a dosis altas en secuencia con enzalutamida en CPRCm asintomático |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Fase 2 | Aún sin reclutar | 26 | Optimización de dosis de enzalutamida en adultos mayores con cáncer de próstata avanzado |
| [NCT01547299](https://clinicaltrials.gov/study/NCT01547299) | Fase 2 | Completado | 52 | Enzalutamida neoadyuvante antes de prostatectomía en cáncer de próstata localizado |
| [NCT04332744](https://clinicaltrials.gov/study/NCT04332744) | Fase 2 | Completado | 54 | Enzalutamida + talazoparib en cáncer de próstata metastásico sensible a hormonas |
| [NCT00510718](https://clinicaltrials.gov/study/NCT00510718) | Fase 1 | Completado | 140 | Estudio de escalada de dosis, seguridad y farmacocinética de MDV3100 (enzalutamida) en CPRC |

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 20 recuperadas), priorizando ensayos clínicos y revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | Informe de ensayo clínico | N Engl J Med | Un ensayo previo mostró que añadir talazoparib a enzalutamida mejoró la supervivencia libre de progresión por imagen y la supervivencia global en cáncer de próstata metastásico |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Revisión | Trends Cancer | Avances de tratamiento en cáncer de próstata avanzado, incluidos enzalutamida y otros agentes aprobados |
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Revisión | JAMA | Revisión del diagnóstico y tratamiento del cáncer de próstata |
| [32989253](https://pubmed.ncbi.nlm.nih.gov/32989253/) | 2020 | Revisión | Oncogene | Papel de la variante AR-V7 en la resistencia a inhibidores de segunda generación del receptor de andrógenos |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Revisión | Nat Rev Urol | Plasticidad celular y fenotipo neuroendocrino como mecanismo de resistencia a abiraterona y enzalutamida |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | Preclínico/Mecanístico | Nature | La inhibición de la quimiotaxis mieloide puede revertir la resistencia al tratamiento en cáncer de próstata |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | Preclínico/Mecanístico | Nat Commun | Subpoblaciones celulares preexistentes y persistentes asociadas con recaída y resistencia a enzalutamida |
| [25151012](https://pubmed.ncbi.nlm.nih.gov/25151012/) | 2015 | Preclínico | Eur Urol | AZD5363 combinado con enzalutamida retrasa significativamente la resistencia en modelos preclínicos |
| [33542074](https://pubmed.ncbi.nlm.nih.gov/33542074/) | 2021 | Preclínico | Clin Cancer Res | La resistencia a enzalutamida se asocia con dependencia de BCL-2 e IKKB |
| [33773874](https://pubmed.ncbi.nlm.nih.gov/33773874/) | 2021 | Revisión | Eur Urol | Selección de pacientes y tratamiento del CPRCm tras docetaxel y abiraterona/enzalutamida: inhibidores de PARP vs. cabazitaxel |

## Información de Mercado en Colombia

Los cinco registros sanitarios se encuentran **cancelados**; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224710 | XTANDI® 40 MG tabletas (Astellas Pharma US) | Tableta recubierta | Enzalutamida |
| 20198992 | Enzalutamida 40 MG cápsulas blandas (Tecnoquímicas) | Cápsula blanda | Enzalutamida |
| 20199474 | ZALTRENSA® 40 MG (Dr. Reddy's Laboratories) | Cápsula blanda | Enzalutamida |
| 20178073 | XTANDI 80 MG tabletas (Astellas Pharma US) | Tableta recubierta | Enzalutamida |
| 20195068 | ENZASTIK® 40 MG cápsulas blandas (Eugia Pharma) | Cápsula blanda | Enzalutamida |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida hormonal (inhibidor del receptor de andrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para informar la seguridad.

Los datos compilados no incluyen advertencias, contraindicaciones ni interacciones farmacológicas clínicas. El único registro de interacción corresponde a la farmacología del fármaco con su blanco (receptor de andrógenos). Un ensayo de Fase 1 completado (NCT04094519) evaluó el efecto de enzalutamida sobre sustratos de P-gp y BCRP (digoxina y rosuvastatina), lo que sugiere la necesidad de revisar interacciones en la ficha técnica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existen ensayos de Fase 3 con enzalutamida, la indicación predicha es esencialmente el cáncer de próstata ya aprobado, por lo que no representa un reposicionamiento real. Además, no hay registros sanitarios vigentes en Colombia y faltan datos de seguridad y de mecanismo de acción. Las otras predicciones de alto puntaje (tumores prostáticos benignos, tumor de Brenner, susceptibilidad genética) carecen de evidencia clínica.

**Para avanzar se necesita:**
- Confirmar por revisión experta si la indicación es nueva o solo reformula la aprobada
- Obtener el prospecto de INVIMA para advertencias y contraindicaciones (brecha de datos bloqueante)
- Completar los datos de mecanismo de acción desde DrugBank
- Aclarar el estado regulatorio: motivos de cancelación de los cinco registros y posibilidad de nueva solicitud
- Si se desea explorar un reposicionamiento real, evaluar de forma separada los tumores prostáticos benignos con expresión de AR mediante estudios preclínicos o de expresión de AR
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

