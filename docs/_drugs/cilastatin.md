---
layout: default
title: Cilastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatina: De Imipenem/Cilastatina a Neumonía (Indicación Predicha de Mayor Evidencia)

## Resumen en Una Frase

La cilastatina es un inhibidor de la dehidropeptidasa-I renal que se administra junto con el antibiótico imipenem, y los registros sanitarios colombianos la listan como "imipenem y cilastatina".
El modelo TxGNN predice que podría ser efectiva para **neumonía**, con **11 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Importante: esta evidencia corresponde al uso de la combinación (el efecto antibacteriano proviene del imipenem), no a un reposicionamiento de la cilastatina sola.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Imipenem y cilastatina (el registro no detalla indicaciones clínicas específicas) |
| Nueva Indicación Predicha | Neumonía (la predicción de mayor puntaje, *S. aureus*, tiene evidencia más débil: L3) |
| Puntaje de Predicción TxGNN | 99.81% (neumonía); 99.94% para infección por *Staphylococcus aureus* |
| Nivel de Evidencia | L1 (neumonía) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, la cilastatina inhibe la dehidropeptidasa-I en los túbulos renales, lo que evita que el imipenem se degrade y mantiene sus concentraciones activas. La cilastatina no tiene actividad antibacteriana propia.

La neumonía (especialmente la nosocomial y la asociada a ventilador) es una infección bacteriana en la que el imipenem/cilastatina ya es una opción establecida. Por eso la predicción es coherente con el uso conocido de la combinación, aunque no constituye un reposicionamiento novedoso de la cilastatina sola.

Las otras predicciones (sinusitis, bronquitis, salmonelosis, infección por *S. aureus*) también dependen de la actividad del imipenem. Las predicciones sobre neoplasia de senos paranasales y esclerodermia difusa no tienen respaldo mecanístico ni evidencia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Completado | 537 | Imipenem/cilastatina/relebactam vs piperacilina/tazobactam en neumonía nosocomial o asociada a ventilador; objetivo de no inferioridad en mortalidad |
| [NCT05204563](https://clinicaltrials.gov/study/NCT05204563) | Fase 3 | Completado | 450 | Imipenem/cilastatina/XNW4107 vs imipenem/cilastatina/relebactam en neumonía nosocomial o asociada a ventilador |
| [NCT00080496](https://clinicaltrials.gov/study/NCT00080496) | Fase 3 | Completado | 430 | Tigeciclina vs imipenem/cilastatina en neumonía nosocomial |
| [NCT00589693](https://clinicaltrials.gov/study/NCT00589693) | Fase 3 | Terminado | 274 | Doripenem vs imipenem/cilastatina en neumonía asociada a ventilador; terminado anticipadamente |
| [NCT03894046](https://clinicaltrials.gov/study/NCT03894046) | Fase 3 | Completado | 207 | Sulbactam-durlobactam en infecciones por *Acinetobacter*; imipenem/cilastatina como terapia de base |
| [NCT00515034](https://clinicaltrials.gov/study/NCT00515034) | Fase 2 | Completado | 146 | Doripenem vs imipenem en neumonía asociada a ventilador o infección intraabdominal complicada |
| [NCT00445094](https://clinicaltrials.gov/study/NCT00445094) | Fase 4 | Completado | 120 | Estrategia de desescalamiento antibiótico en neumonía en UCI médica |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Fase 2 | Terminado | 108 | Dos dosis de tigeciclina vs imipenem/cilastatina en neumonía hospitalaria |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Desconocido | 60 | Linezolid solo o con carbapenem contra SARM en neumonía asociada a ventilador; sin resultados confirmados |
| [NCT05561764](https://clinicaltrials.gov/study/NCT05561764) | Fase 4 | Terminado | 4 | Farmacocinética de imipenem/cilastatina/relebactam en fibrosis quística; solo 4 participantes |

En la mayoría de estos ensayos, el imipenem/cilastatina actúa como comparador o terapia de base; solo algunos evalúan combinaciones que lo contienen como fármaco en estudio. Hay un ensayo adicional de fase 1 sobre bacteriófagos con relevancia baja, omitido de la tabla.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECA | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatina/relebactam vs piperacilina/tazobactam en neumonía nosocomial/asociada a ventilador |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECA (Fase 3) | Int J Infect Dis | Estudio de no inferioridad de imipenem/cilastatina/relebactam vs piperacilina/tazobactam en neumonía nosocomial |
| [37182534](https://pubmed.ncbi.nlm.nih.gov/37182534/) | 2023 | ECA (Fase 3) | Lancet Infect Dis | Sulbactam-durlobactam vs colistina (ATTACK), con imipenem-cilastatina como terapia de base |
| [30509675](https://pubmed.ncbi.nlm.nih.gov/30509675/) | 2018 | ECA (Fase 2) | Lancet Infect Dis | Cefiderocol vs imipenem-cilastatina en infección urinaria complicada |
| [17488146](https://pubmed.ncbi.nlm.nih.gov/17488146/) | 2007 | Revisión | Drugs | Revisión comparativa de carbapenémicos; la cilastatina inhibe la DHP-1 |
| [36522272](https://pubmed.ncbi.nlm.nih.gov/36522272/) | 2023 | Guía de consenso | Enferm Infecc Microbiol Clin | Consenso SEIMC sobre infecciones por bacterias gramnegativas resistentes a carbapenémicos |
| [8543488](https://pubmed.ncbi.nlm.nih.gov/8543488/) | 1995 | Estudio clínico aleatorizado | J Antimicrob Chemother | Meropenem vs imipenem/cilastatina en exacerbaciones de EPOC |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Estudio clínico | Antimicrob Agents Chemother | Imipenem-cilastatina en 23 pacientes con infecciones por SARM y SASM |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Comentario de caso | Antimicrob Agents Chemother | Imipenem/cilastatina más fosfomicina en infección refractaria por SARM |
| [3859208](https://pubmed.ncbi.nlm.nih.gov/3859208/) | 1985 | Estudio abierto | Am J Med | Imipenem/cilastatina en 43 adultos con neumonía bacteriana |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20256282 | Imipenem+Cilastatina 500+500 mg polvo para reconstituir | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |
| 20134454 | Imipenem/Cilastatina polvo para reconstituir a solución inyectable | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |
| 19982795 | Imipenem y Cilastatina 1 g | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |

Los tres registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones/farmacología**: la cilastatina inhibe la dipeptidasa 1 (dehidropeptidasa-I) y se administra en dosis fijas con imipenem para aumentar su eficacia.
- **Reportes de literatura**: se describió un caso de vasculitis leucocitoclástica asociada a imipenem-cilastatina (PMID 9158321).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (para neumonía)

**Justificación:**
Varios ensayos de fase 3 completados respaldan combinaciones con imipenem/cilastatina en neumonía nosocomial y asociada a ventilador. Sin embargo, es un uso ya existente de la combinación y el beneficio proviene del imipenem, no de la cilastatina sola. Las demás predicciones (sinusitis, bronquitis, salmonelosis, *S. aureus*) tienen evidencia indirecta o antigua (L3-L4) y quedan como preguntas de investigación o en espera; las de baja evidencia (rinosinusitis crónica, sinusitis etmoidal, paratifoidea, neoplasia sinusal, esclerodermia difusa) deben mantenerse en Hold.

**Para avanzar se necesita:**
- Verificar en los registros completos si los ensayos NCT05204563 y NCT02493764 incluyen realmente imipenem/cilastatina como fármaco en estudio.
- Obtener los datos de advertencias y contraindicaciones del prospecto de INVIMA.
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria, ya que los tres registros colombianos están cancelados.
- Definir si el interés está en la combinación o en la cilastatina sola, dado que esta carece de actividad antibacteriana propia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

