---
layout: default
title: Acetaminophen
parent: Evidencia Moderada (L3-L4)
nav_order: 19
evidence_level: L4
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Acetaminofén: De Dolor y Fiebre a Migraña con Aura de Tronco Encefálico

## Resumen en Una Frase

El acetaminofén (paracetamol) es un analgésico y antipirético de uso muy extendido, indicado originalmente para aliviar el dolor y reducir la fiebre.
El modelo TxGNN predice que podría ser efectivo para **migraña con aura de tronco encefálico**,
pero hay **0 ensayos clínicos** y **20 publicaciones**, todas sobre migraña en general y ninguna sobre este subtipo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor y fiebre (uso conocido). El texto del registro INVIMA solo dice "PARACETAMOL" |
| Nueva Indicación Predicha | Migraña con aura de tronco encefálico |
| Puntaje de Predicción TxGNN | 99.15% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada. Según la información conocida, el acetaminofén es un analgésico y antipirético cuya eficacia en dolor y fiebre está comprobada. Sus dianas farmacológicas registradas son COX-1 (PTGS1), COX-2 (PTGS2) y TRPV4. Su acción analgésica central, probablemente por modulación de COX/prostaglandinas y efectos sobre las vías serotoninérgicas descendentes, es plausible para el dolor migrañoso.

La predicción probablemente refleja que el acetaminofén ya es un tratamiento establecido para la migraña aguda: la evaluación de evidencia de la American Headache Society (2015) lo incluye. La migraña con aura de tronco encefálico es un subtipo de migraña con aura, así que la relación con el uso original es indirecta, a través del dolor de cabeza.

Ninguna de las publicaciones recuperadas aborda específicamente el subtipo con aura de tronco encefálico. Se trata de evidencia indirecta de la migraña en general y **no de una señal novedosa de reposicionamiento**. El puntaje alto de TxGNN no verifica un mecanismo propio para este subtipo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | ECA | Arch Intern Med | ECA poblacional, doble ciego y controlado con placebo, sobre eficacia y seguridad del acetaminofén en migraña (el resumen disponible no incluye resultados) |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | ECA (3 ensayos) | Arch Neurol | Tres ECA doble ciego con placebo de la combinación acetaminofén, aspirina y cafeína para aliviar el dolor de migraña |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Análisis retrospectivo de 3 ECA | Clin Ther | Evalúa la misma combinación en migraña asociada a la menstruación frente a migraña no menstrual |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guía / revisión sistemática | Headache | Evaluación actualizada de la evidencia de terapias farmacológicas para la migraña aguda (American Headache Society) |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Revisión | Handb Clin Neurol | Estado migrañoso, complicación de la migraña con o sin aura: definición, carga e impacto funcional |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Revisión | Neurol Clin | Cefalea en embarazo y puerperio; el acetaminofén es el tratamiento sintomático de primera línea |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Revisión | Cureus | Terapias abortivas y profilácticas de la migraña en el embarazo |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Revisión | Cureus | Relación y abordaje de la migraña en embarazo y lactancia |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Revisión | Pediatr Ann | Tratamiento de la migraña pediátrica: medidas conductuales, tratamiento agudo y preventivo |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Revisión | Neurol Int | Ubrogepant en migraña aguda; menciona el acetaminofén entre los tratamientos de la migraña leve a moderada |

## Información de Mercado en Colombia

Se muestran los registros únicos; el paquete de datos repite varias filas del mismo registro.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20198205 | PARACETAMOL 1% INFUSION INTRAVENOSA (Otsuka Pharmaceutical India) | Solución concentrada para infusión | PARACETAMOL (sin detalle de indicación) |
| 20048683 | PARACETAMOL (ACETAMINOFEN) 1G/100ML SOLUCION PARA INFUSION (Fresenius Kabi Deutschland) | Solución inyectable | PARACETAMOL (sin detalle de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto (99.15%), pero no hay ensayos clínicos ni literatura específica para migraña con aura de tronco encefálico. La evidencia disponible es indirecta y proviene de la migraña en general, donde el acetaminofén ya se usa. Además, falta la información de seguridad del prospecto de INVIMA, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar evidencia específica sobre migraña con aura de tronco encefálico, incluyendo ensayos clínicos.
- Confirmar las indicaciones aprobadas en los registros sanitarios, ya que el texto actual solo indica "PARACETAMOL".
- Definir la compatibilidad de vías de administración: los registros colombianos identificados son formas de infusión intravenosa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

