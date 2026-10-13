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

# Acetaminofén: De Paracetamol (indicación registrada) a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

El acetaminofén (paracetamol) es un analgésico y antipirético de uso muy extendido; en Colombia sus registros sanitarios figuran con la indicación "paracetamol" en presentaciones intravenosas.
El modelo TxGNN predice que podría ser efectivo para **migraña con aura del tronco encefálico**, pero no hay ensayos clínicos registrados y la literatura disponible (20 publicaciones) trata la migraña en general, no este subtipo, por lo que la evidencia es indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol (texto tal como figura en el registro INVIMA) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.15% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, el acetaminofén actúa como analgésico y antipirético, con inhibición central de la ciclooxigenasa (COX) y modulación de vías serotoninérgicas y de dolor descendente. Los datos farmacológicos compilados lo vinculan con TRPV4, COX-1 y COX-2, y señalan que no tiene efecto antiinflamatorio ni antiplaquetario significativo ni irrita la mucosa gástrica.

El acetaminofén es un tratamiento reconocido para el ataque agudo de migraña en general; la evaluación de evidencia de la Sociedad Americana de Cefalea (2015) respalda su uso. Sin embargo, ninguna de las publicaciones aportadas aborda específicamente la migraña con aura del tronco encefálico. La evidencia se extrapola desde la migraña en general, y el puntaje alto de TxGNN refleja cercanía computacional con la clase amplia de enfermedades migrañosas.

Este subtipo tiene fisiopatología propia y precauciones de tratamiento particulares (por ejemplo, la cautela con vasoconstrictores como los triptanes). El perfil vascular relativamente benigno del acetaminofén lo hace plausible, pero no está verificado para este subtipo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se listan las publicaciones más relevantes (prioridad: guías/ECA, luego revisiones). Ninguna estudia específicamente la migraña con aura del tronco encefálico.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revisión/Guía | Headache | Evaluación de la evidencia de las terapias farmacológicas para la migraña aguda, de la Sociedad Americana de Cefalea |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | ECA (análisis de 3 estudios) | Clin Ther | Combinación de acetaminofén, aspirina y cafeína en migraña asociada a la menstruación, controlada con placebo |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Estudio comparativo | Headache | Isometepteno, diclorafenazona y acetaminofén frente a sumatriptán en migraña leve a moderada |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Revisión (ubrogepant; indirecto) | Neurol Int | Tratamiento de la migraña aguda; menciona el acetaminofén como opción de primera línea no prescrita |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Revisión | Cureus | Terapias abortivas y profilácticas de la migraña en el embarazo |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Revisión | Neurol Clin | Cefalea en el embarazo y el puerperio; el acetaminofén es el tratamiento sintomático de primera línea |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Revisión | Handb Clin Neurol | Estado migrañoso y su carga sanitaria |
| [23203776](https://pubmed.ncbi.nlm.nih.gov/23203776/) | 2013 | Revisión | Curr Treat Options Neurol | Diagnóstico y tratamiento de la migraña hemipléjica familiar y esporádica (subtipo de migraña con aura) |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Revisión | Pediatr Ann | Tratamiento de la migraña pediátrica |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Revisión | Cureus | Abordaje de la migraña durante el embarazo y la lactancia |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20198205 | Paracetamol 1% infusión intravenosa (Otsuka Pharmaceutical India) | Solución concentrada para infusión | Paracetamol |
| 20048683 | Paracetamol (acetaminofén) 1 g/100 mL solución para infusión (Fresenius Kabi) | Solución inyectable | Paracetamol |
| 20039397 | Paracetamol solución inyectable 500 mg/50 mL (Fresenius Kabi) | Solución inyectable | Paracetamol |

Los tres registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento (no proviene del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, cirrosis hepática, encefalopatía hepática y coma hepático.
- **Interacciones farmacológicas / dianas farmacológicas:** se identificaron 3 asociaciones de tipo farmacológico (dianas TRPV4, COX-1 y COX-2). Corresponden a dianas moleculares y no a interacciones clínicas con otros medicamentos, y no tienen nivel de gravedad asignado.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura indirecta sobre migraña en general (nivel L4), sin ensayos clínicos ni estudios del subtipo con aura del tronco encefálico. Además, no hay registros sanitarios vigentes en Colombia y falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo al cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia específica del subtipo (migraña con aura del tronco encefálico), incluidas series de casos o estudios observacionales.
- Evaluar la seguridad en pacientes con enfermedad hepática, dada la señal de contraindicaciones del grafo de conocimiento.
- Aclarar la situación regulatoria: confirmar si existen presentaciones vigentes (por ejemplo, orales) y la compatibilidad de la vía de administración, ya que los registros hallados son solo intravenosos y cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

