---
layout: default
title: Atorvastatin
parent: Evidencia Alta (L1-L2)
nav_order: 62
evidence_level: L1
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **6** 
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

# Atorvastatina: De Hipercolesterolemia a Hipercolesterolemia Familiar

## Resumen en Una Frase

Atorvastatina es una estatina (inhibidor de la HMG-CoA reductasa) que se usa para reducir el colesterol en hipercolesterolemia y dislipidemia mixta.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**, con **35 ensayos clínicos** y **19 publicaciones** asociados. Varios de esos ensayos usan atorvastatina como tratamiento de base y no como único fármaco evaluado.
Esta predicción coincide con un uso ya establecido de la atorvastatina, por lo que no es un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro INVIMA solo dice «ATORVASTATIN» (nombre del principio activo, sin indicación redactada). La ficha farmacológica describe hipercolesterolemia y dislipidemia mixta |
| Nueva Indicación Predicha | Hipercolesterolemia familiar |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 17 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No hay una descripción detallada del mecanismo de acción en DrugBank. Sin embargo, el registro farmacológico identifica su diana: la enzima HMG-CoA reductasa (gen *HMGCR*). Al inhibirla, disminuye la síntesis hepática de colesterol y aumentan los receptores de LDL en el hígado, lo que reduce el colesterol LDL (LDL-C).

La hipercolesterolemia familiar (HF) se caracteriza por LDL-C muy elevado debido a defectos genéticos en el receptor de LDL. En la forma heterocigota, el receptor conserva función parcial, y por eso las estatinas funcionan. En la forma homocigota, o cuando el receptor es nulo, la respuesta es menor y casi siempre se necesitan terapias adicionales (ezetimiba, inhibidores de PCSK9, inhibidores de CETP en estudio, entre otras).

Conviene aclarar que el uso de atorvastatina en HF ya está establecido. El campo de indicaciones originales llegó vacío por una brecha de datos, y eso hace que parezca una predicción nueva. La evidencia respalda sobre todo el uso en HF heterocigota y en poblaciones pediátricas.

---

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 35 ensayos, priorizando los más relevantes para HF. En varios, la atorvastatina es tratamiento de base y el fármaco evaluado es otro. El proyecto de torcetrapib se suspendió el 2 de diciembre de 2006 por hallazgos de seguridad.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimiba añadida a atorvastatina o simvastatina en HF homocigota. La evidencia respalda la combinación, no la atorvastatina sola |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Fase 3 | Completado | 400 | Torcetrapib/atorvastatina frente a atorvastatina sola (dosis máxima tolerada) durante 6 meses en HF heterocigota |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Fase 3 | Completado | 800 | Ecografía carotídea a 24 meses: torcetrapib/atorvastatina frente a atorvastatina sola en HF heterocigota |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Fase 3 | Completado | 272 | Estudio abierto de 3 años de atorvastatina en niños y adolescentes con HF heterocigota: crecimiento, desarrollo y reducción de colesterol |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Fase 3 | Completado | 621 | Ezetimiba 10 mg añadida a atorvastatina en HF heterocigota o cardiopatía coronaria/factores de riesgo con colesterol no controlado |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Fase 3 | Completado | 30 | Estudio abierto de titulación forzada de torcetrapib/atorvastatina en HF homocigota |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de 24 meses (seguridad y tolerabilidad) de ezetimiba con atorvastatina o simvastatina en HF homocigota |
| [NCT00145431](https://clinicaltrials.gov/study/NCT00145431) | Fase 3 | Terminado | 41 | Estudio cruzado doble ciego de torcetrapib/atorvastatina en disbetalipoproteinemia familiar. Terminó antes de tiempo por seguridad |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Fase 3 | Completado | 355 | Alirocumab añadido a atorvastatina frente a ezetimiba, aumento de dosis de atorvastatina o cambio a rosuvastatina, en pacientes no controlados (incluye HF heterocigota) |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Fase 1 | Completado | 39 | Farmacocinética, farmacodinamia y seguridad de atorvastatina en niños y adolescentes con HF heterocigota (8 semanas) |

---

## Evidencia de Literatura

Se muestran 10 de las 19 publicaciones. La mayoría son estudios clínicos o revisiones. No se identificó ningún ensayo aleatorizado explícitamente clasificado como tal.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Estudio clínico | J Clin Lipidol | Estudio de 3 años de atorvastatina en niños y adolescentes con HF heterocigota. Evalúa eficacia y seguridad más allá de un año, incluyendo niños desde los 6 años |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Estudio comparativo | Nutr Metab Cardiovasc Dis | Compara atorvastatina y simvastatina para alcanzar la meta de LDL-C (NCEP) en HF heterocigota, con cambios en fibrinógeno y otras variables de coagulación |
| [12883464](https://pubmed.ncbi.nlm.nih.gov/12883464/) | 2003 | Estudio clínico | Med Sci Monit | La atorvastatina reduce la microalbuminuria en pacientes con HF y tolerancia normal a la glucosa |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Estudio de cohorte | J Am Coll Cardiol | Cuantifica la reducción de eventos de enfermedad coronaria y de mortalidad con estatinas en HF heterocigota |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Revisión | Curr Atheroscler Rep | Revisión de terapias farmacológicas nuevas para reducir el LDL-C en HF homocigota |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Revisión | Ann Pharmacother | Eficacia y seguridad de atorvastatina en hipercolesterolemia primaria y dislipidemias mixtas |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Revisión | J Am Coll Cardiol | Mejora del monitoreo y la atención de pacientes con HF |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía clínica | Endocr Pract | Guías AACE/ACE para el manejo de dislipidemia y la prevención de enfermedad cardiovascular |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Estudio genético | Pharmacogenomics J | Estrategia de secuenciación que combina genes de HF con genes de respuesta a estatinas, para implementar la farmacogenómica |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Estudio de laboratorio | Toxicology | Miotoxicidad por estatinas (lipofílicas frente a hidrofílicas) en células musculares derivadas de pacientes con HF |

---

## Información de Mercado en Colombia

El Evidence Pack informa 17 registros sanitarios en total, pero solo detalla uno; las cinco filas listadas corresponden al mismo número de registro. Se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19950621 | ATORVASTATINA 20 MG COMPRIMIDOS CON CUBIERTA PELICULAR (fabricante: Sandoz GmbH) | Tableta cubierta con película | Solo figura «ATORVASTATIN» (sin texto de indicación) |

Además, el pack reporta la forma «Tableta recubierta», ambas de vía oral.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados y estudios pediátricos a largo plazo que respaldan el uso de atorvastatina en HF, sobre todo heterocigota. Sin embargo, es un uso ya establecido y no un reposicionamiento nuevo. En muchos ensayos la atorvastatina es tratamiento de base, y la respuesta en HF homocigota o con receptor nulo es limitada. Además, faltan datos de seguridad del prospecto de INVIMA, lo que bloquea la evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha de datos bloqueante)
- Completar el mecanismo de acción desde DrugBank
- Confirmar el texto real de la indicación aprobada en INVIMA, ya que el registro solo muestra el nombre del principio activo
- Detallar los 17 registros sanitarios, de los cuales solo uno está descrito
- Definir el manejo diferenciado de HF homocigota (terapia adicional) y de la población pediátrica

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de aplicarse.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

