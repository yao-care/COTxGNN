---
layout: default
title: Lovastatin
parent: Evidencia Moderada (L3-L4)
nav_order: 267
evidence_level: L3
indication_count: 6
---

# Lovastatin
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **6** 
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

# Lovastatina: De Hipercolesterolemia y Dislipidemia Mixta a Hipercolesterolemia Familiar Homocigota

## Resumen en Una Frase

Lovastatina es una estatina (inhibidor de la HMG-CoA reductasa) usada para tratar la hipercolesterolemia y la dislipidemia mixta. El modelo TxGNN predice que podría ser efectiva para la **hipercolesterolemia familiar homocigota (HoFH)**. La respaldan **3 ensayos clínicos de Fase 3 y 19 publicaciones**, pero ningún ensayo evalúa lovastatina directamente y los reportes propios de lovastatina son pequeños y antiguos (1986-1991).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo indica "LOVASTATINA", sin texto de indicación. Según la farmacología: hipercolesterolemia y dislipidemia mixta |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Lovastatina inhibe la enzima HMG-CoA reductasa (HMGCR), lo que reduce la síntesis hepática de colesterol y aumenta la expresión del receptor de LDL (LDLR). La base de datos farmacológica también registra el receptor X de pregnano (PXR, gen NR1I2) como blanco. El campo de mecanismo de acción del Evidence Pack está vacío, así que esta descripción se apoya en esos datos y en el análisis de razonabilidad de la predicción.

La HoFH es una forma grave de hipercolesterolemia, causada por mutaciones en ambos alelos del LDLR. Tiene una relación directa con la indicación original: en ambas el problema central es el colesterol LDL elevado. Por eso el puntaje del modelo es muy alto.

Sin embargo, el beneficio de una estatina en HoFH depende de la actividad residual del LDLR. Los reportes propios de lovastatina apuntan en esa dirección:

- En niños con HoFH receptor-negativo (PMID 3397806), lovastatina no redujo el LDL-C.
- En un caso de HoFH tras trasplante hepático (PMID 3534334), se logró normalizar el colesterol, pero con receptor parcialmente restaurado.
- En dos pacientes con HoFH (PMID 1785747), se usó lovastatina combinada con probucol y colestiramina.

Además, lovastatina no es una opción de primera línea en HoFH frente a estatinas de alta potencia y terapias más nuevas.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de 24 meses de seguridad de ezetimiba añadida a atorvastatina o simvastatina en HoFH. No evalúa lovastatina |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Alirocumab (inhibidor de PCSK9) en niños y adolescentes con HoFH. Mecanismo distinto; no evalúa lovastatina |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimiba añadida a atorvastatina o simvastatina en HoFH. No evalúa lovastatina |

Los tres ensayos solo aportan contexto de la enfermedad; ninguno prueba lovastatina.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | ECA | Circulation | Ezetimiba con atorvastatina o simvastatina en 50 pacientes con HoFH. No es de lovastatina |
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Estudio clínico | J Pediatr | Tres niños con HoFH receptor-negativo tratados con lovastatina (2 mg/kg/día): sin descenso del LDL-C |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Estudio clínico | An Esp Pediatr | Lovastatina con probucol y colestiramina en dos pacientes con HoFH; relaciona el receptor de LDL con la respuesta |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Reporte de caso | JAMA | Niña con HoFH tras trasplante hepático; con lovastatina alcanzó colesterol normal |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Reporte de caso (según el resumen) | An Esp Pediatr | Respuesta a colestiramina más lovastatina en un paciente con HoFH con receptor defectuoso |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Reporte de caso (según el resumen) | Eur J Pediatr | Niña de 7 años con HoFH tratada con aféresis de LDL (HELP), con y sin lovastatina |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Revisión | Ann N Y Acad Sci | Tratamientos farmacológicos y quirúrgicos de la dislipidemia pediátrica, incluida lovastatina |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Revisión | Am J Cardiovasc Drugs | Revisión de ezetimiba como inhibidor de la absorción de colesterol |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Revisión | Clin Ther | Rosuvastatina en hiperlipidemia, con indicación en HoFH |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohorte | Arterioscler Thromb Vasc Biol | Variabilidad de la expresión del LDLR en HoFH y su efecto sobre la respuesta a evolocumab |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38340 | LOVASTATINA 20 MG TABLETAS (TECNOQUÍMICAS S.A., planta Yumbo) | Tableta | LOVASTATINA (sin texto de indicación detallado) |

Los 5 registros listados en los datos son entradas repetidas del mismo número de registro (38340). El total informado es de 20 registros sanitarios. La única vía de administración es la oral.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo devolvió datos farmacológicos de blancos moleculares: HMG-CoA reductasa (HMGCR) y receptor X de pregnano (NR1I2). No son interacciones clínicas confirmadas con otros medicamentos.

Los datos de advertencias y contraindicaciones no están disponibles. Consultar el prospecto de INVIMA para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje TxGNN es muy alto, pero ningún ensayo prueba lovastatina en HoFH. La evidencia propia de lovastatina se limita a estudios pequeños y antiguos, y sugiere respuesta débil o nula en pacientes receptor-negativo.
- Lovastatina no es de primera línea en HoFH frente a estatinas de alta potencia y agentes nuevos.
- Para hipercolesterolemia familiar (heterocigota) y para hiperlipoproteinemia, el Evidence Pack asigna nivel L2 y "Proceed with Guardrails". Son direcciones con mejor respaldo que la HoFH.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias, contraindicaciones e indicación aprobada exacta).
- Estudios de lovastatina en HoFH estratificados por genotipo del LDLR (receptor-negativo frente a defectuoso).
- Comparación frente a estatinas de alta potencia y terapias no estatínicas actuales.
- Datos de mecanismo de acción completos desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

