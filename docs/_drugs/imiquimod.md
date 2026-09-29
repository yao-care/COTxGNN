---
layout: default
title: Imiquimod
parent: Evidencia Alta (L1-L2)
nav_order: 220
evidence_level: L2
indication_count: 10
---

# Imiquimod
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Imiquimod: De Indicación No Especificada en el Registro a Neoplasia Premaligna

## Resumen en Una Frase

Imiquimod es un modulador inmunitario de uso tópico, comercializado en Colombia en crema (Virosupril®). El texto del registro sanitario solo menciona el principio activo, sin describir la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia premaligna**, con **19 ensayos clínicos** y **9 publicaciones** asociados. Muchos de los ensayos usan imiquimod solo como adyuvante de vacunas en tumores ya invasivos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "IMIQUIMOD") |
| Nueva Indicación Predicha | Neoplasia premaligna (pre-malignant neoplasm) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Imiquimod es un agonista del receptor TLR7. Al aplicarse sobre la lesión, induce inmunidad innata y adaptativa local: liberación de interferón alfa, TNF-alfa e IL-12 y reclutamiento de linfocitos T citotóxicos. Los datos de mecanismo de DrugBank no están disponibles en el paquete de evidencia. La descripción anterior proviene del análisis de racional de reposicionamiento.

Este mecanismo es plausible para eliminar epitelio displásico. Las revisiones y estudios incluidos cubren queratosis actínica, neoplasia intraepitelial vulvar y anal, papulosis bowenoide, neoplasia intraepitelial cervical (NIC) y lentigo maligno.

Un matiz importante: la queratosis actínica ya es un uso con indicación en etiqueta. Por eso, parte de la señal predicha se solapa con la indicación existente y no es del todo una indicación nueva. Las lesiones premalignas genitales, cervicales y orales sí serían usos nuevos.

## Evidencia de Ensayos Clínicos

Se muestran los 9 ensayos más relevantes para lesiones premalignas o intraepiteliales, de un total de 19 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Fase 2 | Completado | 90 | ECA de imiquimod tópico en lesiones intraepiteliales cervicales de alto grado |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Fase 3 | Completado | 259 | Imiquimod neoadyuvante para reducir el tamaño de la escisión en lentigo maligno de la cara (proliferación melanocítica intraepidérmica) |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | ECA de imiquimod tópico en NIC de alto grado. Terminado con solo 9 pacientes, sin poder estadístico |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Fase 2 | Completado | 5 | Estudio exploratorio de imiquimod en neoplasia intraepitelial vulvar (NIV 2/3) y verrugas anogenitales, con análisis de mecanismos inmunitarios |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Fase 1 | Terminado | 49 | ECA que compara imiquimod 5 %, 0.05 % y gel nanoencapsulado 0.05 % en queilitis actínica |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Fase 4 | Desconocido | 20 | Imiquimod 3.75 % tras crioterapia en queratosis actínicas hipertróficas de manos y antebrazos |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Estudio abierto de imiquimod 5 % en queratosis actínicas de la cabeza |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Fase 3 | Desconocido | 145 | Escisión quirúrgica frente a curetaje más imiquimod en carcinoma basocelular nodular (enfermedad invasiva) |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Fase 1 temprana | Completado | 16 | Imiquimod neoadyuvante en carcinoma oral de células escamosas en estadio temprano (enfermedad invasiva) |

Los demás ensayos usan imiquimod como adyuvante de vacunas en glioma, melanoma, próstata y pulmón. No aportan evidencia sobre lesiones premalignas.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revisión (Cochrane) | Cochrane Database Syst Rev | Intervenciones para la neoplasia intraepitelial del canal anal, condición premaligna asociada a VPH |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revisión (Cochrane) | Cochrane Database Syst Rev | Tratamientos médicos para la neoplasia intraepitelial vulvar de alto grado |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Terapia fotodinámica combinada para cáncer de piel no melanoma |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión | Skin Therapy Lett | Manejo actual de las queratosis actínicas, lesiones premalignas con potencial de progresar a carcinoma escamoso |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión | Semin Cutan Med Surg | Estrategias tópicas (fluorouracilo, diclofenaco, imiquimod, terapia fotodinámica) para cáncer de piel no melanoma y lesiones precursoras |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclínico | Urol Oncol | Farmacocinética de agonistas de TLR7 (TMX-101 y TMX-202) en rata para cáncer de vejiga; no evalúa imiquimod directamente |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de caso | Int J STD AIDS | Tratamiento exitoso de NIV de alto grado con imiquimod 5 % en una receptora de trasplante renal |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de caso | Int J STD AIDS | Aclaramiento de papulosis bowenoide del pene con crema de imiquimod 5 %, bien tolerada |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Otro (reporte de caso) | Hautarzt | Imagen por tomografía de coherencia óptica de poroqueratosis actínica; relevancia indirecta |

## Información de Mercado en Colombia

Según el paquete de evidencia, hay 20 registros. En la muestra disponible solo aparecen dos números de registro distintos, repetidos varias veces.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128548 | VIROSUPRIL® CREMA 3.75 % (MEGALABS COLOMBIA S.A.S) | Crema tópica | Solo figura el principio activo (imiquimod); sin texto de indicación |
| 19967737 | VIROSUPRIL® CREMA (MEGALABS COLOMBIA S.A.S) | Crema tópica | Solo figura el principio activo (imiquimod); sin texto de indicación |

## Consideraciones de Seguridad

No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas en el paquete de evidencia. Consultar el prospecto para información de seguridad.

La literatura asociada a otras indicaciones predichas señala eventos que conviene vigilar:
- Conversión maligna de una papilomatosis oral y labial florida durante el tratamiento tópico con imiquimod ([PMID 12719972](https://pubmed.ncbi.nlm.nih.gov/12719972/)).
- Carcinoma mucinoso cutáneo que apareció en una enfermedad de Paget extramamaria tras 2 meses de imiquimod 5 % ([PMID 21885944](https://pubmed.ncbi.nlm.nih.gov/21885944/)).
- Eritema multiforme en un paciente con síndrome de Gorlin ([PMID 29173871](https://pubmed.ncbi.nlm.nih.gov/29173871/)).
- Liquen planopilar tras imiquimod 5 % ([PMID 24575881](https://pubmed.ncbi.nlm.nih.gov/24575881/)).

Son reportes de caso y no permiten estimar frecuencia.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado en NIC de alto grado (90 pacientes) y un ensayo de Fase 3 completado en lentigo maligno (259 pacientes). El mecanismo TLR7 es plausible y hay revisiones que respaldan su uso en lesiones intraepiteliales. Sin embargo, el único ECA de Fase 3 directamente dirigido a NIC se terminó con 9 pacientes, y parte de la señal se solapa con la queratosis actínica, que ya es un uso en etiqueta.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones, que hoy es un vacío bloqueante para el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank y aclarar la indicación aprobada de los registros Virosupril®.
- Definir qué lesión premaligna se prioriza (NIC, NIV, queilitis actínica u otra) y cuál sería su vía de administración, ya que la compatibilidad de vía aún no está evaluada.
- Revisar los resultados publicados de NCT03233412 y NCT01720407 antes de proponer un estudio confirmatorio.
- Tratar las demás predicciones como preguntas de investigación o mantenerlas en espera. La neoplasia benigna de mucosa bucal (L4) tiene una señal de seguridad de conversión maligna. Las restantes (neuroblastoma cervical, quiste odontogénico, neoplasia benigna de lengua, teratoma nasofaríngeo, neoplasia quística, neoplasia del oído interno, neoplasia de glándula salival mayor y schwannoma del foramen yugular) tienen evidencia nula o solo indirecta (L4-L5) y quedan en Hold.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

