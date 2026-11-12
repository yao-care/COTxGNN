---
layout: default
title: Dexlansoprazole
parent: Solo Predicción del Modelo (L5)
nav_order: 212
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Dexlansoprazole: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). Indicación original: DEXLANSOPRAZOL"
monitor_inn: "dexlansoprazole"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
---

# Dexlansoprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Dexlansoprazol: De Indicación Registrada (Dexlansoprazol) a Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

Dexlansoprazol es un inhibidor de la bomba de protones (IBP) de liberación retardada, registrado en Colombia bajo el nombre del propio principio activo, sin una indicación detallada en el texto del registro.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ulcerosa péptica activa**, con **2 ensayos clínicos de Fase 3** (ambos sobre esofagitis erosiva, es decir, evidencia indirecta) y **3 publicaciones** que actualmente respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DEXLANSOPRAZOL (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la información conocida, dexlansoprazol es un IBP, enantiómero de lansoprazol, que inhibe de forma irreversible la bomba H+/K+ ATPasa de la célula parietal gástrica y produce una supresión ácida sostenida.

La úlcera péptica depende del ácido gástrico, por lo que la supresión ácida es un mecanismo reconocido para su cicatrización. Esto hace que la predicción sea mecanísticamente plausible, y que otros IBP ya se usen como tratamiento estándar en esta enfermedad.

Sin embargo, los ensayos de Fase 3 disponibles evaluaron esofagitis erosiva, no úlcera péptica. Demuestran eficacia en supresión ácida y seguridad, pero no cicatrización de úlceras. La plausibilidad se apoya en el mecanismo de clase, no en datos directos del fármaco en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Fase 3 | Completado | 2054 | Dexlansoprazol MR (60 y 90 mg) vs lansoprazol 30 mg en cicatrización de esofagitis erosiva a 8 semanas. Apoyo indirecto. |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Fase 3 | Completado | 2038 | Diseño similar al anterior, con criterios de valoración de esofagitis y no de úlcera péptica. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisión sistemática / metaanálisis en red | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potasio (P-CAB) con IBP en esofagitis grado C/D. No aborda úlcera. |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Revisión | Curr Opin Investig Drugs | Describe el desarrollo de dexlansoprazol, formulación de liberación modificada de un enantiómero de lansoprazol, para esofagitis por reflujo. |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclínico/mecanístico | J Chin Med Assoc | Estudia la supresión de la ATPasa vacuolar y el estrés del retículo endoplásmico por IBP, en relación con el riesgo de cáncer gástrico. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20201891 | DEXLANZOPRAL 60 DR | Cápsula dura | DEXLANSOPRAZOL |
| 20224127 | LANSODEX® 60 MG CÁPSULAS DE LIBERACIÓN RETARDADA | Cápsula con cubierta entérica | DEXLANSOPRAZOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento de TxGNN (PrimeKG) asocia el fármaco con enfermedad hepática, enfermedad de la vesícula biliar, osteoporosis, osteoporosis posmenopáusica y fractura ósea. Deben verificarse contra el prospecto antes de cualquier uso.
- **Interacciones farmacológicas:** se identificaron 118 interacciones. Entre las de mayor gravedad (nivel Major) figuran:
  - Acalabrutinib
  - Atazanavir

  Entre las de nivel moderado destacan furosemida, hidroclorotiazida, anfotericina B, amikacina, gefitinib, bosutinib, fosamprenavir y foscarnet. Con ácido acetilsalicílico, axitinib, brivaracetam y cianocobalamina las interacciones son de nivel menor.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo es plausible, pero la evidencia es de nivel L4 y no incluye ningún ensayo que pruebe la cicatrización de úlcera péptica con dexlansoprazol; los ensayos de Fase 3 son de esofagitis. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-dexlansoprazole-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los dos registros sanitarios en Colombia están cancelados, y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dexlansoprazole-1 -->

**Para avanzar se necesita:**
- Esperar los resultados del ensayo [NCT07344506](https://clinicaltrials.gov/study/NCT07344506) (Fase 4, en reclutamiento, n=942), que compara dexlansoprazol, lansoprazol y vonoprazán en la erradicación de *H. pylori*. Es el ensayo más cercano a la indicación, aunque aún sin resultados.
- Obtener del INVIMA el prospecto con advertencias y contraindicaciones, y verificar las señales de enfermedad hepática y salud ósea.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Revisar con prioridad las interacciones de nivel Major (acalabrutinib, atazanavir).

<!-- review:begin co-lic-20261105-dexlansoprazole-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria: ambos registros están cancelados, por lo que sería necesario un nuevo registro o una reactivación. / Revisar con prioridad las interacciones de nivel Major (acalabrutinib, atazanavir)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dexlansoprazole-2 -->

**Otras predicciones del modelo (para referencia):** la úlcera gástrica y la úlcera duodenal también tienen nivel L4 con apoyo indirecto similar. Gastroyeyunal (úlcera marginal) tiene nivel L4, con un único ensayo retirado. Perforación ulcerosa, gastroduodenitis, obstrucción duodenal, reflujo duodenogástrico, aclorhidria y estómago en botella de cuero tienen solo predicción del modelo (L5). Algunas de ellas, como aclorhidria y estómago en botella de cuero, parecen artefactos del modelo y no se recomienda perseguirlas.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "los dos registros sanitarios en Colombia están cancelados, y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria: ambos registros están cancelados, por lo que sería necesario un nuevo registro o una reactivación" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

