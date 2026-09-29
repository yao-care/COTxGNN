---
layout: default
title: Omeprazole
parent: Evidencia Moderada (L3-L4)
nav_order: 307
evidence_level: L3
indication_count: 2
---

# Omeprazole
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **2** 
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

# Omeprazol: De Enfermedad por Reflujo Gastroesofágico y Exceso de Acidez Gástrica a Reflujo Duodenogástrico

## Resumen en Una Frase

Omeprazol es un inhibidor de la bomba de protones que se usa para reducir la acidez del estómago, por ejemplo en la enfermedad por reflujo gastroesofágico.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**,
pero solo hay **1 ensayo clínico** (sin relevancia directa) y **20 publicaciones**, en su mayoría estudios observacionales o en animales, y ninguna demuestra un beneficio del fármaco sobre este reflujo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad por reflujo gastroesofágico y otras causas de exceso de acidez gástrica (según datos farmacológicos; el registro INVIMA solo repite el nombre "OMEPRAZOL") |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información farmacológica disponible, omeprazol actúa sobre la ATPasa H+/K+ gástrica (gen *ATP4A*), la bomba de protones de las células del estómago. Al bloquearla reduce la producción de ácido. Su eficacia en el exceso de acidez y el reflujo gastroesofágico está bien establecida.

El reflujo duodenogástrico es el paso de contenido duodenal (bilis) hacia el estómago. Se relaciona con síntomas de reflujo y con lesión de la mucosa, y a menudo aparece junto con la enfermedad por reflujo ácido y el esófago de Barrett. Esa cercanía clínica explica que el modelo relacione ambas enfermedades. Varios estudios en humanos con esófago de Barrett (PMID 10994616 y 9824338) evaluaron el efecto de omeprazol sobre el reflujo biliar.

Sin embargo, el mecanismo no es claro a favor del fármaco. Omeprazol suprime el ácido, pero no se sabe que reduzca el reflujo de bilis en sí. Además, dos estudios en ratas (PMID 33027361 y 10389684) sugieren que bloquear el ácido junto con el reflujo duodenogástrico podría favorecer la carcinogénesis gástrica. Un posible beneficio sobre los síntomas o la lesión de la mucosa es plausible, pero el beneficio neto sobre el reflujo no está demostrado. El puntaje alto de TxGNN es solo una predicción y ningún dato de eficacia intervencionista lo respalda.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | Completado | 157 | Estudio diagnóstico con imagen endoscópica trimodal para distinguir dispepsia funcional de enfermedad por reflujo (ácido o biliar). No evalúa omeprazol como intervención, por lo que no aporta evidencia de eficacia. |

## Evidencia de Literatura

No se identificaron ensayos clínicos aleatorizados. La tabla prioriza los estudios clínicos con omeprazol y los estudios en animales relevantes para seguridad.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Estudio clínico | Scand J Gastroenterol | Efecto de omeprazol sobre el reflujo duodenogástrico antral en esófago de Barrett. Parte de la hipótesis de que omeprazol podría reducirlo. |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Estudio clínico | Gut | Efecto de omeprazol 20 mg dos veces al día sobre el reflujo biliar duodenogástrico y duodenogastroesofágico en esófago de Barrett. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Estudio prospectivo | J Pediatr Gastroenterol Nutr | Tratamiento con omeprazol del reflujo biliar esofágico en niños. |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Estudio clínico | Am J Gastroenterol | Mayor reflujo ácido y biliar en esófago de Barrett que en esofagitis, y efecto del tratamiento con inhibidores de la bomba de protones. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Estudio clínico | J Gastrointest Surg | Reflujo biliar en esófago de Barrett benigno y maligno, con supresión ácida médica frente a fundoplicatura de Nissen. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Observacional | Eur J Pediatr | Seis pacientes jóvenes con reflujo duodenogástrico primario, síntomas atípicos y sin respuesta a antiácidos clásicos. |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Estudio clínico | Am J Gastroenterol | Compara el reflujo duodenogastroesofágico y ácido entre pacientes que respondieron y que no respondieron a un inhibidor de la bomba de protones una vez al día. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal (rata) | Acta Cir Bras | Papel de omeprazol y nitritos en la mucosa gástrica de ratas con reflujo duodenogástrico inducido, en busca de un posible efecto protector frente al adenocarcinoma. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal (rata) | Dig Dis Sci | El bloqueo ácido con omeprazol promovió la carcinogénesis gástrica inducida por reflujo duodenogástrico. Es una señal preclínica de seguridad. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal (rata) | Dig Dis Sci | El reflujo duodenogástrico estimula el crecimiento de la mucosa del tubo digestivo alto, y el bloqueo ácido potencia este efecto. |

## Información de Mercado en Colombia

Los 20 registros corresponden a la misma licencia repetida, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20066112 | OMEPRAZOL 40 MG (COLMED LTDA) | Cápsula dura | No especificada (el texto registrado solo dice "OMEPRAZOL") |

## Consideraciones de Seguridad

- **Señal preclínica:** dos estudios en ratas (PMID 10389684 y 8943968) indican que combinar bloqueo ácido con reflujo duodenogástrico potencia el crecimiento de la mucosa y puede promover carcinogénesis gástrica. No se ha confirmado en humanos, pero conviene evaluarlo antes de cualquier uso en esta indicación.
- **Interacciones farmacológicas:** los datos disponibles corresponden a dianas farmacológicas de omeprazol (*ATP4A*, la bomba de protones, y *CLCN2*), no a interacciones clínicas con otros medicamentos.

Para advertencias, contraindicaciones e interacciones clínicas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay evidencia intervencionista de que omeprazol beneficie el reflujo duodenogástrico. El único ensayo registrado es diagnóstico y no prueba el fármaco. Los estudios clínicos son observacionales y hay una señal preclínica de seguridad (carcinogénesis gástrica en ratas). El puntaje TxGNN de 99.64% es solo una predicción, y lo apropiado es tratarla como pregunta de investigación.

**Para avanzar se necesita:**
- Ensayos aleatorizados o estudios comparativos que midan el efecto de omeprazol sobre el reflujo duodenogástrico y sus desenlaces clínicos.
- Evaluación de la señal de carcinogénesis gástrica observada en ratas, con datos de seguimiento en humanos.
- Prospecto de INVIMA (advertencias y contraindicaciones) y la indicación aprobada en cada registro.
- Datos formales del mecanismo de acción (DrugBank) para comparar con la indicación original.

**Nota sobre la segunda predicción (obstrucción duodenal, TxGNN 99.64%):** el nivel de evidencia es L4 y la recomendación es Hold. Los ensayos identificados (NCT01265550 y NCT00557921) no evalúan esta condición. La resolución de la obstrucción en la literatura se atribuye principalmente a la erradicación de *H. pylori*, no a omeprazol solo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

